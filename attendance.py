import json
from datetime import datetime, time
from deserializer import DataDeserializer


class Attendance:
    """
    This class takes no attributes, but it has three methods that we use to calculate and save attendance.

    Methods:
        record_in_time: It uses data retriever (DataDeserializer) to get all record from employee.json and check if the assigned 
                        employee_id is valid ID before it takes in data related to attendance.

        record_out_time: It takes in three attributes related to attendance and save them in the dictionary.
        
        store_attendance_to_json: This store data to json however when data are related to record_out_time, it first read attendance.json,
                                and update missing data like departure time, is_departure_early. 
    """

    def __init__(self):
        """Initializing the attributes of this class"""
        self.attendance_records = {}
        
    def record_in_time(self, employee_id, date, in_time):
        """Record the in-time of the employee"""
        employee_data = DataDeserializer().deserialize_employees_from_json() # Retrieve employee data from the JSON file
    
        if not employee_id or not date or not in_time:
            raise ValueError("Invalid EmployeeID.")

        employee_info = None
        for employee in employee_data:
            if employee_id in employee:
                employee_info = employee[employee_id]
                break

        if employee_info:
            full_name = employee_info.get("full_name")
            team = employee_info.get("team")
        else:
            raise ValueError("EmployeeID does not exist.")
        
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

    def record_out_time(self, employee_id_out, date_out, out_time_out):
        """Record the out-time of the employee"""
        current_time = datetime.strptime(out_time_out, "%H:%M").time()

        is_early_departure=False
        if not is_early_departure:
            is_early_departure = current_time < time(17, 0)

        # Update out_time where out_time is not and data matches
        if employee_id_out in self.attendance_records:
            for record in self.attendance_records[employee_id_out]:
                if record['out_time'] is None and record['date'] == date_out:
                    record['out_time'] = out_time_out
                    record['is_early_departure'] = is_early_departure
                    return
        else:
            print(f"EmployeeID {employee_id_out} doesn't have a record for the given date.")

    def store_attendance_to_json(self):
        """Store all employee data as a JSON."""
        try:
            with open("2. attendance.json", "r", encoding="utf-8") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = [] # Return empty list in case attendance.json is not found.

        # Update data related to out_time before saving the dictionary 
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
                
        # Save the newly created dictionary to attendance.json.
        with open("2. attendance.json", "w", encoding="utf-8") as updated_file:
            json.dump(existing_data, updated_file, indent=4)
