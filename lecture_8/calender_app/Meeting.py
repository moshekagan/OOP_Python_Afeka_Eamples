from lecture_8.calender_app.DateTimeError import DateTimeError
from lecture_8.calender_app.validators import validate_day, validate_month, validate_year, validate_hour, \
    validate_minute, validate_duration


class Meeting:
    def __init__(self, title, day, month, year, hour, minute, duration, reminder=False):
        self.title = title
        self.day = validate_day(day)
        self.month = validate_month(month)
        self.year = validate_year(year)
        self.hour = validate_hour(hour)
        self.minute = validate_minute(minute)
        self.duration = validate_duration(duration)
        self.reminder = reminder

    def __str__(self):
        convert_time = lambda t: t if t > 9 else f"0{t}"

        res = f"* {self.title} | \n"
        res += f"{self.day}.{self.month}.{self.year} - "
        res += f"{convert_time(self.hour)}:{convert_time(self.minute)} | \n"
        res += f"Meeting duration: {self.duration} minutes\n"
        return res

    def __repr__(self):
        return str(self)

