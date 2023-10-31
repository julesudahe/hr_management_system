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
            with open("1. employees.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        else:
            return {}

    def deserialize_attendance_from_json(self):
        """Deserialize attendance data from attendance.json file."""

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
