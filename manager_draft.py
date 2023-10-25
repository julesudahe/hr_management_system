"""AndrewID: judahemu"""

# Importing the Employee class from employee.py file (saved in the path as this file)
from salary import Salary

class Manager(Salary):
    """
    A class representing a manager, and it is inheriting attributes and 
    methods from the Employee class.
    
    Additional attributes for Manager class:
        department (str): The department for the manager.
        direct_reports (int): The number of direct reporters.
        manager_rate (float): The support allowance for manager.
    """

    def __init__(self, first_name, last_name, employee_gender, salary, department, direct_reports, manager_rate, deductions=0, allowance=0, bonus=0):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary, deductions, allowance, bonus)
        
        # exception handling to make sure that the program does not clash
        if not department or not isinstance(direct_reports, int) or direct_reports < 0:
            raise ValueError("Invalid department or number of direct reports.")
        
        if 0 <= manager_rate <= 60:
            self.__manager_rate = manager_rate
        else:
            raise ValueError("Rate must be between 0 and 60%.")

        self.department = department
        self.direct_reports = direct_reports
        
    def get_manager_rate(self):
        """Getter for manager rate"""
        return self.__manager_rate

    def show_manager_info(self):
        """Build the print function for this class"""
        print(f"EmployeeID: {self.get_employee_id()}")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print('Position: Manager')
        print(f"Department: {self.department}")
        print(f"Direct Reports: {self.direct_reports}")
        print(f'Gender: {self.get_gender()}')
        print(f"Salary: {self.calculate_manager_earnings(self.get_manager_rate()):.2f}")

