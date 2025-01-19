import argparse

from driving.cli.commands import execute_command


def main():
    parser = argparse.ArgumentParser(description="CLI for the application")
    parser.add_argument("command", help="The command to execute")
    parser.add_argument("--arg1", help="Argument 1 for the command", required=False)
    parser.add_argument("--arg2", help="Argument 2 for the command", required=False)

    args = parser.parse_args()
    execute_command(args.command, arg1=args.arg1, arg2=args.arg2)


if __name__ == "__main__":
    main()

# commands
# python -m cli.main example --arg1 value1 --arg2 value2
