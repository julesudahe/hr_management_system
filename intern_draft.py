"""AndrewID: judahemu"""

# Importing the Employee class from employee.py file (saved in the path as this file)
from salary import Salary

class Intern(Salary):
    """
    A class representing a director, and it is inheriting attributes and 
    methods from the Employee class.
    
    Additional attributes for Manager class:
        university_name (str): The university name of the intern.
        program_name (str): The program name of the intern.
        internship_duration (int): The duration of the intern's internship (3-6 months)
    """

    def __init__(self, first_name, last_name, employee_gender, salary, university_name, program_name, internship_duration, deductions=0, allowance=0, bonus=0):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary, deductions, allowance, bonus)
    
        # exception handling to make sure that the program does not clash
        if not university_name or not program_name or not isinstance(internship_duration, int) or not (3 <= internship_duration <= 6):
            raise ValueError("Invalid university name, program name, or internship duration.")
        
        self.university_name = university_name
        self.program_name = program_name
        self.internship_duration = internship_duration
    
    def show_intern_info(self):
        """Build the print function for this class"""
        print(f"EmployeeID: {self.get_employee_id()}")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print('Position: Intern')
        print(f"University: {self.university_name}")
        print(f"Program: {self.program_name}")
        print(f"Internship Duration (Months): {self.internship_duration}")
        print(f'Gender: {self.get_gender()}')
        print(f"Salary: {self.calculate_intern_earnings(self.internship_duration):.2f}")



