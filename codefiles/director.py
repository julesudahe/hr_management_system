import numpy as np

from emplolyee import Employee

class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, bonus):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.department = department
        self.bonus = bonus
        
    def display_employee_info(self):
        super().display_employee_info()
        print(f"Department: {self.department}")
        print(f"Annual Bonus: ${self.bonus}")
        
    def earnings(self):
        """
        Override the earnings method to include an annual bonus for directors.
        """
        return self.salary + self.bonus


# Test the Director class
director = Director(4, "David", "Mugisha", "david.mg@gmail.com", 90000, "IT", 20000)
director.display_employee_info()
print(f"Director Earnings including annual bonus: ${director.earnings()}")
