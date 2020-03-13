import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/')))

import pytest

from az.cli import az

AZ_SUCCESSFUL_COMMAND = "group list"
AZ_FAIL_COMMAND = "group show -n this-does-not-exist"

def test_az(az_login):
    error_code, result_dict, log = az(AZ_SUCCESSFUL_COMMAND)
    assert error_code == 0
    assert log == ""

def test_az_failure(az_login):

    error_code, result_dict, log = az(AZ_FAIL_COMMAND)
    assert error_code != 0
    assert log 

