"""AndrewID: judahemu & juwizeyi"""

import json
import os

class DataDeserializer:
    """
    This class is responsible for deserializing (read) data from JSON files,
    and save them to dictionary.
    """
    def __init__(self):
        pass # No attributes needed for this class

    def deserialize_employees_from_json(self):
        """Deserialize employee data from employees.json file."""

        if os.path.exists("1. employees.json"):
            try:
                with open("1. employees.json", "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    
                    if isinstance(data, list):
                        return data
                    else:
                        print("Invalid JSON format in employees.json")
                        return []
            except json.JSONDecodeError:
                print("Invalid JSON syntax in employees.json")
                return []
        else:
            print("employees.json file not found")
            return []
    
    def deserialize_attendance_from_json(self):
        """Deserialize salary data from attendance.json file."""
        
        if os.path.exists("2. attendance.json"):
            with open("2. attendance.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        else:
            return {}

    def deserialize_salary_from_json(self):
        """Deserialize salary data from salary.json file."""
        
        if os.path.exists("3. salary.json"):
            with open("3. salary.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        else:
            return {}
