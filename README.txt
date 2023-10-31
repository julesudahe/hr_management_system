Introduction
---------------------------------------------------------------------------------

This is a python a Human Resource Management Information System (HRMIS). 
The HRMIS should efficiently manage employee records, track attendance, calculate salaries, and provide basic reporting 
capabilities using object-oriented programming (OOP) principles

Explaining the Inheritance Hierarchy
---------------------------------------------------------------------------------

Employee Class
---------------------------------------------------------------------------------
Attributes: first_name, last_name, employee_id, employee_gender, salary, job_title, level, team , department, internship_duration
We have ways of validating the employee inputs
We have a methods which generate Email automatically using employee names.
We have setter and getter methods to access employee information.
We have a method to save employee information in the JSON file as a dara persistence mechanism

Salary Class
---------------------------------------------------------------------------------
Attributes: deductions, allowance, bonus 
We have ways of validating that the salary must be number
We have a methods which stores salary information for a respective employee_ID into a JSON format
We have getter methods to access employee salary information.
We have a method to calculate employee salary from base salary 
We have a method to display employee salary breakdown

Attendance Class
---------------------------------------------------------------------------------
Attributes: attendance_records (as a dictionary)
We have methods to record in and out time for employee, both methods accepts dates, in-time and out-time 
We have a methods which stores employee attendance information for a respective employee_ID into a JSON format

Desirializer Class
---------------------------------------------------------------------------------
Attributes: No attributes
We have methods to allow Salary, attendance and employee class read from JSON files 

Employee_management Class (Inherits from all other classes)
---------------------------------------------------------------------------------
Attributes: employees
Methods Used:
    1. _save_to_json: A function to save employee data to JSON
        Attributes: employee_data

    2. add_employee: use Employee class object to add a new employee
        Attributes: first_name, last_name, serial_id, employee_gender, salary, job_title, level, team, department, 
        internship_duration

    3. delete_employee: Uses target employee_ID to check if the employee is available in a JSON file and 
    delete the targeted employee, it raises the error if the employee is not available
        Attributes: target_employee_id
    
    4. update_data: Asks the user to input the employee id and the field that he/she wants to update and stores the new 
    values in a JSON file 

    5. calculate_salary_for_employee_all: Calls the Salary class to calculate the employee salary

    6. hr_record_in_time and hr_record_out_time: to allow the HR to record the in and out time for a specific employee ID

    7. generate_attendance_summary_report: Reads attendance records from the attendance json file and calculate the total
    duration of an employee and whether the employee was late. I then generate and print the summary in a tabular format.
        Attributes: start_date, end_date
    
    8. show_employee_info: Retrieves information for a specific employee from employee json file and print every 
    information related to that employee 
        Attributes: employee_id

    10. show_attendance_info: Retrieves information for a specific employee from attendance json file and print every 
    information related to attendance of that employee
        Attributes: employee_id, date
    
    11. show_team_attendance_info: Retrieves information for a specific employee from attendance json file and print every 
    information related to attendance of the specified team
        Attributes: team_name

    12. show_salary_info:Retrieves information for a specific employee from salary json file and print monthly salary
    information  of the specified employee
        Attributes: self, employee_id
    
    13.  generate_and_save_payslip: Generate and save payslip for the specified employee ID and month-year.
        Attributes: (self, employee_id, month_year)

Tester File
---------------------------------------------------------------------------------
The tester file inheit from Employee_management classes and run a number of operations to test 
the code against different scenarios. 