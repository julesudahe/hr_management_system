class Time:
    def __init__(self, time_in_second):
        self.time_in_second = time_in_second
    
    def convert_to_minutes (self):
        mins = int (self.time_in_second) // 60
        secs = int (self.time_in_second) % 60
        return '{:d}:{:2d}'.format (mins, secs)

    def convert_to_hours (self):
        hours = int (self.time_in_second) // 3600
        mins = (int (self.time_in_second) % 3600) // 60
        secs = int (self.time_in_second) % 60
        return '{:d}:{:d}:{:2d}'.format (hours, mins, secs)

e = Time (input ('Enter your time in second:'))

print ('Time in minutes is equal to:', e.convert_to_minutes())
print ('Time in hours is equal to:', e.convert_to_hours())