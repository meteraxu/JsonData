import json
import os
import config
from json import JSONDecodeError

class system_method:
    def __init__(self):
        print("Init system core successfully!")
    def clean_screen(self):
        if config.compatibility_mode:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            print("In Compatibility mode,will skip this method.")

class JsonData:
    def __init__(self, filename = "database.json"):
        self.filename = filename
        self.data = self.load()
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r",encoding="utf-8") as f:
                    return json.load(f)
            except JSONDecodeError:
                return {}
        return {}
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    def set_value(self, key, value):
        if not isinstance(value, dict):
            raise ValueError("Error:Stuff")
        self.data[key] = value
        self.save()
    def get_value(self, key):
        return self.data.get(key)
    def delete_key(self, key):
        if key in self.data:
            del self.data[key]
            self.save()
            return True
        return False
    def get_all(self):
        return self.data


# db = JsonData("database.json")

# db.set_value("admin", {"name": "Ciesoc","age":16})
# print("Afternoon,", db.get_value("admin").get("name")+"!It is your", db.get_value("admin").get("age"), "time.")
