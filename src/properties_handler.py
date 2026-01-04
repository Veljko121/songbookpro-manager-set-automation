import os


class PropertiesHandler():
    def __init__(self, properties_path: str = "resources/application.properties"):
        self.properties_path = properties_path
        self._check_properties_file()
        self._load_properties()

    def _check_properties_file(self):
        if not os.path.exists(self.properties_path):
            open(self.properties_path, "w", encoding="utf-8").close()

    def _load_properties(self):
        self.properties = {}
        with open(self.properties_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            elements = line.strip().split("=", 1)
            property_name, value = elements[0], elements[1]
            self.properties[property_name] = value
        return self.properties
    
    def get_property(self, property_name: str):
        return self.properties.get(property_name, "")
    
    def update_properties(self, properties: dict):
        self.properties.update(properties)
    
    def save_properties(self, properties: dict):
        with open(self.properties_path, "w", encoding="utf-8") as file:
            for property_name in properties.keys():
                file.write(self._to_property_line(property_name, properties[property_name]))

    def _to_property_line(self, key, value):
        return f"{key}={value}\n"
