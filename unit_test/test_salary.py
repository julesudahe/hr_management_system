import unittest
from salary import Salary

class TestSalaryClass(unittest.TestCase):
    """Building tester class to test the Salary class"""
        
    def test_calculate_monthly_salary(self):
        """Adding different attributes from the salary class, and testing them"""
        
        # Test with various deduction, allowance, bonus, and base salary values
        salary = Salary(deductions=10, allowance=5, bonus=2)
        salary_breakdown = salary.calculate_monthly_salary(60000)
        self.assertEqual(salary_breakdown['base_salary_monthly'], 5000.0)
        self.assertEqual(salary_breakdown['allowance_monthly'], 250.0)
        self.assertEqual(salary_breakdown['bonus_monthly'], 100.0)
        self.assertEqual(salary_breakdown['deductions_monthly'], 500.0)
        self.assertEqual(salary_breakdown['net_pay_monthly'], 4850.0)

        # Test with zero deductions, allowance, and bonus
        salary = Salary(deductions=0, allowance=0, bonus=0)
        salary_breakdown = salary.calculate_monthly_salary(60000)
        self.assertEqual(salary_breakdown['base_salary_monthly'], 5000.0)
        self.assertEqual(salary_breakdown['allowance_monthly'], 0.0)
        self.assertEqual(salary_breakdown['bonus_monthly'], 0.0)
        self.assertEqual(salary_breakdown['deductions_monthly'], 0.0)
        self.assertEqual(salary_breakdown['net_pay_monthly'], 5000.0)

if __name__ == '__main__':
    unittest.main()
