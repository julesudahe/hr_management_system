"""AndrewID: judahemu & Jeannette"""

# Importing the Employee class from employee.py file (saved in the path as this file)
# import os
import json
from deserializer import DataDeserializer

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
## handling missing employee_id
## handling intern salary
## error message when json for employee is empty or missing.

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
        """Calculate and store monthly salary data to a JSON file."""
        employee_data = DataDeserializer().deserialize_employees_from_json()
        salary_results = {}

        for employee_dict in employee_data:
            employee_id, employee_info = list(employee_dict.items())[0]
            full_name = employee_info.get("full_name")
            employee_salary = employee_info.get("salary")

            monthly_breakdown = self.calculate_monthly_salary(employee_salary)
            
            result_dict = {
                'employee_id': employee_id,
                'full_name': full_name,
                'base_salary_monthly': round(monthly_breakdown['base_salary_monthly'], 2),
                'allowance_monthly': round(monthly_breakdown['allowance_monthly'], 2),
                'bonus_monthly': round(monthly_breakdown['bonus_monthly'], 2),
                'deductions_monthly': round(monthly_breakdown['deductions_monthly'], 2),
                'net_pay_monthly': round(monthly_breakdown['net_pay_monthly'], 2)
            }
            salary_results[employee_id] = result_dict

        with open("salary.json", "w", encoding="utf-8") as json_file:
            json.dump(salary_results, json_file, indent=4)

    def calculate_monthly_salary(self, salary):
        """Calculate monthly net salary."""
        monthly_base_salary = int(salary) / 12
        total_allowance = self.get_allowance() * monthly_base_salary / 100
        total_bonus = self.get_bonus() * monthly_base_salary / 100
        total_deductions = self.get_deductions() * monthly_base_salary / 100

        net_pay = monthly_base_salary + total_allowance + total_bonus - total_deductions

        salary_breakdown = {
            'base_salary_monthly': monthly_base_salary,
            'allowance_monthly': total_allowance,
            'bonus_monthly': total_bonus,
            'deductions_monthly': total_deductions,
            'net_pay_monthly': net_pay
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

    def display_salary_breakdown(self, employee_id):
        """Display the calculated salary breakdown for the specified employee ID."""
        with open("salary.json", "r", encoding="utf-8") as json_file:
            salary_data = json.load(json_file)

        if employee_id in salary_data:
            employee_info = salary_data[employee_id]
            full_name = employee_info.get("full_name")
            base_salary = employee_info.get("base_salary_monthly")
            allowance = employee_info.get("allowance_monthly")
            bonus = employee_info.get("bonus_monthly")
            deductions = employee_info.get("deductions_monthly")
            net_pay = employee_info.get("net_pay_monthly")

            print(f"Employee ID: {employee_id}")
            print(f"Full Name: {full_name}")
            print(f"Base Salary: {base_salary:.2f}")
            print(f"Allowance: {allowance:.2f}")
            print(f"Bonus: {bonus:.2f}")
            print(f"Deductions: {deductions:.2f}")
            print(f"Net Pay: {net_pay:.2f}")
        else:
            print(f"No salary information found for Employee ID: {employee_id}")


# salary_instances = Salary(deductions=10, allowance=20, bonus=2)
# employee_id_to_display = "CMUID0001"
# salary_instances.display_salary_breakdown(employee_id_to_display)

