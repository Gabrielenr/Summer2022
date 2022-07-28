# CSCI 381
# Summer 2022
# Homework Chapter 10 - 10.4
# Gabriel Rubio Alvarado

"""Exercise 10.4
(Modifying the Internal Data Representation of a Class) Section 10.4.2’s Time
class represents the time as three integer values. Modify the class to store the time as the
total number of seconds since midnight. Replace the _hour, _minute and _second attributes with
one _total_seconds attribute. Modify the bodies of the hour, minute and
second properties’ methods to get and set _total_seconds. Re-execute Section 10.4’s
IPython session using the modified Time class to show that the updated class
Time is interchangeable with the original one."""


class Time:
    def __init__(self, total_seconds):
        self._total_seconds = total_seconds

    @property
    def hour(self):
        return self._total_seconds // 3600

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._total_seconds -= self._total_seconds // 3600 * 3600
        self._total_seconds += hour * 3600

    @property
    def minute(self):
        return self._total_seconds % 3600 // 60

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._total_seconds -= self._total_seconds % 3600 // 60 * 60
        self._total_seconds += minute * 60

    @property
    def second(self):
        return self._total_seconds % 60

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds -= self._total_seconds % 60
        self._total_seconds += second

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f'Time(hour={self.hour}, minute={self.minute}, second={self.second})'

    def __str__(self):
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    @property
    def time(self):
        return self.hour, self.minute, self.second

    @time.setter
    def time(self, time_tuple):
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])

    # SOLUTION
    @property
    def universal_str(self):
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}'


my_time = Time(5954)
print('the time should be 01:39:14')
print(f'{str(my_time.universal_str):.^30}')

my_time.hour = 4
my_time.minute = 20
my_time.second = 15
print('the time should be 04:20:15')
print(f'{str(my_time.universal_str):.^30}')

my_time.set_time(12, 45, 10)
print('the time should be 12:45:10')
print(f'{str(my_time.universal_str):.^30}')

my_time.time = 22, 10, 2
print('the time should be 10:10:02 PM')
print(f'{str(my_time):.^30}')