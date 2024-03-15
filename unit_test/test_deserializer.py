import unittest
from deserializer import DataDeserializer

class TestDataDeserializerClass(unittest.TestCase):
    """
    Building tester class to test deserializer class.
    Since the function of this class work relatively the same.
    We did not test on each function, but we did test on one and implemented improvement to all.
    """
        
    def test_deserialize_employees_from_json(self):
        """Testing if employee data deserialized correctly"""

        data_deserializer = DataDeserializer()
        employee_data = data_deserializer.deserialize_employees_from_json()
        self.assertIsInstance(employee_data, list)

if __name__ == '__main__':
    unittest.main()
