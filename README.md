# Az.Cli

Python [azure.cli.core](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/__init__.py) interface to execute `az` [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) commands in python.

## Prerequisites

- install [python3](https://www.python.org/downloads/)
- install `REQUIREMENTS.txt` use `make init`
- login to azure using `az login` (this can also be done interactively using the library) see [Sign in using a service principal](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principalt)
- run `python3 src`

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

### Interactive

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

### Run

```bash
make run

```

see [interactive](#interactive)

### Local Development

To develop locally make sure to install Python3.
I recommend to use Python3 virtual environments:

```bash
sudo apt-get install python3-venv
```

Then run:

```bash
python3 -m venv env
make init
```

## Known Bugs: Az login

az login will wait for interactive authentication, the logs are not returned so the execution is blocked.

```python
az('login')
```
