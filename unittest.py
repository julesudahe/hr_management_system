"""AndrewID: judahemu & Juwizeyi"""

import unittest
from employee import Employee
from salary import Salary
from attendance import Attendance
from deserializer import DataDeserializer
from HRMIS import EmployeeManagement

class TestEmployeeClass(unittest.TestCase):
    """ss"""
        
    def test_create_employee(self):
        """ss"""
        
        employee = Employee("John", "Doe", "1", "Male", 50000, "Developer", "Employee", team="Dev Team", department="IT")
        self.assertEqual(employee.get_full_name(), "John Doe")
        self.assertEqual(employee.get_employee_id(), "1")
        self.assertEqual(employee.job_title, "Developer")
        self.assertEqual(employee.team, "Dev Team")
        self.assertEqual(employee.department, "IT")
    
    def test_generate_email(self):
        """ss"""
        employee = Employee("John", "Doe", "1", "Male", 50000, "Developer", "Employee", team="Dev Team", department="IT")
        email = employee.generate_email()
        self.assertEqual(email, "john.doe@example.com")

class TestSalaryClass(unittest.TestCase):
    """ss"""
        
    def test_calculate_monthly_salary(self):
        """ss"""
        salary = Salary(deductions=10, allowance=5, bonus=2)
        salary_breakdown = salary.calculate_monthly_salary(60000)
        self.assertEqual(salary_breakdown['base_salary_monthly'], 5000.0)
        self.assertEqual(salary_breakdown['allowance_monthly'], 250.0)
        self.assertEqual(salary_breakdown['bonus_monthly'], 100.0)
        self.assertEqual(salary_breakdown['deductions_monthly'], 500.0)
        self.assertEqual(salary_breakdown['net_pay_monthly'], 5250.0)

class TestAttendanceClass(unittest.TestCase):
    """ss"""
        
    def test_record_in_time(self):
        """ss"""
        attendance = Attendance()
        attendance.record_in_time("1", "2023-11-01", "09:00")
        attendance_data = attendance.deserialize_attendance_from_json()
        self.assertEqual(attendance_data[0]['1'][0]['in_time'], "09:00")

    def test_record_out_time(self):
        """ss"""
        attendance = Attendance()
        attendance.record_out_time("1", "2023-11-01", "17:00")
        attendance_data = attendance.deserialize_attendance_from_json()
        self.assertEqual(attendance_data[0]['1'][0]['out_time'], "17:00")

class TestDataDeserializerClass(unittest.TestCase):
    """ss"""
        
    def test_deserialize_employees_from_json(self):
        """ss"""
        data_deserializer = DataDeserializer()
        employee_data = data_deserializer.deserialize_employees_from_json()
        self.assertIsInstance(employee_data, list)

class TestEmployeeManagementClass(unittest.TestCase):
    """ss"""
        
    def test_add_employee(self):
        """ss"""
        management = EmployeeManagement()
        management.add_employee("Alice", "Johnson", "3", "Female", 60000, "Manager", "Manager", team="Sales", department="Marketing")
        employee_data = management._load_employees_from_json()
        self.assertIn("3", employee_data[0])

    def test_delete_employee(self):
        """ss"""
        management = EmployeeManagement()
        management.delete_employee("1")
        employee_data = management._load_employees_from_json()
        self.assertNotIn("1", employee_data[0])

if __name__ == '__main__':
    unittest.main()
