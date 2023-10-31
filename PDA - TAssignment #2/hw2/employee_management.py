"""AndrewID: judahemu & Jeannette"""

import json
from datetime import datetime, time
from employee import Employee
from deserializer import DataDeserializer
from attendance import Attendance

class EmployeeManagement:
    """Initialize empty dictionaries to store employee objects, attendance, and salary information"""
        
    def __init__(self):
        """Initialize dictionaries to store employee objects, attendance, and salary information"""
        self.employees = {}

    def _save_to_json(self, employee_data):
        """Save the employee data to the JSON file."""
        with open("employees.json", "w", encoding="utf-8") as json_file:
            json.dump(employee_data, json_file, indent=4)
    
    def add_employee(self, first_name, last_name, serial_id, employee_gender, salary, job_title, level, team=None, department=None, internship_duration=None):
        """Create an Employee object and add it to the employees dictionary"""
        Employee(first_name, last_name, serial_id, employee_gender, salary, job_title, level, team, department, internship_duration)

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
    
    def update_data(self):
        """Update existing employee data with new data."""
        data_deserializer = DataDeserializer()
        existing_data = data_deserializer.deserialize_employees_from_json()

        employee_id = input("Enter the Employee ID to update: ")

        for entry in existing_data:
            if employee_id in entry:
                employee_data = entry[employee_id]
                print(f"Current Information for Employee ID {employee_id}:")
                print(employee_data)

                field_to_update = input("Enter the field to update: ").strip().lower()
                new_value = input(f"Enter the new value for {field_to_update}: ")

                employee_data[field_to_update] = new_value

                updated_existing = True
                break

        self._save_to_json(existing_data)
        
        if not updated_existing:
            print(f"No employee found with ID: {employee_id}")

        return existing_data

    def hr_record_in_time(self, employee_id, date, in_time):
        """Recording attendance"""
        attendance_instance = Attendance()
        attendance_instance.record_in_time(employee_id, date, in_time)
        attendance_instance.store_attendance_to_json()

    def hr_record_out_time(self, employee_id, date, out_time):
        """Recording attendance"""
        data_deserializer = DataDeserializer()
        existing_data = data_deserializer.deserialize_attendance_from_json()

        print("Existing Data:", existing_data)
        # print(existing_data.get('employee_id'))

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
            with open("attendance.json", "w", encoding="utf-8") as updated_file:
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
            employee_id, attendances = next(iter(employee_data.items()))
            filtered_attendances = [a for a in attendances if start_date <= a['date'] <= end_date]
            if filtered_attendances:
                employee_info = filtered_attendances[0]  # Assuming only one set of employee info per period
                full_name = employee_info['full_name']
                team = employee_info['team']

                total_hours = 0
                total_minutes = 0
                early_count = 0
                late_count = 0

                for attendance in filtered_attendances:
                    in_time = attendance['in_time']
                    out_time = attendance['out_time']
                    is_early = attendance['is_late']
                    is_late = attendance['is_early_departure']

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
                print(f"Salary: {salary:.2f}")

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

    def show_attendance_info(self, employee_id):
        """Display attendance data for the specified employee ID."""
        data_deserializer = DataDeserializer()
        attendance_data = data_deserializer.deserialize_attendance_from_json()
        
        for record in attendance_data:
            if employee_id in record:
                attendance_records = record[employee_id]
                print(f"Attendance records for Employee ID: {employee_id}")
                for attendance_record in attendance_records:
                    print(f"Date: {attendance_record['date']}")
                    print(f"In Time: {attendance_record['in_time']}")
                    print(f"Is Late: {attendance_record['is_late']}")
                    print(f"Out Time: {attendance_record['out_time']}")
                    print(f"Is Early Departure: {attendance_record['is_early_departure']}")
                    print("-" * 30)
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
    
    def generate_and_save_payslip(self, employee_id, month_year):
        """Generate and save payslip for the specified employee ID and month-year."""
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
            payslip_content = "Payslip\n"
            payslip_content += f"Pay Period: {pay_period_start} to {pay_period_end}\n"
            payslip_content += "Employee ID: " + employee_id + "\n"
            payslip_content += "Full Name: " + full_name + "\n"
            payslip_content += "Month/Year: " + month_year + "\n"
            payslip_content += "---------------------------\n"
            payslip_content += "Base Salary: $" + str(base_salary) + "\n"
            payslip_content += "Allowance: $" + str(allowance) + "\n"
            payslip_content += "Bonus: $" + str(bonus) + "\n"
            payslip_content += "Deductions: $" + str(deductions) + "\n"
            payslip_content += "Net Pay: $" + str(net_pay) + "\n"

            # Save payslip to text file
            payslip_filename = f"{employee_id}.txt"
            with open(payslip_filename, "w", encoding="utf-8") as payslip_file:
                payslip_file.write(payslip_content)


            print(f"Payslip for Employee ID {employee_id} generated and saved to {payslip_filename}.")
        else:
            print(f"No salary information found for Employee ID: {employee_id}")


# # Create an instance of EmployeeManagement class
record_attendance = EmployeeManagement()

# Assuming `record_attendance` is an instance of the `EmployeeManagement` class
# employee_id_to_generate_payslip = "Development"
# month_year_to_generate_payslip = "10-2023"  # Example month-year format: MM-YYYY

month_years = "2023-10"

# record_attendance.show_team_attendance_info(employee_id_to_generate_payslip)

# record_attendance.generate_attendance_summary_report(month_years)

# Example usage
# employee_manager = EmployeeManagement()

# Specify the start and end dates for the attendance summary report (in the format 'YYYY-MM-DD')
start_dates = "2023-10-01"
end_dates = "2023-10-31"

# # Generate and display the attendance summary report for the specified time period
# record_attendance.generate_attendance_summary_report(start_dates, end_dates)
# iddd = '1'
# record_attendance.generate_attendance_summary_report(start_dates, end_dates)


record_attendance.generate_and_save_payslip('1', month_years)