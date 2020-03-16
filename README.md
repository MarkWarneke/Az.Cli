# Az.Cli

[![PyPi](https://img.shields.io/pypi/pyversions/az.cli)](https://pypi.python.org/pypi/az.cli)
[![Build Status master](https://github.com/MarkWarneke/Az.Cli/workflows/Build/badge.svg?branch=master)](https://github.com/MarkWarneke/Az.Cli/actions?query=workflow%3ABuild)
[![Build Status dev](https://github.com/MarkWarneke/Az.Cli/workflows/Build/badge.svg?branch=dev)](https://github.com/MarkWarneke/Az.Cli/actions?query=workflow%3ABuild)

Python [azure.cli.core](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/__init__.py) interface to execute `az` [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) commands in python.

The method returns a named tuple `AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])`. The [`error_code`](https://docs.python.org/2/library/sys.html#sys.exit) where 0 == success. A `result_dict` containing successfull return as a python dictionary. On failure (`error_code` > 0) a log message inside `log` as a string.

## Usage

Install the package

```bash
pip install az.cli
```

Login using `az login`, see [sign in using a service principal](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principalt).

Under the hood the package uses the [~/.azure](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/_environment.py) folder to persist and retrieve config.

## Example

```python
from az.cli import az

# AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
exit_code, result_dict, logs = az("group show -n test")

# On 0 (SUCCESS) print result_dict, otherwise get info from `logs`
if exit_code == 0:
    print (result_dict)
else:
    print(logs)
```

## Interactive

You can run the command interactively to traverse the dictionary.
Navigate to `src` and run `python3`.
Import the library `from az.cli import az` and run any command by executing the method `az("<my command>")` to invoke Azure CLI.

```python
# cd src
# python3
from az.cli import az
# on Success, the `error_code` is 0 and the result_dict contains the output
az("group list") # list return tuple (exit_code, result_dict, log)
az("group list")[0] # 0
az("group list")[1] # print result_dict
az("group list")[1][0]['id'] # enumerate the id of the first element in dictionary

# On Error, the `error_code` will be != 1 and the log is present
az("group show -n does-not-exsist") # list return tuple (exit_code, result_dict, log)
az("group show -n does-not-exsist")[0] # 3
az("group show -n does-not-exsist")[2] # print the log
```

## Build

### Local Development

- install [python3](https://www.python.org/downloads/)
- install `REQUIREMENTS.txt` using `make init`

I recommend to use [Python3 virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv).

```bash
# sets up environment
make env
# installs requirements
make init
```

### Docker

To build the image run the following in order.

```bash
# Runs docker build & create
make create
```

#### Run

After the container is build & created you can run the `az.cli` interactivly.

```bash
# Run docker run
make run
```

## Known Bugs

- `az('login')` https://github.com/MarkWarneke/Az.Cli/issues/1
