"""AndrewID: judahemu & Jeannette"""

import json
import os

class DataSerializer:
    """ddd"""
    def __init__(self,
                 attendance_filename="attendance.json",
                 salary_filename="salary.json"):
        self.attendance_filename = attendance_filename
        self.salary_filename = salary_filename
        
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

    def serialize_attendance_to_json(self, attendance_data):
        """ddd"""
        with open(self.attendance_filename, "w", encoding="utf-8") as json_file:
            json.dump(attendance_data, json_file, indent=4)

    def serialize_salary_to_json(self, salary_data):
        """ddd"""
        with open(self.salary_filename, "w", encoding="utf-8") as json_file:
            json.dump(salary_data, json_file, indent=4)
