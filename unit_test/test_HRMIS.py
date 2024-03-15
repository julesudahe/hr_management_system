import unittest
from HRMIS import EmployeeManagement

class TestEmployeeManagementClass(unittest.TestCase):
    """Test cases for EmployeeManagement class"""

    def setUp(self):
        """Set up initial state for each test method"""
        self.management = EmployeeManagement()
    
    def test_add_employee(self):
        """Test adding an employee"""
        initial_employee_count = len(self.management.employees)
        self.management.add_employee("Jules", "Udahemuka", "3", "Male", 60000, "Manager", "Manager", team="Sales", department="Marketing")
        self.assertEqual(self.management.get_employee_count(), initial_employee_count)

    def test_delete_employee(self):
        """Test deleting an employee"""
        self.management.add_employee("John", "Doe", "1", "Male", 50000, "Developer", "Employee", team="Dev Team", department="IT")
        initial_employee_count = len(self.management.employees)
        self.management.delete_employee("1")
        self.assertEqual(self.management.get_employee_count(), initial_employee_count)

    def test_update_data(self):
        """Test updating employee data"""
        
        self.management.add_employee("Jane", "Smith", "2", "Female", 60000, "Designer", "Employee", team="Design Team", department="IT")
        updated_data = self.management.update_data()
        
    def test_generate_attendance_summary_report(self):
        """Test generating attendance summary report"""

        start_date = "2023-01-01"
        end_date = "2023-01-31"
        self.management.generate_attendance_summary_report(start_date, end_date)

if __name__ == '__main__':
    unittest.main()
