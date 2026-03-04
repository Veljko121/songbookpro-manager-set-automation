from lib import run
import argparse

def cli():
    parser = argparse.ArgumentParser(description="Manage song sets from spreadsheets")
    parser.add_argument("--ip", "-i", type=str, required=True, help="IP address of the API")
    parser.add_argument("--spreadsheet", "-s", type=str, required=True, help="Path to the spreadsheet file")
    parser.add_argument("--sheet", "-sh", type=str, required=True, help="Sheet name to load songs from")
    parser.add_argument("--set-name", "-n", type=str, required=True, help="Name of the set to be created")
    args = parser.parse_args()

    run(args.ip, args.spreadsheet, args.sheet, args.set_name)


if __name__ == "__main__":
    cli()
