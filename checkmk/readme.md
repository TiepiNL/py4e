# checkmk agent companion
This program eases the life of sysadmins by providing features to troubleshoot the [checkmk agent for Windows]. Linux support will be added later. (**[checkmk]** is an open source infrastructure monitoring tool.)

image_placeholder

## Features

- Get the agent version
- Reload the agent configuration
- Restart the checkmk agent service
- Show the output of an agent test
- Open the agent log file
- Filter the agent log on errors/warnings
- Show the running agent config
- Show the stored configs (default, bakery, or user)
- Lookup the value of a specific config setting

## Requirements

### Python version

checmk.py is written in Python 3. Currently 3.10 is the only tested version.

### pywin32

On Windows systems, this program requires pywin32.

<details><summary><b>Show instructions</b></summary>

Install it via pip:
```
pip install pywin32 --upgrade
```
or alternatively, get [pywin32] from GitHub.

</details>

## Usage

```
checkmk.py [-h] [-v] [-q] [-a {version,reload,restart,test,config,log,setting}]
           [-s {all,fileinfo,global,local,logfiles,logwatch,mrpe,plugins,ps,spool,system,winperf}]
           [-c {all,default,bakery,user}] [-? QUESTION] [-e] [-o] [-n-o]
```

### Options
When calling `checkmk.py`, the following flags are available:

- `-h, --help`
  - show the help message and exit
- `-v, --verbose`
  - increase output verbosity for debugging purposes
- `-q, --quiet`
  - don't print any output
- `-a, --action {version,reload,restart,test,config,log,setting}`
  - action to perform: the main features of the program
- `-c, --config {all,default,bakery,user}`
  - the config to display. 'all' returns the (merged) running config
- `-s, --section {all,fileinfo,global,local,logfiles,logwatch,mrpe,plugins,ps,spool,system,winperf}`
  - set scope
- `-?, --question QUESTION`
  - setting to return (only applicable to the setting-action)
- `-e,  --byexception`
  - only display warning and critical log messages (only applicable to the log-action)              
- `-o, --open`
  - open saved data in a text viewer (supported by the following actions: test, config, log)
  - defaults to True, which can be overwritten with the 'no-open' flag
- `-n-o, --no-open`
  - only save data without opening it (supported by the following actions: test, config, log)
  - used to overwrite the 'open' flag

### Examples

```
py checkmk.py --action version
```
The version-action executes the `check_mk_agent.exe version` command.
It retrieves the version number from the returned output. For example,
the output "Check_MK Agent version 1.6.0p18" becomes "1.6.0p18".

```
py checkmk.py -a reload
```
The reload-action executes the `check_mk_agent.exe reload_config` command.

```
py checkmk.py -a restart
```
Restarts the 'Check Mk Service'.

```
py checkmk.py -a test --verbose
```

```
py checkmk.py -a config --no-open
```

```
py checkmk.py -a config -c user
```

```
py checkmk.py -a log
```

```
py checkmk.py -a log --byexception
```

```
py checkmk.py -a setting -? passphrase
```

```
py checkmk.py -a setting --section global -? encrypted
```

[checkmk]:                      https://checkmk.com/
[checkmk agent for Windows]:    https://docs.checkmk.com/latest/en/agent_windows.html
[pywin32]:                      https://github.com/mhammond/pywin32/releases
