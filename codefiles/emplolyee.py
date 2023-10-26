import numpy as np

class Employee:
    def __init__(self, employee_id, first_name, last_name, email, salary):

        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Annual Salary: ${self.salary}")
    
    def earnings(self):
        """
        Calculate and return the earnings for the employee. 
        This method should be overridden in derived classes for role-specific earnings calculations.
        """
        return self.salary
    
# Test the Employee class with a sample manager
employee1 = Employee(3, "Carol", "Mutesi", "carol.mute@gmail.com", 70000)
employee1.display_employee_info()
print(f"The earning for this employee is: ${employee1.earnings()}")