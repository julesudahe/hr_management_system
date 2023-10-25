import json
import os

class HRMISDataSerializer:
    """Initializing the attributes of this class"""
    def __init__(self, employee_filename="employees.json", attendance_filename="attendance.json", salary_filename="salary.json"):
        """Initializing the attributes of this class"""
        self.employee_filename = employee_filename
        self.attendance_filename = attendance_filename
        self.salary_filename = salary_filename

    def serialize_employees_to_json(self, employee_data):
        """Initializing the attributes of this class"""
        with open(self.employee_filename, "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)

    def serialize_attendance_to_json(self, attendance_data):
        """Initializing the attributes of this class"""
        with open(self.attendance_filename, "w", encoding="utf-8") as json_file:
            json.dump(attendance_data, json_file, indent=4)

    def serialize_salary_to_json(self, salary_data):
        """Initializing the attributes of this class"""
        with open(self.salary_filename, "w", encoding="utf-8") as json_file:
            json.dump(salary_data, json_file, indent=4)

    def deserialize_employees_from_json(self):
        """Initializing the attributes of this class"""
        return self._deserialize_from_json(self.employee_filename)

    def deserialize_attendance_from_json(self):
        """Initializing the attributes of this class"""
        return self._deserialize_from_json(self.attendance_filename)

    def deserialize_salary_from_json(self):
        """Initializing the attributes of this class"""
        return self._deserialize_from_json(self.salary_filename)

    def _deserialize_from_json(self, filename):
        """Initializing the attributes of this class"""
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
