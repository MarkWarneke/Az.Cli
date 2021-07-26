# Az.Cli

[![PyPi](https://img.shields.io/pypi/pyversions/az.cli)](https://pypi.python.org/pypi/az.cli)
[![Build Status master](https://github.com/MarkWarneke/Az.Cli/workflows/Build/badge.svg?branch=master)](https://github.com/MarkWarneke/Az.Cli/actions?query=workflow%3ABuild)
[![Build Status dev](https://github.com/MarkWarneke/Az.Cli/workflows/Build/badge.svg?branch=dev)](https://github.com/MarkWarneke/Az.Cli/actions?query=workflow%3ABuild)

> This package is not officially maintained and developed by Microsoft - visit [github.com/Azure/azure-cli](https://github.com/Azure/azure-cli) for the official azure-cli.

`Az.Cli` is an easy-to-use Python interface that lets developers and administrators query Azure resources.
The Python package is providing a way to interact with Azure using Python while sticking to a well-known concept of the Azure CLI.

```
exit_code, result_dict, logs = az("group list")
```

If you are already familiar with the Azure CLI you should feel right at home using the `Az.Cli` Python packge API.

## Usage

You can find a getting started guide here [@markwarneke.me/2021-03-14-Query-Azure-Resources-Using-Python](https://markwarneke.me/2021-03-14-Query-Azure-Resources-Using-Python/).

Install the package

```bash
pip install az.cli
```

Login using `az login` or [sign in using a service principal](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principalt).

Under the hood the package uses the [~/.azure](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/_environment.py) folder to persist and retrieve config.

The `az` function returns a named tuple that allows you to retrieve the results easily.

```python
AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
```

- The [`error_code`](https://docs.python.org/2/library/sys.html#sys.exit) where `0 == success`.
- The `result_dict` containing a python dictionary on a successful return.
- On failure (`error_code` > 0) a log message is available in the `log` property as a string.

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
Import the pacakge function `from az.cli import az` and run any query by executing the method `az("<my command>")` to invoke the Azure CLI command.

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

## Programmatically Setting The Azure Config

To change the Azure context, the "session" in which you are logged in, the package relies on the stored credentials inside the `~/.azure` folder by default.
In order to change the context a simple change to the environment variable `AZURE_CONFIG_DIR` will point to a new context.
This can easily be done in Python using the `os.enviorn` interface.

```bash
az login
mv ~/.azure/* ~/.azure-mw

az login --service-principal -u $id -p $p -t $t
# creates new ~/.azure folder
```

In Python the environment variable can be set using:

```python
os.environ['AZURE_CONFIG_DIR'] = "<OTHER AZURE CONFIG DIR>"
```

Changing the `AZURE_CONFIG_DIR` environment variables is described in the docs to the [Azure CLI environment variables](https://docs.microsoft.com/en-us/cli/azure/use-cli-effectively?view=azure-cli-latest#cli-environment-variables).
To demonstrate how to change the environment variable programmatically a small example:

```python
from az.cli import az
import os

exit_code, result_dict, logs = az("group list")
print (result_dict)
# [{'id': '/subscriptions/...', 'location': 'westeurope',  'name': 'test1']

# Change the environment variable
os.environ['AZURE_CONFIG_DIR'] = '/Users/mark/.azure_mw'

exit_code, result_dict, logs = az("group list")
print (result_dict)
# [{'id': '/subscriptions/...', 'location': 'westeurope', 'name': 'test2']
```

## How it works

The package is an easy-to-use abstraction on top of the officiale Microsoft [Azure CLI](https://github.com/Azure/azure-cli).
The official [azure.cli.core](https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/__init__.py) library is simply wrapped in a funciton to execute Azure CLI commands using Python3.
The package provides a funciton `az` the is based on the class `AzCLI`.
It exposes the function to execute `az` commands and returns the results in a structured manner.

It has thus a similar API and usage to the shell version of the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest), but commands can be executed within Python, leveraging Pythons full potential. 

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

### Augmenting official Azure CLI Docker image

To those who want to use this wrapper with the [official Azure CLI Docker image](https://docs.microsoft.com/en-us/cli/azure/run-azure-cli-docker), then the quickest way is to mimic the following:

```dockerfile
FROM mcr.microsoft.com/azure-cli:latest

ENV PATH="/venv/bin:${PATH}"

RUN : \
    && python3 -m venv /venv \
    && pip install --disable-pip-version-check --no-cache-dir --no-dependencies az.cli

ENV PYTHONPATH="/usr/local/lib/python3.8/site-packages"
```

What that does is:

- adds the virtual environment directory to the `PATH` environment variable
- installs this project into that virtual environment _without_ installing dependencies
  - as they are already in the original image
  - this is what `--no-dependencies` does
- sets the `PYTHONPATH` environment variable to the equal the path at which the already included Azure CLI modules exist
  - it's added at the end as opposed to the first `ENV` line to avoid overriding the path at which this project is installed at

The `--disable-pip-version-check` option is set as it offers no tangible benefit to check Pip's version when building. The same goes for `--no-cache-dir` as the resulting image will be smaller due to Pip not having cached anything.

It's not possible, [that I know of](https://github.com/moby/moby/issues/29110) to set this dynamically, so this needs to be validated against the version of Python used in [their Dockerfile](https://github.com/Azure/azure-cli/blob/dev/Dockerfile).
