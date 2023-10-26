from emplolyee import Employee
import numpy as np

class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, depart_name, num_reports, rate):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.depart_name = depart_name
        self.num_reports = num_reports
        self.rate = rate

    def display_employee_info(self):
        super().display_employee_info()
        print(f"Department: {self.depart_name}")
        print(f"Number of Direct Reports: {self.num_reports}")
        print(f"Management Support Allowance Rate: {self.rate * 100}%")

    def earnings(self):
        if self.rate > 0.6:
            print("The rate can not be greater than 60%")
        else:
            return (self.salary + (self.rate * self.salary))

# Test the Manager class with a sample manager
manager = Manager(3, "Carol", "Ishimwe", "carol.ishimw@gmail.com", 70000, "Sales", 5, 0.5)
manager.display_employee_info()
print(f"Earnings for manager including support allowance: ${manager.earnings()}")