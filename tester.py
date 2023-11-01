"""AndrewID: judahemu & Juwizeyi"""

from HRMIS import EmployeeManagement

record_attendance = EmployeeManagement()

# Add employees
record_attendance.add_employee("Jules", "Julius", "4", "Male", 50000, "Software Developer", "Employee", team="Development", department="Backend")
record_attendance.add_employee("Jenny", "Jeannette", "2", "Female", 55000, "Project Manager", "Manager", team="Project Management", department="Project A")

# Delete an employee
record_attendance.delete_employee("2")

# Separator line
print("*" * 30)

# Record in time and out time for an employee
record_attendance.hr_record_in_time("4", "2023-10-31", "10:45")
record_attendance.hr_record_out_time("4", "2023-10-31", "11:15")

# Separator line
print("*" * 30)

# Generate attendance summary report for a specific time period
start_date = "2023-10-01"
end_date = "2023-10-31"
record_attendance.generate_attendance_summary_report(start_date, end_date)

# Separator line
print("*" * 30)

# Display employee information
record_attendance.show_employee_info("4")

# Separator line
print("*" * 30)

# Display attendance information for an employee on a specific date
record_attendance.show_attendance_info("4", "2023-10-31")

# Separator line
print("*" * 30)

# Display attendance information for a team
team_name = "Development"
record_attendance.show_team_attendance_info(team_name)

# Separator line
print("*" * 30)

# Display salary information for an employee
record_attendance.show_salary_info("4")

# Separator line
print("*" * 30)

# Generate and save payslip for an employee and month-year
month_year = "10-2023"
employee_id = "4"
record_attendance.generate_and_save_payslip(employee_id, month_year)

# Separator line
print("*" * 30)

# Calculate salary for all employees
record_attendance.calculate_salary_for_employee_all()

# # Separator line
print("*" * 30)

# Update employee data
updated_data = record_attendance.update_data()