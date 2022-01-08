from shlex import quote

import processors as proc

class Agent:
    '''
    '''
    #pylint: disable-next=dangerous-default-value
    def __init__(self, version='unknown',
                 test=False,
                 config='',
                 config_default='',
                 config_bakery='',
                 config_user='',
                 log=''
                 ):
        self.version = version
        self.test = test
        self.config = config
        self.config_default = config_default
        self.config_bakery = config_bakery
        self.config_user = config_user
        self.log = log


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, default):
        ''' (self) -> str

        Sets the Check_MK Agent version, e.g. '1.6.0p18'.
        '''
        exe = proc.get_agent_exe()
        cmd = f'{quote(exe)} version'
        stdout = proc.run_command(cmd)
        # The output should look like "Check_MK Agent version 1.6.0p18".
        pfx = 'Check_MK Agent version'
        pos = stdout.find(pfx)
        if pos == -1:
            self._version = default
        else:
            # The part that comes after the prefix is the version.
            self._version = (stdout[pos + len(pfx):]).strip()


    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, retrieve):
        ''' (self) -> str

        Sets the agent test output.
        '''
        if retrieve:
            exe = proc.get_agent_exe()
            cmd = f'{quote(exe)} test'
            output = proc.run_command(cmd, 60)
            self._test = output
        else:
            self._test = 'no results yet'


    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, default):
        ''' (self) -> dict

        Sets the running agent config (yaml) as dict.
        '''
        exe = proc.get_agent_exe()
        cmd = f'{quote(exe)} showconfig'
        yml = proc.run_command(cmd)
        self._config = proc.yaml2dict(yml)


    @property
    def config_default(self):
        return self._config_default

    @config_default.setter
    def config_default(self, default):
        ''' (self) -> dict

        Sets the default agent config ("cleaned" yaml) as dict.
        '''
        yml = proc.get_agent_config('default')
        self._config_default = proc.yaml2dict(yml)


    @property
    def config_bakery(self):
        return self._config_default

    @config_bakery.setter
    def config_bakery(self, default):
        ''' (self) -> dict

        Sets the default agent config ("cleaned" yaml) as dict.
        '''
        yml = proc.get_agent_config('bakery')
        self._config_bakery = proc.yaml2dict(yml)


    @property
    def config_user(self):
        return self._config_user

    @config_user.setter
    def config_user(self, default):
        ''' (self) -> dict

        Sets the default agent config ("cleaned" yaml) as dict.
        '''
        yml = proc.get_agent_config('user')
        self._config_user = proc.yaml2dict(yml)


    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, default):
        ''' (self) -> list

        Sets a "by exception" list with warning/error log entries.
        '''
        log_file = proc.get_agent_log()
        events = proc.read_textfile(log_file)
        proc.filter_list(events, r'.+\[(Warn|Err).+')
        # Add an item to the list with the (unique) sections without data.
        empty_sections = proc.get_empty_agent_sections(events)
        if len(empty_sections) > 0:
            empty_sections = f"empty sections: {', '.join(empty_sections)}"
            events.append(empty_sections)

        self._log = events
