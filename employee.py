"""AndrewID: judahemu & juwizeyi"""

import json

class Employee:
    """
    A class representing an employee.

    Attributes:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        email (str): Official email of the employee (FORMAT: first_name.last_name@andrew.cmu.edu).
        salary (int): The salary of the employee.
        gender (str): The gender of the employee.
        employee_id (str): The employee_id that is generated automatically by the system.
        job_title (str): The job title of the employee (Director, Intern, Manager).
        department (str): The department for the employee (specific to Managers and Directors).
        internship_duration (int): The duration of the intern's internship in months (specific to Interns).
    """

    # Variable to store informations
    all_employees = {}

    def __init__(self, first_name, last_name, employee_id, employee_gender, salary, job_title, level, team = None, department=None, internship_duration=None):
        """Initializing the attributes of this class, but we add some condition
        to make sure that users are entering correct informations"""
        
        if not first_name or not last_name or not employee_gender or salary < 0:
            raise ValueError("Invalid input for employee attributes.")
        
        valid_level = ["employee", "manager", "director", "intern"]
        if level.lower() not in valid_level:
            raise ValueError(f"Invalid position. Allowed values are {', '.join(valid_level)}.")

        if level.lower() == "employee" or level.lower() == "manager" or level.lower() == "intern":
            if not department or not team:
                raise ValueError("Department or team is required for Interns, Employees and Managers.")
        
        elif level.lower() == "intern":
            if not team or not isinstance(internship_duration, int) or not (3 <= internship_duration <= 6):
                raise ValueError("Invalid input: Internship duration.")
        
        elif level.lower() == "director":
            if not department:
                raise ValueError("Department is required for Directors.")
            team = None
        else:
            internship_duration = None # If not an intern, internship_duration should be None
        
        self._first_name = first_name
        self._last_name = last_name
        self._employee_gender = employee_gender
        self._email = self.generate_email()
        self.__salary = salary
        self.__employee_id = employee_id
        self.job_title = job_title
        self.level = level
        self.team = team
        self.department = department
        self.internship_duration = internship_duration

        self.all_employees[self.get_employee_id()] = {
            "full_name": self.get_full_name(),
            "email": self.get_email(),
            "job_title": self.job_title,
            "level": self.level,
            "gender": self.get_gender(),
            "salary": self.get_salary(),
            "department": self.department,
            "team": self.team,
            "intern_duration_months": self.internship_duration
        }

    def generate_email(self):
        """Generate automatically the email based on first name and last name"""
        return f"{self._first_name.lower()}.{self._last_name.lower()}@andrew.cmu.edu"
    
    @staticmethod
    def store_employees_to_json(new_employee_data):
        """Append new employee data to an existing JSON file if employee ID is not present."""
        try:
            # Load existing data from the JSON file
            with open("1. employees.json", "r", encoding="utf-8") as existing_file:
                existing_data = json.load(existing_file)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty list
            existing_data = []

        existing_employee_ids = []
        # Check if employee ID already exists in the file
        for employee_info in existing_data:
            for existing_employee_id, _ in list(employee_info.items()):
                existing_employee_ids.append(existing_employee_id)
        
        for new_employee_id, _ in list(new_employee_data.items()):
            if new_employee_id in existing_employee_ids:
                raise ValueError(f"EmployeeID {new_employee_id} already exists.")
        
        # Append new employee data to the existing data
        existing_data.append(new_employee_data)
        
        # Write the updated data back to the JSON file
        with open("1. employees.json", "w", encoding="utf-8") as updated_file:
            json.dump(existing_data, updated_file, indent=4)

    def get_full_name(self):
        """Getter for full employee name by combining the first and last name"""
        return self._first_name + " " + self._last_name

    def get_email(self):
        """Getter for email"""
        return self._email

    def get_salary(self):
        """Getter for salary"""
        return self.__salary

    def get_employee_id(self):
        """Getter for employee_id"""
        return self.__employee_id

    def get_gender(self):
        """Getter for gender"""
        return self._employee_gender
