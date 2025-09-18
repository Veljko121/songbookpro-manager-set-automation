import os

REQUIRED_PROPERTIES = ["IP_ADDRESS", "PORT", "SPREADSHEET_PATH", "SHEET", "SET_NAME"]

class PropertiesHandler():
    def __init__(self, properties_path: str = "resources/application.properties"):
        self.properties_path = properties_path
        self.check_properties_file()

    def check_properties_file(self):
        if not os.path.exists(self.properties_path):
            open(self.properties_path, "w", encoding="utf-8").close()

    def load_properties(self):
        properties = {}
        with open(self.properties_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            elements = line.strip().split("=", 1)
            property_name, value = elements[0], elements[1]
            properties[property_name] = value
        self._fill_in_missing_properties(properties)
        return properties
    
    def save_properties(self, properties: dict):
        self._fill_in_missing_properties(properties)
        with open(self.properties_path, "w", encoding="utf-8") as file:
            for property_name in properties.keys():
                file.write(self._to_property_line(property_name, properties[property_name]))

    def _fill_in_missing_properties(self, properties: dict):
        for required_property in REQUIRED_PROPERTIES:
            if required_property not in properties:
                properties[required_property] = ""

    def _to_property_line(self, key, value):
        return f"{key}={value}\n"

    
if __name__ == "__main__":
    handler = PropertiesHandler()
    properties = handler.load_properties()
    print(properties)
    handler.save_properties(properties)
