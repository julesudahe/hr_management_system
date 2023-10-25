"""AndrewID: judahemu"""

from datetime import datetime, date, time
# from datetime import timedelta
from employee import Employee
import random

class Attendance(Employee):
    """
    This class has five main attributes: first name, last name, email, employee_id, and salary.
    It also includes methods for managing employee information and attendance records.
    """
    @staticmethod
    def get_rwanda_public_holidays(year):
        """Get Rwanda's public holidays for the specified year"""
        # Sample public holidays for Rwanda (add more as needed)
        return [
            date(year, 1, 1),  # New Year's Day
            date(year, 2, 1),  # Hereo's day
            date(year, 4, 7),  # Kwibuka
            date(year, 7, 1),  # Independence Day
            date(year, 7, 4),  # Liberation Day
            ]
    
    def apply_public_holiday(self, day_off):
        """Apply public holiday, adjust leave balances accordingly"""
        current_year = datetime.now().year
        rwanda_public_holidays = self.get_rwanda_public_holidays(current_year)
        
        if day_off in rwanda_public_holidays:
            # Deduct the public holiday from the vacation leave balance
            if self.leave_balance['vacation'] > 0:
                self.leave_balance['vacation'] -= 1
                print(f"Public holiday on {day_off}: Deducted from vacation leave balance.")
            else:
                print(f"No available vacation leave balance for the public holiday on {day_off}.")
        else:
            print(f"No public holiday on {day_off}.")

    def __init__(self, first_name, last_name, employee_gender, salary):
        super().__init__(first_name, last_name, employee_gender, salary)
        self.attendance_records = []  # List to store attendance records
        self.leave_balance = {
            'paid_leave': 10,  # Number of paid leave days
            'sick_leave': 5,   # Number of sick leave days
            'vacation': 15,     # Number of vacation days
            'maternity_leave': 90,  # Number of maternity leave days
            'unpaid_leave': 0  # Number of unpaid leave days
        }

    def apply_for_leave(self, leave_type, start_date, end_date):
        """Apply for leave of specified type and duration"""
        leave_duration = (end_date - start_date).days + 1
        if self.leave_balance[leave_type] >= leave_duration:
            self.leave_balance[leave_type] -= leave_duration
            return f"Leave approved: {leave_type} leave for {leave_duration} days."
        else:
            return f"Insufficient {leave_type} leave balance."

    def record_in_time(self, is_late=False):
        """Record the in-time of the employee"""

        current_time = datetime.now().time()
        is_late = current_time > time(9, 0)
        in_time = datetime.now()
        attendance_key = f"{current_time.strftime('%Y%m%d')}-{self.get_employee_id()}-{random.randint(1000, 9999)}"
        
        if is_late:
            pass

        attendance_record = {
            'attendance_key': attendance_key,
            'employee_id': self.get_employee_id(),
            'full_name': self.get_full_name(),
            'in_time': in_time,
            'out_time': None,
            'is_late': is_late
        }
        self.attendance_records.append(attendance_record)

    def record_out_time(self, is_early_departure=False):
        """Record the out-time of the employee"""

        current_time = datetime.now().time()
        is_early_departure = current_time < time(17, 0)
        out_time = datetime.now()
        if is_early_departure:
            pass

        for record in self.attendance_records:
            if record['employee_id'] == self.get_employee_id() and record['out_time'] is None:
                record['out_time'] = out_time
                record['is_early_departure'] = is_early_departure
                return

    # def grant_permissions(self, user_role):
    #     """Grant permissions based on user role"""
    #     # Implement permissions logic here
    #     pass
