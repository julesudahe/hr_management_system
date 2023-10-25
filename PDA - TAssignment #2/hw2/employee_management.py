"""AndrewID: judahemu"""

from employee import Employee
from attendance import Attendance
from salary import Salary

class HRMIS:
    """Initialize empty dictionaries to store employee objects, attendance, and salary information"""
        
    def __init__(self):
        """Initialize empty dictionaries to store employee objects, attendance, and salary information"""
        self.employees = {}
        self.attendance_system = Attendance
        self.salary_system = Salary
    
    def add_employee(self, first_name, last_name, employee_gender, salary, deductions=0.0, allowance=0.0, bonus=0.0):
        """Create an Employee object and add it to the employees dictionary"""
        new_employee = Employee(first_name, last_name, employee_gender, salary)
        self.employees[new_employee.get_employee_id()] = new_employee

        # Add the employee to the attendance and salary systems
        self.attendance_system.add_employee(first_name, last_name, employee_gender, salary)
        self.salary_system.add_employee(first_name, last_name, employee_gender, salary, deductions, allowance, bonus)

    def get_employee_info(self, employee_id):
        """Retrieve and display employee information"""
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            employee.show_employee_info()
        else:
            print("Employee not found.")

    def record_in_time(self, employee_id, is_late=False):
        """Record employee in-time using the attendance system"""
        self.attendance_system.record_in_time(employee_id, is_late)

    def record_out_time(self, employee_id, is_early_departure=False):
        """Record employee out-time using the attendance system"""
        self.attendance_system.record_out_time(employee_id, is_early_departure)

    def apply_for_leave(self, employee_id, leave_type, start_date, end_date):
        """Apply for leave using the attendance system"""
        return self.attendance_system.apply_for_leave(employee_id, leave_type, start_date, end_date)

    def calculate_employee_salary(self, employee_id):
        """Calculate and display employee salary using the salary system"""
        if employee_id in self.employees:
            salary_breakdown = self.salary_system.calculate_employee_salary(employee_id)
            print("Salary Breakdown:")
            for category, amount in salary_breakdown.items():
                print(f"{category}: {amount:.2f}")
        else:
            print("Employee not found.")
