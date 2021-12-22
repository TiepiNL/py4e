# Requires pywin32
# 1. py -m pip install --upgrade pip
# 2. pip install pywin32 --upgrade
# (https://github.com/mhammond/pywin32/releases)

# options:
#  -h, --help            show this help message and exit
#  -v, --verbose         increase output verbosity for debugging purposes
#  -q, --quiet           don't print any output
#  -a {version,reload,restart,test,config,log,setting}, --action {version,
#     reload,restart,test,config,log,setting}
#                        action to perform
#  -s {all,fileinfo,global,local,logfiles,logwatch,mrpe,plugins,ps,spool,
#     system,winperf}, --section {all,fileinfo,global,local,logfiles,logwatch,
#     mrpe,plugins,ps,spool,system,winperf}
#                        set scope
#  -c {all,default,bakery,user}, --config {all,default,bakery,user}
#                        the config to display. 'All' returns the merged config.
#  -? QUESTION, --question QUESTION
#                        setting to return
#  -e, --byexception     only display warning and critical log messages
#                        (for the log-action).
#  -o, --open            open saved data in a text viewer (supported by the
#                        following actions: test, config, log)
#  -n-o, --no-open       only save data without opening it (supported by the
#                        following actions: test, config, log)

# EXAMPLES
# py checkmk.py --action version
# py checkmk.py -a reload --verbose
# py checkmk.py -a restart
# py checkmk.py -a test
# py checkmk.py -a config --no-open
# py checkmk.py -a config -c user
# py checkmk.py -a log
# py checkmk.py -a log --byexception
# py checkmk.py -a setting -? passphrase
# py checkmk.py -a setting --section global -? encrypted

from os import path
from os import getenv
from os.path import exists
from platform import system
import argparse
import logging as log

from subprocess import check_output
from subprocess import run

try:
    import win32serviceutil as win32_service
except:
    print("can't import win32serviceutil.",
          "Install it with 'pip install pywin32'.")
    quit()


# Wrapper around os.getenv.
def get_envvar(key, required=False):
    val = getenv(key)
    if val is None:
        logtxt = "Failed to retrieve environment variable '{}'.".format(key)
        if required == True:
            log.error(logtxt)
            quit()
        log.info(logtxt)
    return val


def run_command(cmd, return_output=True):
    # @TODO: track and report duration
    try:
        stdout = run(cmd, text=True, capture_output=return_output).stdout
    except Exception as err:
        print("Failed to run command '{}'. {}".format(cmd[0], err))
        quit()

    if return_output:
        return stdout


def read_textfile(file):
    try:
        fhandler = open(file)
    except Exception as err:
        print("Can't open file: '{}'. {}".format(fagentlog, err))
        quit()

    lines = fhandler.readlines()
    fhandler.close()

    return lines


def write_textfile(file, content):
    try:
        fhandler = open(file, "w")
    except Exception as err:
        print("Can't create/open file '{}' for writing. {}".format(
              file, err))
        quit()
    fhandler.write(content)
    fhandler.close()


def get_agent_version():
    result = run_command([check_mk_agent, "version"])

    # The output should look like "Check_MK Agent version 1.6.0p18".
    # Strip the prefix to get the version number.
    pfx = "Check_MK Agent version"
    pos = result.find(pfx)
    if pos == -1:
        log.error("Command output has an unexpected format.")
        quit()

    version = (result[pos + len(pfx):]).strip()
    logtxt = "Successfully retrieved the agent version: '{}'.".format(version)
    log.info(logtxt)
    return version


def reload_agent_config():
    result = run_command([check_mk_agent, "reload_config"])

    # The last line of the output should be "Done."
    if result.strip()[len(result)-5:] != 'Done.':
        log.warning("Something went wrong while reloading the agent config.")
        success = False
    else:
        if prt:
            print("Successfully reloaded the agent configuration.")
        success = True

    return success


def restart_service(service_name):
    try:
        win32_service.RestartService(service_name)
    except Exception as err:
        logtxt = "could not restart the '{}' service:".format(service_name)
        print(logtxt, err)
    logtxt = "Successfully restarted the '{}' service.".format(service_name)
    if prt:
        print(logtxt)


def test_agent(ftestoutput, fopen):
    if prt:
        print("Generating test output - this can take up to one minute.")
    result = run_command([check_mk_agent, "test"])
    # Write the output of the testrun to a text file.
    write_textfile(ftestoutput, result)

    logtxt = ("Test run completed successfully. "
              + "Output is available here: '{}'.".format(ftestoutput))
    if fopen == False:
        if prt:
            print(logtxt)
        return
    log.info(logtxt)

    # Open the test output.
    run_command([viewer, ftestoutput], False)


def match_config(config):
    if system() == "Windows":
        # For the agent configuration three files are read sequentially and
        # hierarchically:
        # 1) The default configuration is stored here.
        check_mk_yml = PROGRAMFILES86 + "\\checkmk\\service\\check_mk.yml"
        # 2) Created by the Agent Bakery, and overrides the default values.
        check_mk_bakery_yml = CUSTOM_AGENT_PATH + "bakery\\check_mk.bakery.yml"
        # 3) For manual customizations. overrides default and Bakery values.
        check_mk_user_yml = CUSTOM_AGENT_PATH + "check_mk.user.yml"

    match config:
        case "default":
            cfg = check_mk_yml
        case "bakery":
            cfg = check_mk_bakery_yml
        case "user":
            cfg = check_mk_user_yml
        case _:
            cfg = "all"
    return cfg


def get_agent_config(fconfigoutput, section, config, fopen):
    yml = match_config(config)

    # Rename the destination file. Use the same filepath, but with an extra
    # suffix based on the used config file (all, default, bakery, or user).
    fconfigoutput = "{}_{}{}".format(fconfigoutput[:len(fconfigoutput)-4],
                                     config, fconfigoutput[len(fconfigoutput)-4:])

    if yml == "all":
        # Section "all" is non-existing and only used for parameter validation.
        if section == "all":
            cmd = [check_mk_agent, "showconfig"]
        else:
            cmd = [check_mk_agent, "showconfig", section]
        result = run_command(cmd)
        # Write the running config to a text file.
        write_textfile(fconfigoutput, result)
        fconfig = fconfigoutput

    else:
        # Use one of the yaml config files as input, instead of the just
        # exported (merged) runnig config.
        fconfig = yml

    lines = read_textfile(fconfig)

    cfg = []
    skip = False
    for line in lines:
        # Remove empty lines and comment lines.
        if len(line.strip()) == 0:
            continue
        if line.lstrip().startswith("#"):
            continue

        # The merged config ("all") as retrieved via the 'showconfig' command
        # has all example code filtered out. The separate yaml file can have
        # example code, which starts with an underscore.
        # Filter out all lines that start with '_', and all subsequent lines
        # if the have a larger indentation (subkeys).
        if yml != "all":
            if skip == True:
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
    write_textfile(fconfigoutput, cfg)

    logtxt = ("Successfully exported the agent configuration. "
              + "Output is available here: '{}'.".format(fconfigoutput))
    if fopen == False:
        if prt:
            print(logtxt)
        return
    log.info(logtxt)

    # Open the config output.
    run_command([viewer, fconfigoutput], False)


def open_agent_log(fagentlog, byexception, fopen):
    if byexception == True:
        lines = read_textfile(fagentlog)

        events = []
        for line in lines:
            # Filter the agent log to create an exception log with warnings and
            # errors only.
            if line.find("[Err") == -1 and line.find("[Warn") == -1:
                continue
            # Remove the linebreak at the end of each line.
            events.append(line.rstrip())

        if len(events) == 0:
            print("No warning/error events detected in the current log.")
            quit()
        log.info("{} warning/error events detected in the current log.".format(
                 len(events)))

        separator = '\n'
        events = separator.join(events)

        # Export the stripped log to a new file. Use the same filepath as the
        # agent logfile, with an extra suffix.
        fagentlog = "{}_exceptions{}".format(fagentlog[:len(fagentlog)-4],
                                             fagentlog[len(fagentlog)-4:])
        write_textfile(fagentlog, events)

    logtxt = ("Successfully exported the exceptions from the agent log. "
              + "Output is available here: '{}'.".format(fagentlog))
    if fopen == False:
        if prt:
            print(logtxt)
        return
    log.info(logtxt)

    run_command([viewer, fagentlog], False)


def get_setting(fconfigoutput, config, section, question):
    # Create the scoped output, without opening it.
    get_agent_config(fconfigoutput, section, config, False)
    # Retrieve the source file, based on the used config file
    # (all, default, bakery, or user).
    yml = match_config(config)
    fconfigoutput = "{}_{}{}".format(fconfigoutput[:len(fconfigoutput)-4],
                                     config, fconfigoutput[len(fconfigoutput)-4:])
    lines = read_textfile(fconfigoutput)

    for line in lines:
        if line.lstrip().startswith("{}:".format(question)):
            pos = line.find(":")
            result = line[pos+1:].strip()
            log.info("Lookup succeeded: key '{}' has the value '{}'.".format(
                     question, result))
            return result
    log.info("Lookup failed: can't find key '{}'.".format(question))


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity for "
                    + "debugging purposes",
                    action="store_true")
parser.add_argument("-q", "--quiet", help="don't print any output",
                    action="store_true")
parser.add_argument("-a", "--action", choices=["version", "reload", "restart",
                    "test", "config", "log", "setting"],
                    help="action to perform")
parser.add_argument("-s", "--section", choices=["all", "fileinfo", "global",
                    "local", "logfiles", "logwatch", "mrpe", "plugins", "ps",
                                                "spool", "system", "winperf"], help="set scope")
parser.add_argument("-c", "--config", choices=["all", "default", "bakery",
                    "user"], help="the config to display. 'All' returns the "
                    + "merged config.")
parser.add_argument("-?", "--question", help="setting to return")
parser.add_argument("-e", "--byexception", help="only display warning and "
                    + "critical log messages (for the log-action).",
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

# Print output?
if args.quiet:
    prt = False
else:
    prt = True

if system() == "Windows":
    PROGRAMDATA = get_envvar("PROGRAMDATA", True)
    PROGRAMFILES86 = get_envvar("ProgramFiles(x86)", True)
    CUSTOM_AGENT_PATH = PROGRAMDATA + "\\checkmk\\agent\\"
    check_mk_agent = PROGRAMFILES86 + "\\checkmk\\service\\check_mk_agent.exe"
    fagentlog = CUSTOM_AGENT_PATH + "log\\check_mk.log"
    ftestoutput = CUSTOM_AGENT_PATH + "log\\testrun.txt"
    fconfigoutput = CUSTOM_AGENT_PATH + "log\\config.txt"
    viewer = "notepad.exe"
elif system() == "Linux":
    # @TODO: Linux paths
    pass
else:
    log.error("Unsupported system:", system())
    quit()

CUSTOM_PLUGINS_PATH = CUSTOM_AGENT_PATH + "plugins"
CUSTOM_LOCAL_PATH = CUSTOM_AGENT_PATH + "local"

fexists = exists(check_mk_agent)
if fexists == False:
    log.error("checkmk agent not found!")
    quit()

if args.action == 'version':
    print(get_agent_version())
elif args.action == "reload":
    reload_agent_config()
elif args.action == "restart":
    # Note: Service restart requires an elevated session.
    restart_service("CheckMkService")
elif args.action == "test":
    test_agent(ftestoutput, args.open)
elif args.action == "config":
    get_agent_config(fconfigoutput, args.section, args.config, args.open)
elif args.action == "log":
    open_agent_log(fagentlog, args.byexception, args.open)
elif args.action == "setting":
    print(get_setting(fconfigoutput, args.config, args.section, args.question))
