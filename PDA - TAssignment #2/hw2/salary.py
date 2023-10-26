"""AndrewID: judahemu & Jeannette"""

# Importing the Employee class from employee.py file (saved in the path as this file)
# import os
import json
from deserializer import DataSerializer

class Salary:
    """
    This class import all attributes Employee class.
    We introduce new attributes: deductiopns, allowance, and bonus.

    We have different methods that we are using for salary calculations.
        - getters: this are the getters for our private attributes.
        - calculate_earnings: methods to calculate earning for based on job level.
        - calculate_employee_salary: calculating yearly salary for employee.
        - calculate_monthly_salary: calculating monthly salary for employee.
    """

    def __init__(self, deductions = 0.0, allowance = 0.0, bonus = 0.0):
        """Initializing the attributes of this class"""
        if not all(isinstance(attr, (int, float)) for attr in [deductions, allowance, bonus]) or not (0 <= deductions <= 50):
            raise ValueError("Deductions, allowance, or bonus should be a number between 0 and 50.")
        
        self.__deductions = deductions
        self.__allowance = allowance
        self.__bonus = bonus

        # Automatically store salary data to JSON file
        self.store_salary_to_json()
    
    def store_salary_to_json(self):
        """Store salary data to a JSON file."""
        # Calculate and store salary data
        # salary_instance = Salary()
        salary_data = self.calculate_and_return_salary_breakdowns()

        with open("salary.json", "w", encoding="utf-8") as json_file:
            json.dump(salary_data, json_file, indent=4)

    def calculate_employee_salary(self, salary):
        """Calculate the total salary breakdown of the employee per year"""
        annual_salary = salary
        annual_allowance = self.get_allowance() * salary / 100
        annual_bonus = self.get_bonus() * salary / 100
        annual_deductions = self.get_deductions() * salary / 100
        
        total_salary = annual_salary + annual_allowance + annual_bonus - annual_deductions
        
        salary_breakdown = {
            'base_salary_yearly': annual_salary,
            'allowance_yearly': annual_allowance,
            'bonus_yearly': annual_bonus,
            'deductions_yearly': annual_deductions,
            'net_pay_yearly': total_salary
        }
        return salary_breakdown
    
    def calculate_monthly_salary(self, salary):
        # ADD: handle internship monthly salary differently
        """Calculate monthly net salary."""
        yearly_breakdown = self.calculate_employee_salary(salary)
        monthly_base_salary = yearly_breakdown['base_salary_yearly'] / 12
        total_allowance = yearly_breakdown['allowance_yearly'] / 12
        total_bonus = yearly_breakdown['bonus_yearly'] / 12
        total_deductions = yearly_breakdown['net_pay_yearly'] / 12

        net_pay = monthly_base_salary + total_allowance + total_bonus - total_deductions

        salary_breakdown = {
            'base_salary_monthly': monthly_base_salary,
            'allowance_monthly': total_allowance,
            'bonus_monthly': total_bonus,
            'deductions_monthly': total_deductions,
            'net_pay_monthly': net_pay
        }
        return salary_breakdown
    
    def calculate_and_return_salary_breakdowns(self):
        """Calculate and return yearly and monthly salary breakdowns for each employee.
        Returns a list of dictionaries with the specified structure."""
        employee_data = DataSerializer().deserialize_employees_from_json()
        
        salary_results = {}

        for employee_id, employee_info in employee_data.items():
            full_name = employee_info.get("full_name")
            employee_salary = employee_info.get("salary")

            yearly_breakdown = self.calculate_employee_salary(employee_salary)
            monthly_breakdown = self.calculate_monthly_salary(employee_salary)

            result_dict = {
                'employee_id': employee_id,
                'full_name': full_name,
                'base_salary_yearly': yearly_breakdown['base_salary_yearly'],
                'allowance_yearly': yearly_breakdown['allowance_yearly'],
                'bonus_yearly': yearly_breakdown['bonus_yearly'],
                'deductions_yearly': yearly_breakdown['deductions_yearly'],
                'net_pay_yearly': yearly_breakdown['net_pay_yearly'],
                'base_salary_monthly': monthly_breakdown['base_salary_monthly'],
                'allowance_monthly': monthly_breakdown['allowance_monthly'],
                'bonus_monthly': monthly_breakdown['bonus_monthly'],
                'deductions_monthly': monthly_breakdown['deductions_monthly'],
                'net_pay_monthly': monthly_breakdown['net_pay_monthly']
            }
            salary_results[employee_id] = result_dict

        return salary_results
    
    def get_bonus(self):
        """Getter for bonus"""
        return self.__bonus

    def get_deductions(self):
        """Getter for bonus"""
        return self.__deductions

    def get_allowance(self):
        """Getter for bonus"""
        return self.__allowance

salary_instances = Salary(deductions=10, allowance=5, bonus=2)

