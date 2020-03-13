# app.py
import pprint

from az.cli import az, SUCCESS_CODE


def main():
    show(*az("group show -n test"))
    show(*az("group list"))


def show(code, dict, log):
    pp = pprint.PrettyPrinter(indent=4)
    if code == SUCCESS_CODE:
        pp.pprint(dict)
    else:
        print(log)


if __name__ == "__main__":
    # execute only if run as a script
    main()
