"""AndrewID: judahemu"""

# Importing the Employee class from employee.py file (saved in the path as this file)
from salary import Salary

class Director(Salary):
    """
    A class representing a director, and it is inheriting attributes and 
    methods from the Employee class.
    
    Additional attributes for Manager class:
        department (str): The department for the manager.
        direct_reports (int): The number of direct reporters.
    """
    
    def __init__(self, first_name, last_name, employee_gender, salary, department, direct_reports, special_bonus_dir = 0.0, deductions=0, allowance=0, bonus=0):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary, deductions, allowance, bonus)
        
        # exception handling to make sure that the program does not clash
        if not department or not isinstance(direct_reports, int) or direct_reports < 0 or special_bonus_dir < 0:
            raise ValueError("Invalid department or number of direct reports or bonus.")
        
        self.department = department
        self.direct_reports = direct_reports
        self.__special_bonus_dir = special_bonus_dir

    def get_special_bonus_dir(self):
        """Getter for special bonus for directors"""
        return self.__special_bonus_dir

    def show_director_info(self):
        """Build the print function for this class"""
        print(f"EmployeeID: {self.get_employee_id()}")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print('Position: Director')
        print(f"Department: {self.department}")
        print(f"Direct Reports: {self.direct_reports}")
        print(f'Gender: {self.get_gender()}')
        print(f"Salary: {self.calculate_director_earnings(self.get_special_bonus_dir()):.2f}")
