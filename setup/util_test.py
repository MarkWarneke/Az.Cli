import pytest

from util import *

# For prod releases
PROD_VERSION_CORRECT = '1.0'
GITHUB_REF_CORRECT = 'refs/tags/1.0'

# For dev releases
GITHUB_RUN_NUMBER_CORRECT = '2'
DEV_VERSION_CORRECT = GITHUB_RUN_NUMBER_CORRECT

GITHUB_WORKFLOW_PRE_RELEASE = 'Pre-Release Package'
GITHUB_REF_FALSE = 'not_there'


@pytest.fixture(scope="module")
def reset_env():
    """
    Change the environment variables to empy
    Each test should set during arrange
    """
    os.environ["GITHUB_WORKFLOW"] = ""
    os.environ["GITHUB_REF"] = ""
    os.environ["GITHUB_RUN_NUMBER"] = ""


def test_getVersionProd(reset_env):
    # arrange
    _setProd()

    # act
    version = getVersionProd()
    # assert
    assert version == PROD_VERSION_CORRECT


def test_getVersionDev(reset_env):
    # arrange
    _setNotProd()

    os.environ["GITHUB_RUN_NUMBER"] = GITHUB_RUN_NUMBER_CORRECT
    # act
    version = getVersionDev()

    # assert
    assert version == DEV_VERSION_CORRECT


def test_prod_getVariables():
    # arrange
    _setProd()
    # act
    name, version = getVariables()
    # assert
    assert name == NAME_PROD
    assert version == PROD_VERSION_CORRECT


def test_dev_getVariables():
    # arrange
    _setNotProd()
    # act
    name, version = getVariables()
    # assert
    assert name == NAME_DEV
    assert version == DEV_VERSION_CORRECT


def _setProd():
    os.environ["GITHUB_REF"] = GITHUB_REF_CORRECT
    os.environ["GITHUB_WORKFLOW"] = WORKFLOW_RELEASE


def _setNotProd():
    os.environ["GITHUB_WORKFLOW"] = GITHUB_WORKFLOW_PRE_RELEASE
    os.environ["GITHUB_REF"] = GITHUB_REF_FALSE
