import os
from lib import run

def load_properties(filepath):
    properties = {}
    if not os.path.exists(filepath):
        print(f"Error: Properties file '{filepath}' not found.")
        exit(1)
    
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):  # Ignore empty lines and comments
                continue
            key_value = line.split("=", 1)
            if len(key_value) != 2:
                print(f"Error: Invalid line in properties file: {line}.")
                exit(1)
            key, value = key_value
            properties[key.strip()] = value.strip()
    
    return properties

def main():
    properties_file = "properties.txt"
    properties = load_properties(properties_file)
    
    required_keys = ["URL", "SPREADSHEET", "SHEET", "SET_NAME"]
    
    for key in required_keys:
        if key not in properties or not properties[key]:
            print(f"Error: Missing required property '{key}' in {properties_file}.")
            exit(1)
    
    run(properties["URL"], properties["SPREADSHEET"], properties["SHEET"], properties["SET_NAME"])

if __name__ == "__main__":
    main()
