"""AndrewID: judahemu & Juwizeyi"""

from HRMIS import EmployeeManagement

def print_menu():
    """command-line interface for our project"""

    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Record Attendance")
    print("4. Generate Attendance Summary Report")
    print("5. Show Employee Information")
    print("6. Show Attendance Information")
    print("7. Show Team Attendance Information")
    print("8. Show Salary Information")
    print("9. Generate and Save Payslip")
    print("10. Update Employee Data")
    print("11. Calculate Salary for All Employees")
    print("0. Exit")

def main():
    record_attendance = EmployeeManagement()

    print("Welcome to Employee Management System!")
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter employee details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            employee_id = input("Employee ID: ")
            gender = input("Gender: ")
            salary = float(input("Salary: "))
            job_title = input("Job Title: ")
            level = input("Level: ")
            team = input("Team: ")
            department = input("Department: ")
            record_attendance.add_employee(first_name, last_name, employee_id, gender, salary, job_title, level, team, department)
        elif choice == "2":
            print("Enter employee ID to delete:")
            employee_id = input("Employee ID: ")
            record_attendance.delete_employee(employee_id)
        elif choice == "3":
            print("Record attendance:")
            employee_id = input("Employee ID: ")
            date = input("Date (YYYY-MM-DD): ")
            in_time = input("In Time (HH:MM): ")
            record_attendance.hr_record_in_time(employee_id, date, in_time)
        elif choice == "4":
            print("Generate attendance summary report:")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            record_attendance.generate_attendance_summary_report(start_date, end_date)
        elif choice == "5":
            print("Enter Employee ID to display information:")
            employee_id = input("Employee ID: ")
            record_attendance.show_employee_info(employee_id)
        elif choice == "6":
            print("Enter Employee ID and Date to display attendance information:")
            employee_id = input("Employee ID: ")
            date = input("Date (YYYY-MM-DD): ")
            record_attendance.show_attendance_info(employee_id, date)
        elif choice == "7":
            print("Enter Team Name to display team attendance information:")
            team_name = input("Team Name: ")
            record_attendance.show_team_attendance_info(team_name)
        elif choice == "8":
            print("Enter Employee ID to display salary information:")
            employee_id = input("Employee ID: ")
            record_attendance.show_salary_info(employee_id)
        elif choice == "9":
            print("Generate and Save Payslip:")
            employee_id = input("Employee ID: ")
            month_year = input("Month-Year (MM-YYYY): ")
            record_attendance.generate_and_save_payslip(employee_id, month_year)
        elif choice == "10":
            print("Update Employee Data:")
            updated_data = record_attendance.update_data()
        elif choice == "11":
            print("Calculating Salary for All Employees...")
            record_attendance.calculate_salary_for_employee_all()
        elif choice == "0":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
