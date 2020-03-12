# --------------------------------------------------------------------------------------------
# Copyright (c) Mark Warneke <warneke.mark@gmail.com> 2020
# Licensed under the MIT License. See License.txt in the project root for license information.
# Based on https://github.com/Azure/azure-cli/blob/8e369b9d2d63ddf5c6678ee710905bf9e5028f99/src/azure-cli-core/azure/cli/core/__init__.py
# --------------------------------------------------------------------------------------------

import sys
from io import StringIO
import json
import shlex

from exitstatus import ExitStatus

# https://github.com/Azure/azure-cli/blob/8e369b9d2d63ddf5c6678ee710905bf9e5028f99/src/azure-cli-core/azure/cli/core/__init__.py
from azure.cli.core import get_default_cli


def az(command):
    """
    This function executes a "az" command based on argument
    :param command: string
    Returns a tuple of error_code (1==success) and result (returns empty result on error)

    See implementation example here:
    https://github.com/Azure/azure-cli/blob/8e369b9d2d63ddf5c6678ee710905bf9e5028f99/src/azure-cli-core/azure/cli/core/__init__.py

    Reference can be found here:
    https://github.com/Azure/azure-cli/blob/fc532b4dee320e7f20994d548f284729a0c66ae8/src/azure-cli-testsdk/azure/cli/testsdk/base.py#L252
    """

    # Create default shell to run commands
    cli = get_default_cli()

    # Create string buffer to get the result
    stdout_buf = StringIO()

    try:
        # Split command https://docs.python.org/3/library/shlex.html#shlex.split
        args = shlex.split(command)
        # On success store error code
        exit_code = cli.invoke(args, out_file=stdout_buf) or ExitStatus.success

    except:
        # FIXME: Error will be printed to the stderr anyway, bug to intercept err stream
        # See:  https://github.com/Azure/azure-cli/blob/fc532b4dee320e7f20994d548f284729a0c66ae8/src/azure-cli-testsdk/azure/cli/testsdk/base.py#L252
        exit_code = ExitStatus.failure
        pass

    if exit_code == ExitStatus.success:
        return (exit_code, _parseResult(stdout_buf))
    else:
        return (exit_code, "")


def _parseResult(buffer):
    try:
        # Retrieve output buffer
        output = buffer.getvalue()
        # Turn json output into dict
        result = json.loads(output)
        return result
    except:
        raise BaseException("Error handling result")
