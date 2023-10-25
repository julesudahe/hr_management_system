Introduction
---------------------------------------------------------------------------------

This is a python employee management system and we are using class 
and inheritance hierarchy where Employee class is the parent class while 
other remaining class are the child inheriting from Employee class. 
Our four different classes: Employee, Manager, Director, and Intern. 
They represent employees hierarchy within an organization.

The class have relatively the same function except where we are adding 
new information needed specifically for that class. Below are the class 
breakdown and how they differ.


Explaining the Inheritance Hierarchy
---------------------------------------------------------------------------------

Employee Class
---------------------------------------------------------------------------------
Attributes: first name, last name, gender, and salary.
We have Email and Employee ID methods which generate Email and EmployeeID automatically
using employee names.
We have setter and getter methods to access employee information.
print method: We have print method to display the information from our class

Manager Class (Inherits from Employee)
---------------------------------------------------------------------------------
This class inherits all attributes and methods from the Employee class, and add new attributes.
New attributes: department manager_rate, and number of direct reports.
New method: Calculating salary based on management allowance and base salary.
print method: We have print method to display the information from our class

Director Class (Inherits from Employee)
---------------------------------------------------------------------------------
This class inherits all attributes and methods from the Employee class, and add new attributes.
New attributes: department, bonus, and a number of direct reports.
New method: Calculating director's earnings using bonus and base salary.
print method: We have print method to display the information from our class

Intern Class (Inherits from Employee)
---------------------------------------------------------------------------------
This class inherits all attributes and methods from the Employee class, and add new attributes.
New attributes: university name, program name, and internship durations.
New method: Calculating intern's earnings based on internship duration.
print method: We have print method to display the information from our class

Tester File
---------------------------------------------------------------------------------
The tester file inheit from all classes and run a number of operations to test 
the code against different scenarios. 