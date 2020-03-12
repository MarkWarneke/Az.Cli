
# app.py
import pprint
import sys
sys.path.append('../src/az')


if __name__ == "__main__":
    from az.cli import az, ExitStatus

    pp = pprint.PrettyPrinter(indent=4)

    code, result = az("group show -n test")

    if code == ExitStatus.success:
        pp.pprint(result)
    else:
        print("error")
