# Az.Cli

Python [azure.cli.core](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/__init__.py) interface to execute `az` [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) commands in python.

## Prerequisites

- install [python3](https://www.python.org/downloads/)
- install `REQUIREMENTS.txt` use `make init`
- login to azure using `az login` (this can also be done interactively using the library) see [Sign in using a service principal](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principalt)
- run `python3 src`

## Example

```python
from az.cli import az, ExitStatus
exitCode, resultSet = az("group show -n test")
```

You can also interactively traverse the resultSet in python interactive. Navigate into `src` and run `python3`. Import the library by `from az.cli import az` and run any `az` command e.g. `az("group list")` to fetch all resource groups.

```python
# cd src
# python3
from az.cli import az
az("group list") # list return tuple (exitCode, resultSet)
az("group list")[1] # return resultSet content <dict>
az("group list")[1][0]['id'] # Enumerate id of first element in resultSet
```