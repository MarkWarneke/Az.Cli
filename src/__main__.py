# app.py
"""
Demonstration/Example script of `az("<Command>")` interface
"""
from az.cli import az, SUCCESS_CODE


def main():
    """
    Demonstrage the usage of `az("<Command>")` by invoking one failing and one working cmd
    """
    show(*az("login"))

    show(*az("group show -n test"))
    show(*az("group list"))


def show(exit_code, result_dict, log):
    """
    Prints a successfull command using pprint
    Prints an unsuccessfull command as a simple print
    """
    import pprint
    pp = pprint.PrettyPrinter(indent=2)

    if exit_code == SUCCESS_CODE:
        pp.pprint(result_dict)
    else:
        print(log)


if __name__ == "__main__":
    # execute only if run as a script
    main()
