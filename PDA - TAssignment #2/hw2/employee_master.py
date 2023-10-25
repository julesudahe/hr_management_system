"""AndrewID: judahemu & Jeannette"""

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

    Methods:
        show_employee_info(): Displays the information of the employee.
    """

    # Variable to store informations
    all_employees = {}
    __last_employee_id = 0

    def __init__(self, first_name, last_name, employee_gender, salary, job_title, level, team = None, department=None, internship_duration=None):
        """Initializing the attributes of this class"""
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
            # If not an intern, internship_duration should be None
            internship_duration = None
        
        
        
        self._first_name = first_name
        self._last_name = last_name
        self._employee_gender = employee_gender
        self._email = self.generate_email(first_name, last_name)
        self.__salary = salary
        self.__employee_id = self.generate_employee_id()
        self.job_title = job_title
        self.level = level
        self.team = team
        self.department = department
        self.internship_duration = internship_duration

        self.__class__.all_employees[self.get_employee_id()] = {
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

        # Automatically store data to JSON
        self.__class__.store_employees_to_json()

    @classmethod
    def generate_employee_id(cls):
        """Generate automatically the employee ID"""
        employee_id = f"CMUID{cls.__last_employee_id + 1:04}"
        cls.__last_employee_id += 1
        return employee_id

    @staticmethod
    def generate_email(first_name, last_name):
        """Generate automatically the email based on first name and last name"""
        return f"{first_name.lower()}.{last_name.lower()}@andrew.cmu.edu"
    
    @classmethod
    def get_all_employees(cls):
        """Returns a dictionary containing all employee information."""
        return cls.all_employees
    
    @staticmethod
    def store_employees_to_json():
        """Store all employee data to a JSON file."""
        with open("employees.json", "w", encoding="utf-8") as json_file:
            json.dump(Employee.get_all_employees(), json_file, indent=4)

    def get_full_name(self):
        """Getter to combine the first and last name"""
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
    
    def show_employee_info(self):
        """Build the print function for this class"""
        print(f"EmployeeID: {self.get_employee_id()}")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Job Title: {self.job_title}")
        print(f"Gender: {self.get_gender()}")
        print(f"Salary: {self.get_salary():.2f}")

        if self.level == "Director":
            print(f"Department: {self.department}")
        elif self.level == "Manager":
            print(f"Team: {self.team}")
        elif self.level == "Intern":
            print(f"Team: {self.team}")
            print(f"Internship Duration (Months): {self.internship_duration}")

# Example 1: Creating an Employee
employee1 = Employee("John", "Doe", "Male", 50000, "Marketing Manager", "Manager", team="Marketing", department="Marketing & Communications")

# Example 2: Creating a Manager
employee2 = Employee("Alice", "Smith", "Female", 40000, "Manager", "Manager", team="Sales", department="Sales")

# Example 3: Creating a Director
employee3 = Employee("Bob", "Johnson", "Male", 30000, "Director of Operations", "Director", department="Finance")

# Example 4: Creating an Intern
employee4 = Employee("Eva", "Brown", "Female", 20000, "Researc Intern", "Intern", team="Development", department="Research", internship_duration=6)
