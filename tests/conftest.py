import os

import pytest

# Set the path to import az
import context
from az.cli import az


@pytest.fixture(scope="module")
def az_login():
    """
    az_login signs in using a service principal
    expects to have the environment variables for login present
    https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest#sign-in-using-a-service-principal
    """
    sp_name = os.environ["AZ_SP_APP_ID"]
    sp_password = os.environ["AZ_SP_SECRET"]
    sp_tenant = os.environ["AZ_SP_TENANT"]

    login_command = "login --service-principal --username {} --password {} --tenant {}".format(
        sp_name, sp_password, sp_tenant)

    az(login_command)
