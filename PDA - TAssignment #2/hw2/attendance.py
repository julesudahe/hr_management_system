"""AndrewID: judahemu & Jeannette"""

import json
from datetime import datetime, time
from deserializer import DataDeserializer

class Attendance:
    """
    This class imports employee data and provides methods to record
    in-time and out-time for employees.
    """
# hardcode the
    def __init__(self):
        """Initializing the attributes of this class"""
        # List to store attendance records
        self.attendance_records = {}
        
        # Automatically store data to JSON
        self.store_attendance_to_json()

    def record_in_time(self, employee_id, is_late=False):
        """Record the in-time of the employee"""
        # Retrieve employee data from the JSON file
        employee_data = DataDeserializer().deserialize_employees_from_json()

        if employee_id in employee_data:
            current_time = datetime.now().time()
            if not is_late:
                is_late = current_time > time(9, 0)
            in_time = datetime.now().isoformat()
            
            # Get employee details from employee_data
            employee_details = employee_data[employee_id]
            full_name = employee_details['full_name']

            attendance_record = {
                'employee_id': employee_id,
                'full_name': full_name,
                'in_time': in_time,
                'is_late': is_late,
                'out_time': None,
            }

            # Initialize attendance record list if not exists
            if employee_id not in self.attendance_records:
                self.attendance_records[employee_id] = []

            self.attendance_records[employee_id].append(attendance_record)
        else:
            print("That EmployeeID does not exist")

    def record_out_time(self, employee_id, is_early_departure=False):
        """Record the out-time of the employee"""
        current_time = datetime.now().time()
        if not is_early_departure:
            is_early_departure = current_time < time(17, 0)
        out_time = datetime.now().isoformat()
        
        if employee_id in self.attendance_records:
            for record in self.attendance_records[employee_id]:
                if record['out_time'] is None:
                    record['out_time'] = out_time
                    record['is_early_departure'] = is_early_departure
                    return

    def store_attendance_to_json(self):
        """Store attendance data to a JSON file."""
        with open("attendance.json", "w", encoding="utf-8") as json_file:
            json.dump(self.attendance_records, json_file, indent=4)

# Assuming you have the Attendance class definition and DataSerializer class imported

# Create an instance of the Attendance class
attendance_system = Attendance()

# Record in-time for an employee with ID '123'
attendance_system.record_in_time('CMUID0002')

# Record out-time for the same employee with ID '123'
attendance_system.record_out_time('CMUID0002')

# Record in-time for another employee with ID '456' who is late
attendance_system.record_in_time('CMUID0003', is_late=True)

# Record out-time for the employee with ID '456'
attendance_system.record_out_time('CMUID0004')

# Store attendance data to JSON file
attendance_system.store_attendance_to_json()
