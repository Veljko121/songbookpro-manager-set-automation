class PropertiesHandler():
    def __init__(self, properties_path: str = "resources/application.properties"):
        self.properties_path = properties_path
        self.property_names = ["IP_ADDRESS", "SPREADSHEET_PATH", "SHEET", "SET_NAME"]

    def load_properties(self):
        properties = {}
        with open(self.properties_path, "r") as file:
            lines = file.readlines()
        for line in lines:
            elements = line.strip().split("=")
            property_name, value = elements[0], elements[1]
            properties[property_name] = value
        self.fill_in_missing_properties(properties)
        return properties
    
    def save_properties(self, properties: dict):
        self.fill_in_missing_properties(properties)
        with open(self.properties_path, "w") as file:
            for property_name in properties.keys():
                file.write(self.to_property_line(property_name, properties[property_name]))

    def fill_in_missing_properties(self, properties: dict):
        for required_property in self.property_names:
            if required_property not in properties:
                properties[required_property] = ""

    def to_property_line(self, key, value):
        return f"{key}={value}\n"

    
if __name__ == "__main__":
    handler = PropertiesHandler()
    properties = handler.load_properties()
    handler.save_properties(properties)
