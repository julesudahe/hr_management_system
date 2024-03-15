import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Test cases for Employee class"""

    def test_invalid_inputs(self):
        """Test creating an employee with invalid inputs"""

        # Test negative salary
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2", "Male", -50000, "Developer", "Employee")

        # Test invalid job title
        with self.assertRaises(ValueError):
            Employee("Jane", "Smith", "3", "Female", 60000, "Invalid Job", "Employee")

        # Test invalid gender
        with self.assertRaises(ValueError):
            Employee("Alex", "Johnson", "4", "Other", 70000, "Designer", "Employee")

        # Test empty first name
        with self.assertRaises(ValueError):
            Employee("", "Brown", "5", "Male", 80000, "Manager", "Manager")

        # Test empty email
        with self.assertRaises(ValueError):
            Employee("Ella", "Clark", "6", "Female", 90000, "Manager", "Manager")

        # Test missing team and department for Manager level
        with self.assertRaises(ValueError):
            Employee("Michael", "Lee", "7", "Male", 100000, "Manager", "Manager")

        # Test invalid internship duration for Intern
        with self.assertRaises(ValueError):
            Employee("Olivia", "Lopez", "8", "Female", 40000, "Intern", "Intern", team="Dev Team", department="IT", internship_duration=7)

if __name__ == '__main__':
    unittest.main()
