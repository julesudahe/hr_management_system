"""AndrewID: judahemu & Jeannette"""

import json
from datetime import datetime, time
from deserializer import DataDeserializer
 # add name, team
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
    
        employee_info = None
        for employee in employee_data:
            if employee_id in employee:
                employee_info = employee[employee_id]
                break

        if employee_info:
            full_name = employee_info.get("full_name")
            team = employee_info.get("team")
            # rest of your code remains the same
        else:
            print("EmployeeID does not exist.")
            return  # Add this return statement to exit the function if employee ID does not exist.

        is_late = False
        if not is_late:
            current_time = datetime.strptime(in_time, "%H:%M").time()
            is_late = current_time > time(9, 0)

        attendance_record = {
            'employee_id': employee_id,
            'full_name': full_name,
            'team': team,
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

    def record_out_time(self, employee_id_2, date_2, out_time_2):
        """Record the out-time of the employee"""
        current_time = datetime.strptime(out_time_2, "%H:%M").time()

        is_early_departure=False
        if not is_early_departure:
            is_early_departure = current_time < time(17, 0)

        if employee_id_2 in self.attendance_records:
            for record in self.attendance_records[employee_id_2]:
                if record['out_time'] is None and record['date'] == date_2:
                    record['out_time'] = out_time_2
                    record['is_early_departure'] = is_early_departure
                    return
        else:
            print(f"EmployeeID {employee_id_2} doesn't have a record for the given date.")

    def store_attendance_to_json(self):
        """Store all employee data as a JSON array to an existing JSON file."""

        try:
            with open("attendance.json", "r", encoding="utf-8") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        for employee_id_1, attendance_info in self.attendance_records.items():
            for record in existing_data:
                if employee_id_1 in record:
                    # Update the existing record with the new attendance information
                    existing_records = record[employee_id_1]
                    for existing_record in existing_records:
                        if existing_record['date'] == attendance_info[0]['date']:
                            existing_record['out_time'] = attendance_info[0]['out_time']
                            existing_record['is_early_departure'] = attendance_info[0]['is_early_departure']
                            break
                    break
            else:
                # If no existing record is found, add a new record to the existing data
                existing_data.append({employee_id_1: attendance_info})
                
        with open("attendance.json", "w", encoding="utf-8") as updated_file:
            json.dump(existing_data, updated_file, indent=4)
            

# Example usage of the Attendance class

# Create an instance of the Attendance class
attendance_manager = Attendance()

# Example 1: Recording in-time for an employee
# employee_id = "CMUID0001"
# date = "2023-10-29"
# in_time = "09:30"
# attendance_manager.record_in_time(employee_id, date, in_time)

# # Example 2: Recording out-time for the same employee on the same date
# out_time = "17:15"
# attendance_manager.record_out_time(employee_id, date, out_time)

# Example 3: Recording in-time for another employee on a different date
employee_ids = "CMUID0002"
dates = "2023-10-30"
in_times = "09:45"
attendance_manager.record_in_time(employee_ids, dates, in_times)

out_time = "17:15"
attendance_manager.record_out_time(employee_ids, dates, out_time)
# Example 4: Storing attendance records to a JSON file
attendance_manager.store_attendance_to_json()

# # Example 5: Displaying attendance records for individual employees
# print("Attendance Records for CMUID0001:")
# print(attendance_manager.attendance_records.get("CMUID0001", "No attendance records found"))

# print("Attendance Records for CMUID0002:")
# print(attendance_manager.attendance_records.get("CMUID0002", "No attendance records found"))

# # Example 6: Displaying attendance records for the entire team
# print("Attendance Records for the Entire Team:")
# print(json.dumps(attendance_manager.attendance_records, indent=4))
