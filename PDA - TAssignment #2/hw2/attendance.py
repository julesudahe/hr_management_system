"""AndrewID: judahemu & Jeannette"""

import json
from datetime import datetime, time
from deserializer import DataDeserializer

class Attendance:
    """
    This class imports employee data and provides methods to record
    in-time and out-time for employees.
    """

    def __init__(self):
        """Initializing the attributes of this class"""
        self.attendance_records = {}
        
    def record_in_time(self, employee_id, date, in_time):
        """Record the in-time of the employee"""
        # Retrieve employee data from the JSON file
        employee_data = DataDeserializer().deserialize_employees_from_json()
        employee_info = next((employee for employee in employee_data if employee.get(employee_id)), None)

        is_late=False
        if employee_info:
            if not is_late:
                current_time = datetime.strptime(in_time, "%H:%M").time()
                is_late = current_time > time(9, 0)

            attendance_record = {
                'employee_id': employee_id,
                'date': date,
                'in_time': in_time,
                'is_late': is_late,
                'out_time': None,
                'is_early_departure': None
            }

            # Initialize attendance record list if not exists
            if employee_id not in self.attendance_records:
                self.attendance_records[employee_id] = []

            self.attendance_records[employee_id].append(attendance_record)
        else:
            print("That EmployeeID does not exist")

    def record_out_time(self, employee_id, date, out_time):
        """Record the out-time of the employee"""
        current_time = datetime.strptime(out_time, "%H:%M").time()

        is_early_departure=False
        if not is_early_departure:
            is_early_departure = current_time < time(17, 0)

        if employee_id in self.attendance_records:
            for record in self.attendance_records[employee_id]:
                if record['out_time'] is None and record['date'] == date:
                    record['out_time'] = out_time
                    record['is_early_departure'] = is_early_departure
                    return
        else:
            print(f"EmployeeID {employee_id} doesn't have a record for the given date.")

    def store_attendance_to_json(self):
        """Store all employee data as a JSON array to an existing JSON file."""

        try:
            with open("attendance.json", "r", encoding="utf-8") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        for employee_id, attendance_info in self.attendance_records.items():
            if employee_id not in existing_data:
                existing_data.append({employee_id: attendance_info})

        with open("attendance.json", "w", encoding="utf-8") as updated_file:
            json.dump(existing_data, updated_file, indent=4)

# record_attendance = Attendance()

# # Record in-time for an employee with ID 'CMUID0001' on a specific date
# # record_attendance.record_in_time('CMUID0001', '2023-10-29', '09:30')

# # # Record out-time for the same employee with ID 'CMUID0001' on the same date
# # record_attendance.record_out_time('CMUID0001', '2023-10-29', '17:15')

# # Record in-time for another employee with ID 'CMUID0002'.
# record_attendance.record_in_time('CMUID000q1', '2023-10-30', '09:45')

# # Record out-time for the employee with ID 'CMUID0002' on the same date, indicating they left early
# record_attendance.record_out_time('CMUID000q1', '2023-10-30', '16:45')

# # Store attendance data to JSON file
# record_attendance.store_attendance_to_json()
