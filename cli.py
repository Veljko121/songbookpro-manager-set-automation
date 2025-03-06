from cli import run
import argparse

def cli():
    parser = argparse.ArgumentParser(description="Manage song sets from spreadsheets")
    parser.add_argument("--url", "-u", type=str, required=True, help="Base URL of the API")
    parser.add_argument("--spreadsheet", "-s", type=str, required=True, help="Path to the spreadsheet file")
    parser.add_argument("--sheet", "-sh", type=str, required=True, help="Sheet name to load songs from")
    parser.add_argument("--set-name", "-n", type=str, required=True, help="Name of the set to be created")
    args = parser.parse_args()

    run(args.url, args.spreadsheet, args.sheet, args.set_name)


if __name__ == "__main__":
    cli()
