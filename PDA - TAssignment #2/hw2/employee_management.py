"""AndrewID: judahemu & Jeannette"""

import json
from employee import Employee
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
    
    def update_data(self):
        """Update existing employee data with new data."""
        data_deserializer = DataDeserializer()
        existing_data = data_deserializer.deserialize_employees_from_json()

        employee_id = input("Enter the Employee ID to update: ")

        for entry in existing_data:
            if employee_id in entry:
                employee_data = entry[employee_id]
                print(f"Current Information for Employee ID {employee_id}:")
                print(employee_data)

                field_to_update = input("Enter the field to update: ").strip().lower()
                new_value = input(f"Enter the new value for {field_to_update}: ")

                employee_data[field_to_update] = new_value

                updated_existing = True
                break

        self._save_to_json(existing_data)
        
        if not updated_existing:
            print(f"No employee found with ID: {employee_id}")

        return existing_data

    def _save_to_json(self, employee_data):
        """Save the employee data to the JSON file."""
        with open("employees.json", "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)

# Create an instance of EmployeeManagement class
employee_management = EmployeeManagement()
