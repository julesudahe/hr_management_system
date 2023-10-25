"""AndrewID: judahemu"""

from datetime import datetime, date, time, timedelta
from employee import Employee

class Attendance(Employee):
    """
    This class import all attributes Employee class.
    We introduce two attributes: attendance_record to store attendance data, and
    leave balance which is a list of allowed leave days

    We have five methods that we are using for attendance calculations.
        - get_rwanda_public_holidays: get for public holidays in Rwanda.
        - apply_public_holiday: methods to check if request time is not on holiday.
        - apply_for_leave: method for requesting time off.
        - record_in_time: method to record arrival time.
        - record_out_time: method to record departure time.
    """

    def __init__(self, first_name, last_name, employee_gender, salary):
        """Initializing the attributes of this class"""
        super().__init__(first_name, last_name, employee_gender, salary)
        
        # List to store attendance records
        self.attendance_records = {}
        
        # Dictionary to store types of days off and number of allowed days
        self.leave_balance = {
            'Paid Leave': 10, 
            'Sick Leave': 5,
            'Vacation': 15,
            'Maternity Leave': 90,
            'Unpaid Leave': 0
            }

    @staticmethod
    def get_rwanda_public_holidays(year):
        """Getter for Rwanda's public holidays"""
        # Public holidays for Rwanda
        return [
            date(year, 1, 1),  # New Year's Day
            date(year, 2, 1),  # Hereo's day
            date(year, 4, 7),  # Kwibuka Day
            date(year, 7, 1),  # Independence Day
            date(year, 7, 4),  # Liberation Day
            date(year, 12, 25),  # Christmas Day
            date(year, 12, 26),  # Boxing Day
            ]

    def check_leave_balance(self, leave_type, leave_duration):
        """Check leave balance before applying for leave"""
        return self.leave_balance[leave_type] >= leave_duration

    def apply_for_leave(self, leave_type, start_date, end_date):
        """Apply for leave days. It considers weekends and public holidays"""
        leave_duration = 0
        current_date = start_date

        while current_date <= end_date:
            # Check if it is not a weekend and not a public holiday
            if current_date.weekday() < 5 and current_date not in self.get_rwanda_public_holidays(current_date.year):
                leave_duration += 1
            current_date += timedelta(days=1)

        if self.check_leave_balance(leave_type, leave_duration):
            self.leave_balance[leave_type] -= leave_duration
            return f"Your {leave_type} for {leave_duration} days was approved."
        else:
            return f"You have insufficient {leave_type} days."
        
    def record_in_time(self, employee_id, is_late=False):
        """Record the in-time of the employee"""
        current_time = datetime.now().time()
        if not is_late:
            is_late = current_time > time(9, 0)
        in_time = datetime.now()
        
        attendance_record = {
            'employee_id': employee_id,
            'full_name': self.get_full_name(),
            'in_time': in_time,
            'out_time': None,
            'is_late': is_late,
            'leave_days': self.leave_balance.copy()
        }
        if employee_id not in self.attendance_records:
            self.attendance_records[employee_id] = []
        self.attendance_records[employee_id].append(attendance_record)

    def record_out_time(self, employee_id, is_early_departure=False):
        """Record the out-time of the employee"""
        current_time = datetime.now().time()
        if not is_early_departure:
            is_early_departure = current_time < time(17, 0)
        out_time = datetime.now()
        
        if employee_id in self.attendance_records:
            for record in self.attendance_records[employee_id]:
                if record['out_time'] is None:
                    record['out_time'] = out_time
                    record['is_early_departure'] = is_early_departure
                    return
