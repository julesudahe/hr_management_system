"""AndrewID: judahemu & juwizeyi"""

import json
from datetime import datetime, time
from employee import Employee
from deserializer import DataDeserializer
from attendance import Attendance
from salary import Salary

class EmployeeManagement:
    """Initialize empty dictionaries to store employee objects, attendance, and salary information"""
        
    def __init__(self):
        """Initialize dictionaries to store employee objects, attendance, and salary information"""
        self.employees = {}

    def _save_to_json(self, employee_data):
        """Save the employee data to the JSON file."""
        with open("1. employees.json", "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)
    
    def add_employee(self, first_name, last_name, serial_id, employee_gender, salary, job_title, level, team=None, department=None, internship_duration=None):
        """Create an Employee object and add it to the employees dictionary"""
        try:
            Employee(first_name, last_name, serial_id, employee_gender, salary, job_title, level, team, department, internship_duration)
            Employee.store_employees_to_json(Employee.all_employees)

        except ValueError as e:
            print(e)
            
    def delete_employee(self, target_employee_id):
        """Delete an employee's information from the JSON file."""
        data_deserializer = DataDeserializer()
        employee_data = data_deserializer.deserialize_employees_from_json()

        removed_employees = [employee_info for employee_info in employee_data if target_employee_id in employee_info.keys()]
        employee_data = [employee_info for employee_info in employee_data if target_employee_id not in employee_info.keys()]

        if removed_employees:
            self._save_to_json(employee_data)
            print(f"Employee with ID {target_employee_id} deleted.")
        else:
            print("Employee not found. Available IDs:", [list(record.keys())[0] for record in employee_data])

    def get_employee_count(self):
        """Return the number of employees in the management system"""
        return len(self.employees)
    
    def update_data(self):
        """Update existing employee data with new data."""
        data_deserializer = DataDeserializer()
        existing_data = data_deserializer.deserialize_employees_from_json()

        updated_existing = False

        while True:
            employee_id = input("Enter the Employee ID to update (or X to quit): ")
            
            if employee_id.lower() == "x": #condition to stop the system from running unending loop
                break

            # Check if the entered employee_id exists in the data
            if any(employee_id in entry for entry in existing_data):
                for entry in existing_data:
                    if employee_id in entry:
                        employee_data = entry[employee_id]
                        print(f"Current Information for Employee ID {employee_id}:")
                        print(employee_data)

                        field_to_update = input("Enter the field to update: ").strip().lower()

                        # Validate if the field to update exists in employee_data
                        if field_to_update in employee_data:
                            new_value = input(f"Enter the new value for {field_to_update}: ")
                            employee_data[field_to_update] = new_value
                            updated_existing = True
                        else:
                            print(f"Invalid field: {field_to_update}. Please enter a valid field name.")

                        break
            else:
                print(f"Invalid Employee ID: {employee_id}. Please enter a valid Employee ID.")
                continue

            self._save_to_json(existing_data)

            if not updated_existing:
                print(f"No employee found with ID: {employee_id}")

            return existing_data

    def calculate_salary_for_employee_all(self):
        """Create an Employee object and add it to the employees dictionary"""
        Salary(30, 20, 10)

    def hr_record_in_time(self, employee_id, date, in_time):
        """Recording attendance"""
        attendance_instance = Attendance()
        attendance_instance.record_in_time(employee_id, date, in_time)
        attendance_instance.store_attendance_to_json()

    def hr_record_out_time(self, employee_id, date, out_time):
        """Recording attendance"""
        data_deserializer = DataDeserializer()
        existing_data = data_deserializer.deserialize_attendance_from_json()
        
        # Check if the employee_id exists in the attendance data
        employee_found = False
        for record in existing_data:
            if employee_id in record:
                attendance_records = record[employee_id]
                # Assuming there's only one attendance record for each employee on a specific date
                for attendance_record in attendance_records:
                    if attendance_record['date'] == date:
                        attendance_record['out_time'] = out_time
                        current_time = datetime.strptime(out_time, "%H:%M").time()
                        attendance_record['is_early_departure'] = current_time < time(17, 0)
                        employee_found = True
                        break
                if employee_found:
                    break

        if employee_found:
            with open("2. attendance.json", "w", encoding="utf-8") as updated_file:
                json.dump(existing_data, updated_file, indent=4)
        else:
            print(f"Employee with ID {employee_id} not found in attendance records for the given date.")

    def generate_attendance_summary_report(self, start_date, end_date):
        """Calculating attendance for the specified time period"""
        data_deserializer = DataDeserializer()
        attendance_records = data_deserializer.deserialize_attendance_from_json()

        # Print table header
        print(f"{'Employee ID':<15}{'Full Name':<25}{'Team':<20}{'Total Hours Worked':<20}{'Early Arrivals':<20}{'Late Arrivals':<20}")
        print("=" * 110)

        for employee_data in attendance_records:
            _, attendances = next(iter(employee_data.items()))

            total_hours = 0
            total_minutes = 0
            early_count = 0
            late_count = 0

            for data in attendances:
                if start_date <= data['date'] <= end_date:
                    employee_id = data['employee_id']  # Assuming only one set of employee info per period
                    full_name = data['full_name']
                    team = data['team']
                    in_time = data['in_time']
                    current_time = datetime.now().strftime("%H:%M")
                    out_time = data['out_time'] if data['out_time'] is not None else current_time
                    is_early = data['is_late']
                    is_late = data['is_early_departure']

                    # Convert in_time and out_time to datetime objects for easier calculations
                    in_time_obj = datetime.strptime(in_time, "%H:%M")
                    out_time_obj = datetime.strptime(out_time, "%H:%M")
                    duration = out_time_obj - in_time_obj
                    total_hours += duration.seconds // 3600
                    total_minutes += (duration.seconds // 60) % 60

                    # Update early and late counts
                    if is_early is True:
                        early_count += 1
                    if is_late is True:
                        late_count += 1

                    total_hours += total_minutes // 60
                    total_minutes %= 60

                    # Print attendance summary in tabular format
                    print(f"{employee_id:<15}{full_name:<25}{team:<20}{total_hours}h {total_minutes:<18}{early_count:<20}{late_count:<20}")

    def show_employee_info(self, employee_id):
        """Display the employee information for the specified employee ID."""
        data_deserializer = DataDeserializer()
        employee_data = data_deserializer.deserialize_employees_from_json()

        for employee_record in employee_data:
            if employee_id in employee_record:
                employee_info = employee_record[employee_id]
                full_name = employee_info.get("full_name")
                email = employee_info.get("email")
                job_title = employee_info.get("job_title")
                gender = employee_info.get("gender")
                salary = employee_info.get("salary")
                level = employee_info.get("level")
                team = employee_info.get("team")
                department = employee_info.get("department")
                internship_duration = employee_info.get("internship_duration_months")

                # Display employee information
                print(f"Employee ID: {employee_id}")
                print(f"Full Name: {full_name}")
                print(f"Email: {email}")
                print(f"Job Title: {job_title}")
                print(f"Gender: {gender}")
                print(f"Salary: {int(salary):.2f}")

                if level.lower() == "director":
                    print(f"Department: {department}")
                elif level.lower() in ["manager", "employee"]:
                    print(f"Department: {department}")
                    print(f"Team: {team}")
                elif level.lower() == "intern":
                    print(f"Department: {department}")
                    print(f"Team: {team}")
                    print(f"Internship Duration (Months): {internship_duration}")
                break
        else:
            print(f"No information found for Employee ID: {employee_id}")

    def show_attendance_info(self, employee_id, date):
        """Display attendance data for the specified employee ID."""
        data_deserializer = DataDeserializer()
        attendance_data = data_deserializer.deserialize_attendance_from_json()
        
        for record in attendance_data:
            if employee_id in record:
                attendance_records = record[employee_id]
                print(f"Attendance records for Employee ID: {employee_id}")
                for attendance_record in attendance_records:
                    if date == attendance_record['date']:
                        print(f"Date: {attendance_record['date']}")
                        print(f"In Time: {attendance_record['in_time']}")
                        print(f"Is Late: {attendance_record['is_late']}")
                        print(f"Out Time: {attendance_record['out_time']}")
                        print(f"Is Early Departure: {attendance_record['is_early_departure']}")
                        print("-" * 30)
                    else:
                        print(f"No attendance records for {employee_id} on this date {date}")
                break
        else:
            print(f"No attendance records found for Employee ID: {employee_id}")

    def show_team_attendance_info(self, team_name):
        """Display attendance data for the specified employee ID."""
        data_deserializer = DataDeserializer()
        attendance_data = data_deserializer.deserialize_attendance_from_json()

        print(f"Attendance records for Team: {team_name}")
        print("=" * 50)
        for employee_record in attendance_data:
            _, employee_info = next(iter(employee_record.items()))
            
            for data in employee_info:
                if data['team'] == team_name:
                    print(f"Employee ID: {data['employee_id']}")
                    print(f"Full Name: {data['full_name']}")
                    print(f"Team: {data['team']}")
                    print(f"Date: {data['date']}")
                    print(f"In Time: {data['in_time']}")
                    print(f"Is Late: {data['is_late']}")
                    print(f"Out Time: {data['out_time']}")
                    print(f"Is Early Departure: {data['is_early_departure']}")
            print("=" * 50)


    def show_salary_info(self, employee_id):
        """Display the calculated salary breakdown for the specified employee ID."""
        data_deserializer = DataDeserializer()
        salary_data = data_deserializer.deserialize_salary_from_json()
        self.calculate_salary_for_employee_all()

        if employee_id in salary_data:
            employee_info = salary_data[employee_id]
            full_name = employee_info.get("full_name")
            base_salary = employee_info.get("base_salary_monthly")
            allowance = employee_info.get("allowance_monthly")
            bonus = employee_info.get("bonus_monthly")
            deductions = employee_info.get("deductions_monthly")
            net_pay = employee_info.get("net_pay_monthly")
            current_month = employee_info.get("current_month")

            print(f"Employee ID: {employee_id}")
            print(f"Month: {current_month}")
            print(f"Full Name: {full_name}")
            print(f"Base Salary: {base_salary:.2f}")
            print(f"Allowance: {allowance:.2f}")
            print(f"Bonus: {bonus:.2f}")
            print(f"Deductions: {deductions:.2f}")
            print(f"Net Pay: {net_pay:.2f}")
        else:
            print(f"No salary information found for Employee ID: {employee_id}")
    
    def generate_and_save_payslip(self, employee_id, month_year):
        """Generate and save payslip for the specified employee ID and month-year."""
        
        self.calculate_salary_for_employee_all()
        data_deserializer = DataDeserializer()
        salary_data = data_deserializer.deserialize_salary_from_json()
        
        # Validate if the specified employee ID exists in the salary data
        if employee_id in salary_data:
            employee_info = salary_data[employee_id]
            full_name = employee_info.get("full_name")
            base_salary = employee_info.get("base_salary_monthly")
            allowance = employee_info.get("allowance_monthly")
            bonus = employee_info.get("bonus_monthly")
            deductions = employee_info.get("deductions_monthly")
            net_pay = employee_info.get("net_pay_monthly")

            # Parse month and year from the input (assuming it is in the format "MM-YYYY")
            try:
                month, year = map(int, month_year.split('-'))
                pay_period_start = datetime(year, month, 1)
                pay_period_end = datetime(year, month % 12 + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
            except ValueError:
                print("Invalid month-year format. Please use the format MM-YYYY.")
                return

            # Create payslip content
            payslip_content = f"{'*' * 30}\n"
            payslip_content += f"{'Payslip'.center(30)}\n"
            payslip_content += f"{'*' * 30}\n"
            payslip_content += f"Pay Period: {pay_period_start.strftime('%Y-%m-%d')} to {pay_period_end.strftime('%Y-%m-%d')}\n"
            payslip_content += f"Employee ID: {employee_id}\n"
            payslip_content += f"Full Name: {full_name}\n"
            payslip_content += f"Month/Year: {month_year}\n"
            payslip_content += "-" * 30 + "\n"
            payslip_content += f"Base Salary: ${base_salary:.2f}\n"
            payslip_content += f"Allowance: ${allowance:.2f}\n"
            payslip_content += f"Bonus: ${bonus:.2f}\n"
            payslip_content += f"Deductions: ${deductions:.2f}\n"
            payslip_content += f"Net Pay: ${net_pay:.2f}\n"
            payslip_content += f"{'*' * 30}\n"

            # Save payslip to text file
            payslip_filename = f"4. {full_name}.txt"
            with open(payslip_filename, "w", encoding="utf-8") as payslip_file:
                payslip_file.write(payslip_content)


            print(f"Payslip for Employee ID {employee_id} generated and saved to {payslip_filename}.")
        else:
            print(f"No salary information found for Employee ID: {employee_id}")
