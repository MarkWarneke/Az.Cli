# Az.Cli

Python [azure.cli.core](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/__init__.py) interface to execute `az` [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) commands in python.

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

# AzResult = namedtuple('AzResult', ['exit_code', 'out', 'log'])
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
Import the library `from az.cli import az` and run  any command by executing the method `az("<my command>")` to invoke Azure CLI.

```python
# cd src
# python3
from az.cli import az
az("group list") # list return tuple (exitCode, resultSet)
az("group list")[1] # return resultSet content <dict>
az("group list")[1][0]['id'] # Enumerate id of first element in resultSet

# On Error
az("group show -n does-not-exsist") # list return tuple (exitCode, resultSet)
az("group show -n does-not-exsist")[0] # 3
az("group show -n does-not-exsist")[2] # Print the logs
```

## Build

To build the image run the following in order.

```bash
# Runs docker build & create
make create
```

## Run

After the container is build & created you can run the `az.cli` interactivly. 

```bash
# Run docker run
make run
```

see [interactive](#interactive)

## Local Development

- install [python3](https://www.python.org/downloads/)
- install `REQUIREMENTS.txt

I recommend to use [Python3 virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv).

```bash
python3 -m venv env
source env/bin/activate
make init
```

## Known Bugs

- `az('login')` https://github.com/MarkWarneke/Az.Cli/issues/1
