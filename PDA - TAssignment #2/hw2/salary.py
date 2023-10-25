"""AndrewID: judahemu & Jeannette"""

# Importing the Employee class from employee.py file (saved in the path as this file)
from employee_master import Employee

class Salary(Employee):
    """
    This class import all attributes Employee class.
    We introduce new attributes: deductiopns, allowance, and bonus.

    We have different methods that we are using for salary calculations.
        - getters: this are the getters for our private attributes.
        - calculate_earnings: methods to calculate earning for based on job level.
        - calculate_employee_salary: calculating yearly salary for employee.
        - calculate_monthly_salary: calculating monthly salary for employee.
    """

    def __init__(self, first_name, last_name, employee_gender, salary, deductions = 0.0, allowance = 0.0, bonus = 0.0):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary)
        
        # exception handling to make sure that the program does not clash
        if not isinstance(deductions, allowance, bonus, int) or (50 < deductions < 0) or allowance < 0 or bonus < 0:
            raise ValueError("Deductions, allowance, or bonus cannot be negative.")
    
        self.__deductions = deductions
        self.__allowance = allowance
        self.__bonus = bonus

    def calculate_employee_salary(self):
        """Calculate the total salary breakdown of the employee per year"""
        annual_salary = self.get_salary()
        annual_allowance = self.get_allowance() * self.get_salary() / 100
        annual_bonus = self.get_bonus() * self.get_salary() / 100
        annual_deductions = self.get_deductions() * self.get_salary() / 100
        
        total_salary = annual_salary + annual_allowance + annual_bonus - annual_deductions
        
        salary_breakdown = {
            'Base Salary (Yearly)': annual_salary,
            'Allowance (Yearly)': annual_allowance,
            'Bonus (Yearly)': annual_bonus,
            'Deductions, taxes, etc. (Yearly)': annual_deductions,
            'Total Salary (Yearly)': total_salary
        }
        return salary_breakdown
    
    def calculate_monthly_salary(self):
        # ADD: handle internship monthly salary differently
        """Calculate monthly net salary."""
        yearly_breakdown = self.calculate_employee_salary()
        monthly_base_salary = yearly_breakdown['Base Salary (Yearly)'] / 12
        total_allowance = yearly_breakdown['Allowance (Yearly)'] / 12
        total_bonus = yearly_breakdown['Bonus (Yearly)'] / 12
        total_deductions = yearly_breakdown['Deductions, taxes, etc. (Yearly)'] / 12

        net_pay = monthly_base_salary + total_allowance + total_bonus - total_deductions

        salary_breakdown = {
            'Base Salary (Monthly)': monthly_base_salary,
            'Allowance (Monthly)': total_allowance,
            'Bonus (Monthly)': total_bonus,
            'Deductions (Monthly)': total_deductions,
            'Net Pay (Monthly)': net_pay
        }
        return salary_breakdown
        
    def get_bonus(self):
        """Getter for bonus"""
        return self.__bonus

    def get_deductions(self):
        """Getter for bonus"""
        return self.__deductions

    def get_allowance(self):
        """Getter for bonus"""
        return self.__allowance


