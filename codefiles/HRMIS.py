from emplolyee import Employee
from attendance import Attendance
from salary import Salary
import pickle


class HRMIS:
    def __init__(self):
        self.employees = {}  # key: employee_id, value: Employee object
        self.attendance_records = {}  # key: (employee_id, date), value: Attendance object
        self.salaries = {}  # key: employee_id, value: Salary object
    
    def add_employee(self, employee_id, first_name, last_name, email, salary):
        if employee_id in self.employees:
            print(f"An employee with ID: {employee_id} already exists.")
            return
        self.employees[employee_id] = Employee(employee_id, first_name, last_name, email, salary)
        self.salaries[employee_id] = Salary(salary)
        print(f"Added records for employee ID: {employee_id}")

    def update_employee(self, employee_id, first_name=None, last_name=None, email=None, salary=None):
        if employee_id not in self.employees:
            print(f"No employee found with ID: {employee_id}")
            return
        employee = self.employees[employee_id]
        if first_name:
            employee.first_name = first_name
        if last_name:
            employee.last_name = last_name
        if email:
            employee.email = email
        if salary:
            employee.salary = salary
            self.salaries[employee_id].base_salary = salary  # update salary object as well
        print(f"Updated records for employee ID: {employee_id}")

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            
            # Delete salary details of the employee
            if employee_id in self.salaries:
                del self.salaries[employee_id]
            
            # Delete all attendance records of the employee
            for key in list(self.attendance_records.keys()):
                if key[0] == employee_id:
                    del self.attendance_records[key]
            print(f"Deleted records for employee ID: {employee_id}")
        else:
            print(f"No employee found with ID: {employee_id}")
    
    def record_attendance(self, employee_id, date, in_time, out_time):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            self.attendance_records[(employee_id, date)] = Attendance(employee_id, employee.first_name, employee.last_name, employee.email, employee.salary, date, in_time, out_time)
        else:
            print(f"No employee found with ID: {employee_id}")
    
    def update_salary(self, employee_id, deductions=0, allowances=0, bonuses=0):
        if employee_id in self.salaries:
            salary = self.salaries[employee_id]
            salary.deductions = deductions
            salary.allowances = allowances
            salary.bonuses = bonuses
        else:
            print(f"No salary record found for employee ID: {employee_id}")

    def display_employee_info(self, employee_id):
        if employee_id in self.employees:
            self.employees[employee_id].display_employee_info()
        else:
            print(f"No employee found with ID: {employee_id}")

    def display_employee_attendance(self, employee_id, date):
        key = (employee_id, date)
        if key in self.attendance_records:
            self.attendance_records[key].display_attendance()
        else:
            print(f"No attendance record found for employee ID: {employee_id} on {date}")

    def display_employee_salary(self, employee_id):
        if employee_id in self.salaries:
            self.salaries[employee_id].display_salary_details()
        else:
            print(f"No salary record found for employee ID: {employee_id}")

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            
            # Delete salary details of the employee
            if employee_id in self.salaries:
                del self.salaries[employee_id]
            
            # Delete all attendance records of the employee
            for key in list(self.attendance_records.keys()):
                if key[0] == employee_id:
                    del self.attendance_records[key]
                    
            print(f"Deleted records for employee ID: {employee_id}")
        else:
            print(f"No employee found with ID: {employee_id}")

    def record_attendance(self, employee_id, date, in_time, out_time):
        if employee_id not in self.employees:
            print(f"No employee found with ID: {employee_id}")
            return
        
        employee = self.employees[employee_id]
        attendance = Attendance(employee_id, employee.first_name, employee.last_name, employee.email, employee.salary, date, in_time, out_time)
        
        # Store multiple attendance records for each employee
        if employee_id not in self.attendance_records:
            self.attendance_records[employee_id] = []
        self.attendance_records[employee_id].append(attendance)

    def display_attendance_for_employees(self, employee_id):
        if employee_id not in self.attendance_records:
            print(f"No attendance records found for employee ID: {employee_id}")
            return

        for attendance in self.attendance_records[employee_id]:
            attendance.display_attendance()

    def display_attendance_for_all_employees(self):
        for employee_id, attendances in self.attendance_records.items():
            print(f"\nEmployee ID: {employee_id}")
            for attendance in attendances:
                attendance.display_attendance()

    def calculate_total_working_hours(self, employee_id, start_date=None, end_date=None):
        if employee_id not in self.attendance_records:
            print(f"No attendance records found for employee ID: {employee_id}")
            return

        total_hours = 0
        total_minutes = 0
        for attendance in self.attendance_records[employee_id]:
            if (start_date and attendance.date < start_date) or (end_date and attendance.date > end_date):
                continue  # Skip attendance records outside the date range
            hours, minutes = map(int, attendance.duration().split()[:2:2])  # split 'X hours, Y minutes' and take X and Y
            total_hours += hours
            total_minutes += minutes
            total_hours += total_minutes // 60  # Convert every 60 minutes into 1 hour
            total_minutes %= 60

        return f"{total_hours} hours, {total_minutes} minutes"
    
    
    def generate_employee_list_report(self):
        print("Employee List Report:")
        print("==================================")
        for employee_id, employee in self.employees.items():
            employee.display_employee_info()
            print("----------------------------------")

    def generate_attendance_summary_report(self, month_year):
        # Assuming month_year is in the format 'YYYY-MM'
        print(f"Attendance Summary Report for {month_year}:")
        print("============================================")
        for employee_id, attendances in self.attendance_records.items():
            filtered_attendances = [a for a in attendances if a.date.startswith(month_year)]
            if filtered_attendances:
                print(f"Employee ID: {employee_id}")
                total_hours = 0
                total_minutes = 0
                for attendance in filtered_attendances:
                    attendance.display_attendance()
                    hours, minutes = map(int, attendance.duration().split()[:2:2])
                    total_hours += hours
                    total_minutes += minutes

                total_hours += total_minutes // 60
                total_minutes %= 60
                print(f"Total hours worked in {month_year}: {total_hours} hours, {total_minutes} minutes")
                print("----------------------------------")

    def generate_salary_summary_report(self, month_year):
        # Assuming month_year is in the format 'YYYY-MM'
        print(f"Salary Summary Report for {month_year}:")
        print("=======================================")
        for employee_id, salary in self.salaries.items():
            employee = self.employees[employee_id]
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee.first_name} {employee.last_name}")
            print(f"Base Salary: ${salary.base_salary}")
            total_deductions = sum(salary.deductions)
            total_allowances = sum(salary.allowances)
            total_bonuses = sum(salary.bonuses)
            print(f"Total Deductions: ${total_deductions}")
            print(f"Total Allowances: ${total_allowances}")
            print(f"Total Bonuses: ${total_bonuses}")
            net_salary = salary.base_salary + total_allowances + total_bonuses - total_deductions
            print(f"Net Salary for {month_year}: ${net_salary}")
            print("----------------------------------")
    
    def save_data(self):
        with open('employees.pkl', 'wb') as f:
            pickle.dump(self.employees, f)

        with open('attendance_records.pkl', 'wb') as f:
            pickle.dump(self.attendance_records, f)

        with open('salaries.pkl', 'wb') as f:
            pickle.dump(self.salaries, f)

    # Load data from files
    def load_data(self):
        try:
            with open('employees.pkl', 'rb') as f:
                self.employees = pickle.load(f)
        except FileNotFoundError:
            self.employees = {}

        try:
            with open('attendance_records.pkl', 'rb') as f:
                self.attendance_records = pickle.load(f)
        except FileNotFoundError:
            self.attendance_records = {}

        try:
            with open('salaries.pkl', 'rb') as f:
                self.salaries = pickle.load(f)
        except FileNotFoundError:
            self.salaries = {}

    def generate_pay_slip(self, employee_id, month_year):
        # Assuming month_year is in the format 'YYYY-MM'
        if employee_id not in self.salaries:
            print(f"No salary information found for employee ID: {employee_id}")
            return

        salary = self.salaries[employee_id]
        employee = self.employees[employee_id]

        pay_slip = f"Pay Slip for {employee.first_name} {employee.last_name} - {month_year}\n"
        pay_slip += f"Employee ID: {employee_id}\n"
        pay_slip += f"Base Salary: ${salary.base_salary}\n"
        total_deductions = sum(salary.deductions)
        total_allowances = sum(salary.allowances)
        total_bonuses = sum(salary.bonuses)
        pay_slip += f"Total Deductions: ${total_deductions}\n"
        pay_slip += f"Total Allowances: ${total_allowances}\n"
        pay_slip += f"Total Bonuses: ${total_bonuses}\n"
        net_salary = salary.base_salary + total_allowances + total_bonuses - total_deductions
        pay_slip += f"Net Salary for {month_year}: ${net_salary}\n"

        with open(f"{employee_id}.txt", "w") as file:
            file.write(pay_slip)


# Example usage:
# hr_system = HRMIS()
# hr_system.add_employee(101, 'John', 'Doe', 'john@example.com', 50000)
# hr_system.record_attendance(101, '2023-10-24', '09:00', '17:00')
# hr_system.update_salary(101, deductions=1000, allowances=2000, bonuses=500)

# hr_system.display_employee_info(101)
# hr_system.display_employee_attendance(101, '2023-10-24')
# hr_system.display_employee_salary(101)

# hr_system.delete_employee(101)
# hr_system.display_employee_info(101)  # This should now say the employee is not found

hr_system = HRMIS()
hr_system.add_employee(101, 'John', 'Doe', 'john@example.com', 50000)  # Add an employee
hr_system.update_employee(101, first_name='Jonathan', email='jonathan@example.com')  # Update employee details
hr_system.display_employee_info(101)
hr_system.delete_employee(101)
hr_system.display_employee_info(101)  # This should now say the employee is not found