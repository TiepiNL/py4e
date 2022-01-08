"""
Managing and troubleshooting the checkmk agent.
"""
import argparse
import logging as log
import sys

from classes import Agent
import processors as proc

def validate_args(args):
    ''' (list) -> NoneType

    Validate argument combinations.
    '''
    # A question cannot be combined with a action other than 'config'.
    if args.question and args.action != 'config':
        logtxt = ("The --question parameter (or its alias -?) cannot be combined with "
                 + "an action other than 'config'.")
        log.error(logtxt)
        sys.exit(1)
    # 'write' can only be combined with the actions 'log', 'config', 'test'.
    if args.write and args.action not in ['log', 'config', 'test']:
        logtxt = ("The --write parameter (or its alias -w) cannot be combined with "
                 + "an action other than 'log', 'config' or 'test'.")
        log.error(logtxt)
        sys.exit(1)


if __name__ == '__main__':

    if proc.is_admin() == 0:
        log.error('This program requires admin rights in an elevated session.')
        sys.exit(1)


    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity for '
                        + 'debugging purposes', action='store_true')
    parser.add_argument('action', choices=['version', 'config', 'log', 'test',
                        'restart', 'reload'], help='action to perform')
    parser.add_argument('-t', '--type', choices=['running', 'default', 'bakery',
                        'user'], help='the config type to display.')
    parser.add_argument('-s', '--section', choices=['all', 'fileinfo', 'global',
                        'local', 'logfiles', 'logwatch', 'mrpe', 'plugins', 'ps',
                        'spool', 'system', 'winperf'], help='set config scope')
    parser.add_argument('-f', '--format', choices=['yml', 'dict', 'json'],
                        help='the output format of the config.')
    parser.add_argument('-?', '--question', help='setting to return '
                        + '(only applicable to the setting-actions)')
    parser.add_argument("-w", "--write", help="save output as file via a "
                    + " save-as dialog (supported by the following actions: "
                    + "test, config, log)", action="store_true")
    parser.set_defaults(type='running', section='all', format='yml', write=False)
    args = parser.parse_args()

    # Check for invalid argument combinations.
    validate_args(args)

    if args.verbose:
        log.basicConfig(format='%(levelname)s: %(message)s', level=log.DEBUG)
        log.info('Verbose output enabled.')
    else:
        log.basicConfig(format='%(levelname)s: %(message)s')


    if args.action == 'test':
        TEST = True
        print('Generating test output - this can take up to one minute.')
    else:
        TEST = False

    agent = Agent(test=TEST)

    # Defaults
    result = 'No action performed.'
    file_name = args.action
    file_ext = args.format

    match args.action:
        case 'version':
            result = agent.version
        case 'config':
            match args.type:
                case 'running':
                    dictionary = agent.config
                case 'default':
                    dictionary = agent.config_default
                    file_name = 'config_default'
                case 'bakery':
                    dictionary = agent.config_bakery
                    file_name = 'config_bakery'
                case 'user':
                    dictionary = agent.config_user
                    file_name = 'config_user'
            if args.question:
                result = proc.get_setting(args.question, dictionary, args.section)
            else:
                if args.section != 'all':
                    dictionary = dictionary[args.section]
                match args.format:
                    # The search is always performand against the dict format.
                    # Convert it to the requested format, if necessary.
                    case 'yml':
                        result = proc.dict2yaml(dictionary)
                    case 'dict':
                        result = dictionary
                    case 'json':
                        result = proc.dict2json(dictionary)
        case 'log':
            result = ''.join(agent.log)
            file_name = 'agent'
            file_ext = 'log'
        case 'test':
            result = agent.test
            file_ext = 'txt'
        case 'restart':
            result = proc.restart_service('CheckMkService')
        case 'restart':
            result = proc.reload_agent_config()

    print(result)
    if args.write:
        filepath = f"{file_name}.{file_ext}"
        proc.save(filepath, result, ext=file_ext)
