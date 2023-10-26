from emplolyee import Employee

class Salary:
    def __init__(self, base_salary, deductions=0, allowances=0, bonuses=0):
        self.base_salary = base_salary
        self.deductions = deductions
        self.allowances = allowances
        self.bonuses = bonuses
    
    def calculate_net_salary(self):
        """
        Calculate and return the net salary after adding allowances and bonuses, and subtracting deductions.
        """
        return self.base_salary + self.allowances + self.bonuses - self.deductions

    def display_salary_details(self):
        print(f"Base Salary: ${self.base_salary}")
        print(f"Deductions: ${self.deductions}")
        print(f"Allowances: ${self.allowances}")
        print(f"Bonuses: ${self.bonuses}")
        print(f"Net Salary: ${self.calculate_net_salary()}")

# Example usage:
employee_salary = Salary(50000, deductions=5000, allowances=3000, bonuses=2000)
employee_salary.display_salary_details()