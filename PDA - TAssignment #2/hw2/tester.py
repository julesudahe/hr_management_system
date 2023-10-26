"""AndrewID: judahemu & Jeannette"""

# Importing different class to be used here during testing
from employee_master import Employee
from salary import Salary
from attendance import Attendance
from employee_management import EmployeeManagement


employee_example = Employee("Jules", "Udahemuka", "Male", 60000.0)
manager_example = Salary("Jacky", "Mukakalinda", "Male", 60000.0, "Business Operations", 5, 10)
director_example = Attendance("Emmy", "Iraturinze", "Male", 60000.0, 20000.0, "Data Insight", 5)
intern_example = EmployeeManagement("Romalice", "Ishimwe", "Male", 60000.0, "Carnegie Mellon University", "MS in Engineering AI", 5)
