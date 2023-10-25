"""AndrewID: judahemu"""

# Importing the Employee class from employee.py file (saved in the path as this file)
from employee import Employee

class Salary(Employee):
    """
    bra bra bra bra
    """

    def __init__(self, first_name, last_name, employee_gender, salary, deductions = 0.0, allowance = 0.0, bonus = 0.0):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary)
        
        # exception handling to make sure that the program does not clash
        if not isinstance(deductions, allowance, bonus, int) or deductions < 0 or allowance < 0 or bonus < 0:
            raise ValueError("Deductions, allowance, or bonus cannot be negative.")
    
        self.__deductions = deductions
        self.__allowance = allowance
        self.__bonus = bonus

    def calculate_employee_salary(self):
        """Clculating the total salary of the employee"""
        total_salary = self.get_salary() + self.get_allowance + self.get_bonus() - self.get_deductions()
        
        return total_salary
    
    def calculate_intern_earnings(self, internship_duration):
        """Calculating the  intern's earnings based on internship duration."""
        intern_salary = self.calculate_employee_salary() * internship_duration / 12

        return intern_salary

    def calculate_manager_earnings(self, manager_rate):
        """Calculating the  manager's earnings based on the base salary and the manager rate."""
        manager_allowance = self.calculate_employee_salary() * manager_rate / 100
        manager_salary = self.calculate_employee_salary() + manager_allowance

        return manager_salary
    
    def calculate_director_earnings(self, special_bonus_dir):
        """Calculating the  director's earnings based on the base salary and the bonus."""
        director_salary = self.calculate_employee_salary() + special_bonus_dir
        
        return director_salary
        
    def get_bonus(self):
        """Getter for bonus"""
        return self.__bonus

    def get_deductions(self):
        """Getter for bonus"""
        return self.__deductions

    def get_allowance(self):
        """Getter for bonus"""
        return self.__allowance


    