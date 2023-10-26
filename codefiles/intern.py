from emplolyee import Employee
class Intern(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, university_name, program_name, duration):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.university_name = university_name
        self.program_name = program_name
        self.duration = max(3, min(duration, 6))  # Ensure the duration is between 3 and 6 months
        
    def display_employee_info(self):
        super().display_employee_info()
        print(f"University: {self.university_name}")
        print(f"Program: {self.program_name}")
        print(f"Internship Duration: {self.duration} months")
        
    def earnings(self):
        """
        Override the earnings method to calculate earnings based on internship duration.
        """
        return self.salary * (self.duration / 12)


# Test the Intern class with a sample intern
intern = Intern(5, "Ella", "James", "ella.james@gmail.com", 30000, "CMU_Africa", "MSEAI", 5)
intern.display_employee_info()
print(f"Earnings for the internship duration: ${intern.earnings():.2f}")
