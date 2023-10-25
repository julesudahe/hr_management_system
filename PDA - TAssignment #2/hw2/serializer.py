import json
import os

class DataSerializer:
    def __init__(self, 
                 employee_filename="data/employees.json",
                 attendance_filename="data/attendance.json", 
                 salary_filename="data/salary.json"):
        self.employee_filename = employee_filename
        self.attendance_filename = attendance_filename
        self.salary_filename = salary_filename
        
        # Check if the 'data' folder exists, if not, create it
        data_folder = os.path.dirname(employee_filename)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

    def serialize_employees_to_json(self, employee_data):
        with open(self.employee_filename, "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)

    def serialize_attendance_to_json(self, attendance_data):
        with open(self.attendance_filename, "w", encoding="utf-8") as json_file:
            json.dump(attendance_data, json_file, indent=4)

    def serialize_salary_to_json(self, salary_data):
        with open(self.salary_filename, "w", encoding="utf-8") as json_file:
            json.dump(salary_data, json_file, indent=4)

# Example usage
# serializer = DataSerializer()
# serializer.serialize_employees_to_json(employee_data)
# serializer.serialize_attendance_to_json(attendance_data)
# serializer.serialize_salary_to_json(salary_data)
