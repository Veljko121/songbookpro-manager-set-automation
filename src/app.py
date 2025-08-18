from lib import run
from properties_handler import PropertiesHandler

def main():
    properties_handler = PropertiesHandler()
    properties = properties_handler.load_properties()
        
    try:
        run(properties["IP_ADDRESS"], properties["SPREADSHEET_PATH"], properties["SHEET"], properties["SET_NAME"])
    except FileNotFoundError:
        print("Spreadsheet '" + properties["SPREADSHEET_PATH"] + "' doesn't seem to exist. Try again.")
        exit(1)
    except KeyError:
        print("Worksheet '" + properties["SHEET"] + "' doesn't seem to exist. Try again.")
        exit(1)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
