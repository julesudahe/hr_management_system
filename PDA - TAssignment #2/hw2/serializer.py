"""AndrewID: judahemu & Jeannette"""

import json
import os

class DataSerializer:
    """ddd"""
    def __init__(self):
        pass

    def deserialize_employees_from_json(self):
        """ddd"""
        if os.path.exists("employees.json"):
            with open("employees.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                employees = {}
                for employee_id, info in data.items():
                    full_name = info.get("full_name")
                    salary = info.get("salary")
                    employees[employee_id] = {
                        "full_name": full_name,
                        "salary": salary
                    }
                return employees
        else:
            return {}