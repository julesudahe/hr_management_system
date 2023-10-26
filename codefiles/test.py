import unittest
from datetime import datetime
from HRMIS import HRMIS

class TestHRMIS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hrmis = HRMIS()

    def test_add_employee(self):
        self.hrmis.add_employee("E001", "John", "Doe", "john.doe@email.com", 5000)
        self.assertIn("E001", self.hrmis.employees)

    def test_update_employee(self):
        self.hrmis.update_employee("E001", first_name="Jane")
        self.assertEqual(self.hrmis.employees["E001"].first_name, "Jane")

    def test_delete_employee(self):
        self.hrmis.add_employee("E002", "Test", "User", "test.user@email.com", 4000)
        self.hrmis.delete_employee("E002")
        self.assertNotIn("E002", self.hrmis.employees)

    def test_record_attendance(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        self.hrmis.record_attendance("E001", date_str, "09:00", "17:00")
        attendances = self.hrmis.attendance_records["E001"]
        self.assertTrue(any(a.date == date_str for a in attendances))

    def test_update_salary(self):
        self.hrmis.update_salary("E001", deductions=100, allowances=200, bonuses=50)
        salary = self.hrmis.salaries["E001"]
        self.assertEqual(salary.deductions, 100)
        self.assertEqual(salary.allowances, 200)
        self.assertEqual(salary.bonuses, 50)

    def test_data_persistence(self):
        # Add some data
        self.hrmis.add_employee("E003", "Temp", "User", "temp.user@email.com", 3500)
        self.hrmis.save_data()

        # Create a new HRMIS object and load data
        new_hrmis = HRMIS()
        new_hrmis.load_data()

        self.assertIn("E003", new_hrmis.employees)

    def test_generate_pay_slip(self):
        self.hrmis.generate_pay_slip("E001", "2023-10")
        # Ensure that the file has been created
        try:
            with open("E001.txt", "r") as file:
                content = file.read()
                self.assertIn("Pay Slip for Jane Doe - 2023-10", content)
        except FileNotFoundError:
            self.fail("Pay slip file not generated!")

if __name__ == "__main__":
    unittest.main()