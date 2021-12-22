# checkmk agent companion
**[checkmk]** is an open source infrastructure monitoring tool. 

This program contains features to troubleshoot the [checkmk agent for Windows]. Linux support will be added later.

## Features

## Requirements

@TODO: Python version

On Windows systems, this program requires pywin32. Install it via pip:
```
pip install pywin32 --upgrade
```
or alternatively, get [pywin32] from GitHub. 

## Usage

### Flags
When calling `checkmk.py`, the following flags are available:

- `--help` aliased with `-h`
  - Displays... @TODO
- `--verbose` aliased with `-v`
- `--quiet` aliased with `-q`
- `--action` aliased with `-a`
- `--config` aliased with `-c`
- `--section` aliased with `-s`
- `--question` aliased with `-?`
- `--byexception` aliased with `-e`

### Examples

py checkmk.py --help
py checkmk.py --action version
py checkmk.py -a reload --verbose
py checkmk.py -a restart
py checkmk.py -a test
py checkmk.py -a config --no-open
py checkmk.py -a config -c user
py checkmk.py -a log
py checkmk.py -a log --byexception
py checkmk.py -a setting -? passphrase
py checkmk.py -a setting --section global -? encrypted


[checkmk]:                      https://checkmk.com/
[checkmk agent for Windows]:    https://docs.checkmk.com/latest/en/agent_windows.html
[pywin32]:                      https://github.com/mhammond/pywin32/releases
