import os
import re

WORKFLOW_RELEASE = "Release Package"
NAME_PROD = "az.cli"
NAME_DEV = "az-cli-MARKWARNEKE"


def getVariables():

    workflow_name = os.environ["GITHUB_WORKFLOW"]

    if WORKFLOW_RELEASE == workflow_name:
        version = getVersionProd()
        name = NAME_PROD
    else:
        version = getVersionDev()
        name = NAME_DEV

    return name, version


def getVersionProd():
    REF_PREFIX = "refs/tags/"

    github_ref = os.environ["GITHUB_REF"]
    return re.sub(REF_PREFIX, '', github_ref)


def getVersionDev():
    return os.environ["GITHUB_RUN_NUMBER"]
