"""AndrewID: judahemu & Jeannette"""

import json
import os

class DataDeserializer:
    """ddd"""
    def __init__(self):
        pass

    def deserialize_employees_from_json(self):
        """ddd"""
        if os.path.exists("employees.json"):
            with open("employees.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
    
                return data
        else:
            return {}

    def deserialize_attendance_from_json(self):
        """ddd"""
        if os.path.exists("attendance.json"):
            with open("attendance.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
    
                return data
        else:
            return {}

    def deserialize_salary_from_json(self):
        """ddd"""
        if os.path.exists("salary.json"):
            with open("salary.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
    
                return data
        else:
            return {}
