"""
Features for troubleshooting the checkmk agent
"""

import argparse
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
import win32api

# pywin32 is (only) required on Windows systems.
if system() == "Windows":
    try:
        import win32serviceutil as win32_service
    except ModuleNotFoundError as error:
        print(f"Can't import win32serviceutil: {error}.",
              "Install it with 'pip install pywin32'.")
        sys.exit(1)


def get_envvar(key, required=False):
    """
    Wrapper around os.getenv with traceback handling.
    :param key: environment variable to lookup.
    :param required: throw an error and quit if the key doesn't exist.
    :return: environment variable (str)
    """
    val = getenv(key)
    if val is None:
        logtxt = f"Failed to retrieve environment variable '{key}'."
        if required:
            log.error(logtxt)
            sys.exit(1)
        log.info(logtxt)
    return val


def add_filename_suffix(filename, suffix, before_ext=True, separator="_"):
    """
    Extend a filename with a suffix. The suffix can be placed before
    the last dot in the filename, or truly at the end of the filename.
    :param filename: the filename to alter.
    :param suffix: string to add at the end of the filename.
    :before_ext: whether the suffix should be placed before or after the file extension (if any).
    :separator: prefix for the suffix :)
    :return: altered filename (Str)
    """
    if filename.find(".") != -1 and before_ext:
        pieces = filename.split(".")
        ext = pieces[len(pieces)-1]
        name = ''.join(pieces[:len(pieces)-1])
        new_filename = f"{name}{separator}{suffix}.{ext}"
    else:
        new_filename = f"{filename}{separator}{suffix}"

    logtxt = f"Converted filename '{filename}' to '{new_filename}'."
    log.info(logtxt)

    return new_filename


def run_command_async(command_line):
    """
    Execute a shell command asynchronously.
    :param command_line: shell command to execute.
    :return: N/A
    """
    # Break the shell command into a sequence of arguments.
    cmd_args = split(command_line)
    try:
        subprocess.Popen(cmd_args)
    except OSError as err:
        logtxt = f"Failed to open program '{cmd_args[0]}'. {err}."
        print(logtxt)
        sys.exit(1)


def run_command(command_line, timeout_sec=10):
    """
    Execute a shell command synchronously and capture the output.
    :param command_line: shell command to execute.
    :param timeout: timeout in seconds. If the timeout expires, the
    child process will be killed and waited for.
    :return: command output (str)
    @TODO: track and (verbose) report duration
    """
    # Break the shell command into a sequence of arguments.
    cmd_args = split(command_line)
    try:
        result = subprocess.run(
            cmd_args, text=True, capture_output=True, check=True, timeout=timeout_sec)
    except OSError as err:
        logtxt = f"Failed to run command '{cmd_args[0]}'. {err}."
        print(logtxt)
        sys.exit(1)
    except subprocess.TimeoutExpired as err:
        logtxt = (
            f"Execution of command '{cmd_args}' exceeded the timeout value of {timeout_sec}s. "
            f"{err}."
        )
        print(logtxt)
        sys.exit(1)
    except subprocess.CalledProcessError as err:
        logtxt = f"Command '{cmd_args}' returned a non-zero exit status. {err}."
        print(logtxt)
        sys.exit(1)

    return result.stdout


def read_textfile(file):
    """
    Open a text file and return the content.
    :param file: the file to read.
    :return: all lines in the file (list)
    """
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode="r", encoding="utf-8") as fopen:
            lines = fopen.readlines()
    except OSError as err:
        logtxt = f"Can't open file: '{file}'. {err}."
        print(logtxt)
        sys.exit(1)

    return lines


def write_textfile(file, content):
    """
    Open a text file and (over)write content to it.
    :param file: the file to write to.
    :param content: the content to write to the file.
    :return: N/A
    """
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode="w", encoding="utf-8") as fopen:
            fopen.write(content)
    except OSError as err:
        logtxt = f"Can't create/open file '{file}' for writing. {err}."
        print(logtxt)
        sys.exit(1)


def get_agent_version():
    """
    Retrieve the Check_MK Agent version.
    :return: agent version (str) - e.g. '1.6.0p18'
    """
    cmd = f"{quote(CHECK_MK_AGENT)} version"
    result = run_command(cmd)
    # The output should look like "Check_MK Agent version 1.6.0p18".
    # Strip the prefix to get the version number.
    pfx = "Check_MK Agent version"
    pos = result.find(pfx)
    if pos == -1:
        log.error("Command output has an unexpected format.")
        sys.exit(1)

    version = (result[pos + len(pfx):]).strip()
    logtxt = f"Successfully retrieved the agent version: '{version}'."
    log.info(logtxt)
    return version


def reload_agent_config():
    """
    Reload the Check MK Agent configuration.
    :return: success (bool)
    """
    cmd = f"{quote(CHECK_MK_AGENT)} reload_config"
    result = run_command(cmd)

    # The last line of the output should be "Done."
    if result.strip()[len(result)-5:] != 'Done.':
        log.warning("Something went wrong while reloading the agent config.")
        return FAILURE
    else:
        logtxt = "Successfully reloaded the agent configuration."
        if PRT:
            print(logtxt)
        else:
            log.info(logtxt)
        return SUCCESS


def restart_service(service_name):
    """
    Restart the Check MK Agent service.
    :param service_name: the service name (not the display name!) to restart.
    :return: success/failure (bool)
    """
    try:
        win32_service.RestartService(service_name)
    except win32api.error as err:
        logtxt = f"could not restart the '{service_name}' service. {err}."
        print(logtxt)
        return FAILURE
    logtxt = f"Successfully restarted the '{service_name}' service."
    if PRT:
        print(logtxt)
    else:
        log.info(logtxt)
    return SUCCESS


def test_agent(output_file, viewfile):
    """
    Restart the Check MK Agent service.
    :param output_file: the file to write the test results to.
    :param viewfile: the viewer (e.g. notepad.exe) to open the file.
    :return: N/A
    """
    if PRT:
        print("Generating test output - this can take up to one minute.")
    cmd = f"{quote(CHECK_MK_AGENT)} test"
    result = run_command(cmd, 60)
    # Write the output of the testrun to a text file.
    write_textfile(output_file, result)

    logtxt = f"Test run completed successfully. Output is available here: '{output_file}'."
    if not viewfile:
        if PRT:
            print(logtxt)
        return
    log.info(logtxt)

    # Open the test output.
    cmd = f"{quote(VIEWER)} {quote(output_file)}"
    run_command_async(cmd)


def get_config_path(config_type):
    """
    Get the path of the matching config type file.
    :param config_type: the config type (default, bakery, or user).
    :return: filepath (str)
    """
    if system() == "Windows":
        # For the agent configuration three files are read sequentially and
        # hierarchically:
        # 1) The default configuration is stored here.
        check_mk_yml = f"{PROGRAMFILES86}\\checkmk\\service\\check_mk.yml"
        # 2) Created by the Agent Bakery, and overrides the default values.
        check_mk_bakery_yml = f"{CUSTOM_AGENT_PATH}\\bakery\\check_mk.bakery.yml"
        # 3) For manual customizations. overrides default and Bakery values.
        check_mk_user_yml = f"{CUSTOM_AGENT_PATH}\\check_mk.user.yml"

    match config_type:
        case "default":
            cfg = check_mk_yml
        case "bakery":
            cfg = check_mk_bakery_yml
        case "user":
            cfg = check_mk_user_yml
        case _:
            cfg = "all"
    return cfg


def get_agent_config(output_file, section, config_type, viewfile):
    """
    Get the path of the matching config type file.
    :param output_file: the file to write the retrieved config to.
    :section: config scope.
    :config_type: the config type (all, default, bakery, or user).
    :viewfile: whether the generated output file should be opened.
    :return: N/A
    """
    # Rename the destination file. Use the same filepath, but with an extra
    # suffix based on the used config file (all, default, bakery, or user).
    output_file = add_filename_suffix(output_file, config_type)

    yml = get_config_path(config_type)
    if yml == "all":
        # Section "all" is non-existing and only used for parameter validation.
        if section == "all":
            cmd = f"{quote(CHECK_MK_AGENT)} showconfig"
        else:
            cmd = f"{quote(CHECK_MK_AGENT)} showconfig {section}"
        result = run_command(cmd)
        # Write the running config to a text file.
        write_textfile(output_file, result)
        fconfig = output_file
    else:
        # Use one of the yaml config files as input, instead of the just
        # exported (merged) runnig config.
        fconfig = yml

    lines = read_textfile(fconfig)

    # Comment lines are removed from the output. The exception is the
    # informational header of the running config, which contains Environment
    # Variables and the loaded config files.
    if yml == "all" and section == "all":
        info_header = True
    else:
        info_header = False
    skip = False
    cfg = []
    for line in lines:
        # Remove empty lines and comment lines.
        if len(line.strip()) == 0:
            # The first whiteline indicates the end of the informational header.
            # From this point onwards all comment lines will be skipped.
            if info_header:
                info_header = False
            continue
        if line.lstrip().startswith("#"):
            # Skip all comment lines, except the informational header.
            if not info_header:
                continue

        # The merged config ("all") as retrieved via the 'showconfig' command
        # has all example code filtered out. The separate yaml file can have
        # example code, which starts with an underscore.
        # Filter out all lines that start with '_', and all subsequent lines
        # if the have a larger indentation (subkeys).
        if yml != "all":
            if skip:
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
                    skip = False

            if line.lstrip().startswith("_"):
                # Get the indentation aka the amount of prefixed spaces.
                pos = line.find('_')
                spaces = len(line[:pos])
                # Make sure the identation of the next line gets examined.
                skip = True
                continue

            # Strip in-line comments.
            pos = line.find('#')
            if pos != -1:
                line = line[:pos]

        cfg.append(line.rstrip())

    separator = '\n'
    cfg = separator.join(cfg)

    # Overwrite the exported config with the stripped config.
    write_textfile(output_file, cfg)

    logtxt = (
        f"Successfully exported the agent configuration. "
        f"Output is available here: '{output_file}'."
    )
    if not viewfile:
        if PRT:
            print(logtxt)
        return
    log.info(logtxt)

    # Open the config output.
    cmd = f"{quote(VIEWER)} {quote(output_file)}"
    run_command_async(cmd)


def open_agent_log(log_file, byexception, viewfile):
    """
    Open the agent log file.
    :param log_file: the log filepath to read.
    :byexception: filter the log to only display errors/warnings.
    :viewfile: whether the generated output file should be opened.
    :return: N/A
    """
    if byexception:
        lines = read_textfile(log_file)

        events = list()
        empty_sections = list()
        for line in lines:
            # Filter the agent log to create an exception log with warnings and
            # errors only.
            if line.find("[Err") == -1 and line.find("[Warn") == -1:
                continue
            # Check for potentially unused agent sections.
            pattern = re.compile("Section '[a-z_]*' cannot provide data")
            if pattern.search(line):
                # Only interested in unique section names.
                section = line.split("'")[1]
                if section not in empty_sections:
                    empty_sections.append(section)
            # Remove the linebreak at the end of each line.
            events.append(line.rstrip())

        if len(events) == 0:
            print("No warning/error events detected in the current log.")
            sys.exit(0)
        logtxt = f"{len(events)} warning/error events detected in the current log."
        log.info(logtxt)

        if len(empty_sections) > 0:
            separator = ', '
            empty_sections = separator.join(empty_sections)
            logtxt = (
                f"The following agent sections cannot provide any data: "
                f"'{empty_sections}'. Disabling these sections - if unused - "
                f"will drastically reduce the amount of warning messages in the agent log."
            )
            if PRT:
                print(logtxt)
            else:
                log.info(logtxt)

        separator = '\n'
        events = separator.join(events)

        # Export the stripped log to a new file. Use the same filepath as the
        # agent logfile, with an extra suffix.
        log_file = add_filename_suffix(log_file, "exceptions")
        write_textfile(log_file, events)

    logtxt = (
        f"Successfully exported the exceptions from the agent log. "
        f"Output is available here: '{log_file}'."
    )
    if not viewfile:
        if PRT:
            print(logtxt)
        return
    log.info(logtxt)

    cmd = f"{quote(VIEWER)} {quote(log_file)}"
    run_command_async(cmd)


def get_setting(output_file, config_type, section, key):
    """
    Retrieve the value of a specific configuration setting.
    :param output_file: the file to write the retrieved config to.
    :config_type: the config type (all, default, bakery, or user).
    :section: config scope.
    :key: the config setting to lookup.
    :return: value (str)
    """
    # Create the scoped output, without opening it.
    get_agent_config(output_file, section, config_type, False)
    output_file = add_filename_suffix(output_file, config_type)

    lines = read_textfile(output_file)
    for line in lines:
        if line.lstrip().startswith(f"{key}:"):
            pos = line.find(":")
            result = line[pos+1:].strip()
            logtxt = f"Lookup succeeded: key '{key}' has the value '{result}'."
            log.info(logtxt)
            return result
    logtxt = f"Lookup failed: can't find key '{key}'."
    log.info(logtxt)


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity for "
                    + "debugging purposes",
                    action="store_true")
parser.add_argument("-q", "--quiet", help="don't print any output",
                    action="store_true")
parser.add_argument("action", choices=["version", "reload", "restart",
                    "test", "config", "log"], help="action to perform")
parser.add_argument("-c", "--config", choices=["all", "default", "bakery",
                    "user"], help="the config to display. 'all' returns the "
                    + "(merged) runnig config")
parser.add_argument("-s", "--section", choices=["all", "fileinfo", "global",
                    "local", "logfiles", "logwatch", "mrpe", "plugins", "ps",
                                                "spool", "system", "winperf"],
                    help="set config scope")
parser.add_argument("-?", "--question", help="setting to return "
                    + " (only applicable to the setting-action)")
parser.add_argument("-e", "--byexception", help="only display warning and "
                    + "critical log messages (for the log-action)",
                    action="store_true")
parser.add_argument("-o", "--open", dest="open", help="open saved data in "
                    + " a text viewer (supported by the following actions: "
                    + "test, config, log)", action="store_true")
parser.add_argument("-n-o", "--no-open", dest="open", help="only save data "
                    + " without opening it (supported by the following "
                    + "actions: test, config, log)", action="store_false")
parser.set_defaults(section="all", config="all", open=True)
args = parser.parse_args()

if args.verbose:
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output enabled.")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")

action = args.action
# Validate argument combinations.
# A question cannot be combined with a action other than 'config'.
if args.question and action != "config":
    logmsg = ("The --question parameter (or its alias -?) cannot be combined with "
             + "an action other than 'config'.")
    log.error(logmsg)
    sys.exit(1)

# Section based scoping only works on the running config ("all").
if args.section != "all" and args.config != "all":
    logmsg = "Cannot combine a section scope with a configuration scope (other than 'all')."
    log.error(logmsg)
    sys.exit(1)

# Log events "by Exception" cannot be combined with a action other than 'log'.
if args.byexception and action != "log":
    logmsg = ("The --byexception parameter (or its alias -e) cannot be combined with "
             + "an action other than 'log'.")
    log.error(logmsg)
    sys.exit(1)

# Don't print feedback if the quiet switch is set, or if a single
# setting ("question") is returned.
if args.quiet or args.question:
    PRT = False
else:
    PRT = True

FAILURE = False
SUCCESS = True

if system() == "Windows":
    PROGRAMDATA = get_envvar("PROGRAMDATA", True)
    PROGRAMFILES86 = get_envvar("ProgramFiles(x86)", True)
    CUSTOM_AGENT_PATH = f"{PROGRAMDATA}\\checkmk\\agent"
    CHECK_MK_AGENT = f"{PROGRAMFILES86}\\checkmk\\service\\check_mk_agent.exe"
    FAGENTLOG = f"{CUSTOM_AGENT_PATH}\\log\\check_mk.log"
    FTESTOUTPUT = f"{CUSTOM_AGENT_PATH}\\log\\testrun.txt"
    FCONFIGOUTPUT = f"{CUSTOM_AGENT_PATH}\\log\\config.txt"
    VIEWER = "notepad.exe"
elif system() == "Linux":
    # @TODO: Linux paths
    pass
else:
    logmsg = f"Unsupported system: {system()}"
    log.error(logmsg)
    sys.exit(1)

FEXISTS = exists(CHECK_MK_AGENT)
if not FEXISTS:
    log.error("checkmk agent not found!")
    sys.exit(1)

if action == 'version':
    print(get_agent_version())
elif action == "reload":
    reload_agent_config()
elif action == "restart":
    # Note: Service restart requires an elevated session.
    restart_service("CheckMkService")
elif action == "test":
    test_agent(FTESTOUTPUT, args.open)
elif action == "config":
    if args.question:
        print(get_setting(FCONFIGOUTPUT, args.config, args.section, args.question))
    else:
        get_agent_config(FCONFIGOUTPUT, args.section, args.config, args.open)
elif action == "log":
    open_agent_log(FAGENTLOG, args.byexception, args.open)
