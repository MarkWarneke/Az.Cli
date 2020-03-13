import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/')))

import pytest

from az.cli import az

@pytest.fixture(scope="module")
def az_login():
    """
    az_login signs in using a service principal
    expects to have the environment variables for login present
    https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principal
    """
    sp_name = os.environ["ENV_SP_NAME"]
    sp_password = os.environ["ENV_SP_SECRET"]
    sp_tenant = os.environ["ENV_SP_TENANT"]

    login_command = "login --service-principal --username {} --password {} --tenant {}".format(sp_name, sp_password, sp_tenant)

    az(login_command)