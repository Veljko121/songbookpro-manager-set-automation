from lib import run
from properties_handler import PropertiesHandler

def main():
    properties_handler = PropertiesHandler()
        
    try:
        run(properties_handler.get_property("IP_ADDRESS"), properties_handler.get_property("SPREADSHEET_PATH"), properties_handler.get_property("SHEET"), properties_handler.get_property("SET_NAME"))
    except FileNotFoundError:
        print("Spreadsheet '" + properties_handler.get_property("SPREADSHEET_PATH") + "' doesn't seem to exist. Try again.")
        exit(1)
    except KeyError:
        print("Worksheet '" + properties_handler.get_property("SHEET") + "' doesn't seem to exist. Try again.")
        exit(1)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
