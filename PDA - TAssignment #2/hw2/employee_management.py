"""AndrewID: judahemu & Jeannette"""

import json
from employee_master import Employee
from deserializer import DataDeserializer
# from attendance import Attendance
# from salary import Salary

class EmployeeManagement:
    """Initialize empty dictionaries to store employee objects, attendance, and salary information"""
        
    def __init__(self):
        """Initialize dictionaries to store employee objects, attendance, and salary information"""
        self.employees = {}
        # self.attendance_system = Attendance()
        # self.salary_system = Salary()

    def add_employee(self, first_name, last_name, employee_gender, salary, job_title, level, team=None, department=None, internship_duration=None):
        """Create an Employee object and add it to the employees dictionary"""
        Employee(first_name, last_name, employee_gender, salary, job_title, level, team, department, internship_duration)

    def delete_employee(self, target_employee_id):
        """Delete an employee's information from the JSON file."""
        data_deserializer = DataDeserializer()
        employee_data = data_deserializer.deserialize_employees_from_json()

        removed_employees = [employee_info for employee_info in employee_data if target_employee_id in employee_info.keys()]
        employee_data = [employee_info for employee_info in employee_data if target_employee_id not in employee_info.keys()]

        if removed_employees:
            self._save_to_json(employee_data)
            print(f"Employee with ID {target_employee_id} deleted.")
        else:
            print("Employee not found. Available IDs:", [list(record.keys())[0] for record in employee_data])
    
    def _save_to_json(self, employee_data):
        """Save the employee data to the JSON file."""
        with open("employees.json", "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)

employee_management = EmployeeManagement()
