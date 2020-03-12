
# app.py
import pprint
import sys

from az.cli import az, ExitStatus


def main():
    pp = pprint.PrettyPrinter(indent=4)

    code, result = az("group show -n test")

    if code == ExitStatus.success:
        pp.pprint(result)
    else:
        print("error")


if __name__ == "__main__":
    # execute only if run as a script
    main()
