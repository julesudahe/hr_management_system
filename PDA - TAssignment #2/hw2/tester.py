"""AndrewID: judahemu & Jeannette"""

# Importing different class to be used here during testing
from employee import Employee
from manager import Manager
from director import Director
from intern import Intern

employee_example = Employee("Jules", "Udahemuka", "Male", 60000.0)
manager_example = Manager("Jacky", "Mukakalinda", "Male", 60000.0, "Business Operations", 5, 10)
director_example = Director("Emmy", "Iraturinze", "Male", 60000.0, 20000.0, "Data Insight", 5)
intern_example = Intern("Romalice", "Ishimwe", "Male", 60000.0, "Carnegie Mellon University", "MS in Engineering AI", 5)

print('-------------------------------\n')

employee_example.show_employee_info()
print('-------------------------------\n')

manager_example.show_manager_info()
print('-------------------------------\n')

director_example.show_director_info()
print('-------------------------------\n')

intern_example.show_intern_info()
print('-------------------------------')
