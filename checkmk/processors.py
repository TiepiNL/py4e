'''
'''
from collections import abc
import json
import logging as log
from os import getenv
from os.path import exists
import pathlib
from platform import system
import re
from shlex import quote
from shlex import split
import subprocess
import sys

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

try:
    import yaml
except ModuleNotFoundError as error:
    logtxt = f"Can't import yaml: {error}. Install it with 'pip install pyyaml'."
    log.error(logtxt)
    sys.exit(1)

# pywin32 is (only) required on Windows systems.
if system() == 'Windows':
    try:
        import win32api
        import win32serviceutil
    except ModuleNotFoundError as error:
        logtxt = (
            f"Can't import win32serviceutil: {error}."
            f"Install it with 'pip install pywin32'."
        )
        log.error(logtxt)
        sys.exit(1)


def run_command(command_line, timeout_sec=10):
    ''' (str, [int]) -> str

    Execute shell command 'command_line' synchronously and return the captured stdout.
    The child process will be killed if the 'timeout' (s) expires.

    >>> stdout = run_command("""powershell 'Write-Host "test"'""")
    >>> stdout.strip()
    'test'
    '''
    # Break the shell command into a sequence of arguments.
    cmd_args = split(command_line)
    try:
        result = subprocess.run(
            cmd_args, text=True, capture_output=True, check=True, timeout=timeout_sec)
    except OSError as err:
        # The system cannot find the file specified?
        log.error(err)
        sys.exit(1)
    except subprocess.TimeoutExpired as err:
        # Command timed out after x seconds.
        log.error(err)
        sys.exit(1)
    except subprocess.CalledProcessError as err:
        #  Command returned non-zero exit status.
        log.error(err)
        sys.exit(1)

    return result.stdout


def run_command_async(command_line):
    ''' (str) -> NoneType

    Execute shell command 'command_line' asynchronously.
    '''
    # Break the shell command into a sequence of arguments.
    cmd_args = split(command_line)
    try:
        subprocess.Popen(cmd_args)
    except OSError as err:
        log.error(err)
        sys.exit(1)


def read_textfile(file):
    ''' (str) -> list

    Open text file 'file' and return the content as a list of lines.
    '''
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode='r', encoding='utf-8') as fopen:
            lines = fopen.readlines()
    except OSError as err:
        log.error(err)
        sys.exit(1)

    return lines


def write_textfile(file, content):
    ''' (str, str) -> NoneType

    Open 'file' and (over)write 'content' to it.

    Precondition: len(file) > 0
    '''
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode='w', encoding='utf-8') as fopen:
            fopen.write(content)
    except OSError as err:
        log.error(err)
        sys.exit(1)


def save(filename, content, ext='*'):
    ''' (str, str, [str]) -> NoneType

    Open a save file filedialog with default filename 'filename',
    and write 'content' to it. Optionally, add a file extension ('ext)
    to populate the "save file as" list.
    '''
    files = [('All Files', '*.*')]
    match ext:
        case 'json':
            files.append(('Json Document', '*.json'))
        case 'yml':
            files.append(('Yaml Document', '*.yml'))
        case 'log':
            files.append(('Yaml Document', '*.log'))
        case 'txt':
            files.append(('Text Document', '*.txt'))

    file_out = asksaveasfile(filetypes=files, defaultextension=files, initialfile=filename)
    # Make sure we received a filename (tkinter has input validation but user can still cancel).
    if file_out:
        # Write output to location specified by user in "Save As" dialogue.
        write_textfile(file_out, content)
    else:
        log.info("No filename provided - can't save content.")


def filter_list(lst, regex):
    ''' (list, str) -> NoneType

    Remove (pop) items in 'lst' that don't match 'regex'.
    '''
    # Loop in reversed order to avoid index out of range errors.
    for i in reversed(range(len(lst))):
        if not re.match(regex, lst[i]):
            lst.pop(i)


def get_empty_agent_sections(events):
    ''' (list) -> list

    '''
    empty_sections = list()
    for event in events:
        # Check for potentially unused agent sections.
        # These lines look like:
        # 2021-12-21 23:44:58.516 [Warn ] Section 'mrpe' cannot provide data
        pattern = re.compile("Section '[a-z_]*' cannot provide data")
        if pattern.search(event):
            # Only interested in unique section names (the part between single quotes).
            section = event.split("'")[1]
            if section not in empty_sections:
                empty_sections.append(section)

    return empty_sections


def is_admin():
    ''' () -> int

    Returns 1 if and only if the user is admin and the session is elevated,
    otherwise return 0.
    '''
    if system() == 'Windows':
        #pylint: disable-next=import-outside-toplevel
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as err:
            log.error(err)
            log.info('Admin check failed, assuming not an admin.')
            return 0
    else:
        #pylint: disable-next=redefined-outer-name
        logtxt = f"Unsupported operating system for this module: {system()}"
        log.error(logtxt)
        sys.exit(1)


def restart_service(service_name):
    ''' (str) -> bool

    Restart the 'service_name' (not the display name!) service,
    and return success/failure.
    '''
    try:
        win32serviceutil.RestartService(service_name)
    except win32api.error as err:
        logtxt = f"Could not restart the '{service_name}' service. {err}."
        log.error(logtxt)
        return False
    logtxt = f"Successfully restarted the '{service_name}' service."
    log.info(logtxt)
    return True


def reload_agent_config():
    ''' () -> bool

    Reload the Check MK Agent configuration, and return success/failure.
    '''
    exe = get_agent_exe()
    cmd = f"{quote(exe)} reload_config"
    result = run_command(cmd)

    # The last line of the output should be "Done."
    if result.strip()[-5:] != 'Done.':
        log.warning("Something went wrong while reloading the agent config.")
        return False
    else:
        logtxt = "Successfully reloaded the agent configuration."
        log.info(logtxt)
        return True


def get_agent_exe():
    ''' () -> str
    Use the registry to get the path of the agent executable.
    This should return a string like:
    "C:\\Program Files (x86)\\checkmk\\service\\check_mk_agent.exe"
    '''
    try:
        exe = win32serviceutil.LocateSpecificServiceExe('CheckMkService').strip('"')
    except win32api.error as err:
        log.warning(err)
        # Alternatively, use the default path.
        exe = f"{getenv('ProgramFiles(x86)')}\\checkmk\\service\\check_mk_agent.exe"

    if not exists(exe):
        #pylint: disable-next=redefined-outer-name
        logtxt = f"checkmk agent not found: {exe} doesn't exist or access denied!"
        log.error(logtxt)
        sys.exit(1)

    return exe


def get_agent_log():
    ''' () -> str

    Return a validated agent log filepath.
    '''
    agent_log_file = f"{getenv('PROGRAMDATA')}\\checkmk\\agent\\log\\check_mk.log"

    if not exists(agent_log_file):
        #pylint: disable-next=redefined-outer-name
        logtxt = f"checkmk agent log not found: {agent_log_file} doesn't exist or access denied!"
        log.error(logtxt)
        sys.exit(1)

    return agent_log_file


def get_config_path(config_type):
    ''' (str) -> str

    Return the path of the matching config_type.

    For the agent configuration three files are read sequentially and
    hierarchically: 1) default, 2) bakery, and 3) user.

    (Assuming systemroot is C)
    >>> get_config_path('default')
    'C:\\\\Program Files (x86)\\\\checkmk\\\\service\\\\check_mk.yml'
    >>> get_config_path('bakery')
    'C:\\\\ProgramData\\\\checkmk\\\\agent\\\\bakery\\\\check_mk.bakery.yml'
    >>> get_config_path('user')
    'C:\\\\ProgramData\\\\checkmk\\\\agent\\\\check_mk.user.yml'
    '''
    if system() == 'Windows':

        custom_agent_path = f"{getenv('PROGRAMDATA')}\\checkmk\\agent"

        match config_type:
            case 'default':
                # 1) The default configuration is stored here.
                cfg = f"{getenv('ProgramFiles(x86)')}\\checkmk\\service\\check_mk.yml"
            case 'bakery':
                # 2) Created by the Agent Bakery, and overrides the default values.
                cfg = f"{custom_agent_path}\\bakery\\check_mk.bakery.yml"
            case 'user':
                # 3) For manual customizations. overrides default and Bakery values.
                cfg = f"{custom_agent_path}\\check_mk.user.yml"

        return cfg


def yaml2dict(yaml_object):
    ''' (str) -> dict

    Returns the converted yaml_object string as dictionary.

    precondition: yaml_object is valid yaml
    '''
    return yaml.safe_load(yaml_object)


def yaml2json(yaml_object):
    ''' (str) -> str

    Returns the converted yaml_object string as json.

    precondition: yaml_object is valid yaml
    '''
    dict_object = yaml2dict(yaml_object)
    return dict2json(dict_object)


def dict2json(dict_object):
    ''' (dict) -> str

    Returns the dict_object as json string.
    '''
    # Serializing json
    return json.dumps(dict_object, indent=4)


def dict2yaml(dict_object):
    ''' (dict) -> str

    Returns the dict_object as yaml string.
    '''
    return yaml.dump(dict_object)


#pylint: disable-next=dangerous-default-value
def strip_yaml(lines, prefix_to_skip='_'):
    ''' (list2, [str]) -> list

    '''
    spaces = 0
    skip_line = False
    clean_lines = []
    for line in lines:
        # ...
        if len(line.strip()) == 0:
            continue
        if line.lstrip().startswith('#'):
            continue

        # yaml files can have example code, e.g. keys that start with an underscore.
        # Filter out all lines that start with items in 'prefix', and all subsequent lines
        # if they have a larger indentation (=subkeys). This is tracked with the skip_line var.
        if skip_line:
            # the previous line has been skipped. Examine if the current
            # line should be skipped too, based on indentation.
            # Do so by comparing the length of a right-trimmed line with a
            # fully trimmed line length.
            indent = len(line.rstrip()) - len(line.strip())
            # Only skip larger indented lines because if the indentation is
            # equal, it's not a subkey of the skipped key.
            # Otherwise reset the 'skip' flag.
            if indent > spaces:
                continue
            else:
                skip_line = False

        if line.lstrip().startswith(prefix_to_skip):
            # Get the indentation aka the amount of prefixed spaces.
            pos = line.find(prefix_to_skip)
            spaces = len(line[:pos])
            # Make sure the identation of the next line gets examined.
            skip_line = True
            continue

        # Strip in-line comments.
        pos = line.find('#')
        if pos != -1:
            line = line[:pos]

        clean_lines.append(line.rstrip())

    return clean_lines


def get_agent_config(config_type):
    ''' (str) -> str

    Return the content of the config_type configuration file.
    '''
    cfg = get_config_path(config_type)
    lines = read_textfile(cfg)
    clean_lines = strip_yaml(lines)
    return '\n'.join(clean_lines)


def nested_dict_iter(nested):
    for key, value in nested.items():
        if isinstance(value, abc.Mapping):
            yield from nested_dict_iter(value)
        else:
            yield key, value


def find_needle_in_dict(needle, dictionary):
    pairs = list(nested_dict_iter(dictionary))
    values = []
    for pair in pairs:
        if pair[0] == needle:
            values.append(str(pair[1]))
    return values


def get_setting(key, dictionary, section='all'):
    ''' (str, dict, [str]) -> str

    Return the value of 'key' if it exists in 'dictionary', optionally scoped to 'section'.
    '''
    if section == 'all':
        results = find_needle_in_dict(key, dictionary)
    else:
        results = find_needle_in_dict(key, dictionary[section])

    return ', '.join(results)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
