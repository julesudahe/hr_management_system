# import numpy as np

from emplolyee import Employee

class Attendance(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, date, in_time, out_time):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
    
    def display_attendance(self):
        print(f"Date: {self.date}")
        print(f"In Time: {self.in_time}")
        print(f"Out Time: {self.out_time}")

    def duration(self):
        """
        Calculate and return the duration between in-time and out-time.
        """
        # Assuming in_time and out_time are strings in the format 'HH:MM'
        in_hour, in_minute = map(int, self.in_time.split(':'))
        out_hour, out_minute = map(int, self.out_time.split(':'))
        
        duration_hour = out_hour - in_hour
        duration_minute = out_minute - in_minute
        
        # Handle cases where out_minute < in_minute
        if duration_minute < 0:
            duration_hour -= 1
            duration_minute += 60
        
        return f"{duration_hour} hours, {duration_minute} minutes"
    
attendance_record = Attendance(123, 'John', 'Doe', 'johndoe@example.com', 50000, '2023-10-24', '09:00', '17:00')
attendance_record.display_employee_info()
attendance_record.display_attendance()
print(f"Worked Duration: {attendance_record.duration()}")
