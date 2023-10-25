"""AndrewID: judahemu"""

class HumanResourceMaster:
    def __init__(self):
        self.employees = []
        self.attendance_records = []
        self.salary_records = []

    def add_employee(self, emp_id, name, role):
        employee = Employee(emp_id, name, role)
        self.employees.append(employee)

    def add_attendance(self, emp_id, date, in_time, out_time):
        attendance = Attendance(emp_id, date, in_time, out_time)
        self.attendance_records.append(attendance)

    def add_salary_info(self, emp_id, base_salary, deductions, allowances, bonuses):
        salary = Salary(emp_id, base_salary, deductions, allowances, bonuses)
        self.salary_records.append(salary)

    def calculate_employee_salary(self, emp_id):
        for salary_record in self.salary_records:
            if salary_record.emp_id == emp_id:
                return salary_record.calculate_salary()
        return None
