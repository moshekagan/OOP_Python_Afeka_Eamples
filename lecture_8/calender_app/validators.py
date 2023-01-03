from lecture_8.calender_app.DateTimeError import DateTimeError

VALID_DAYS = list(range(1, 32))
VALID_MONTHS = list(range(1, 13))
VALID_YEARS = list(range(2023, 2034))
VALID_DURATION = [15, 30, 45, 60]


def validate_day(day):
    if type(day) != int and not day.isnumeric():
        raise TypeError(f"Day should be a number! [{day}]")
    day = int(day)

    if not 1 <= day <= 31:
        raise DateTimeError(f"Day ({day}) most be between 1-31!")

    return day


def validate_month(month):
    if type(month) != int and not month.isnumeric():
        raise TypeError(f"Month should be a number! [{month}]")
    month = int(month)

    if not 1 <= month <= 12:
        raise DateTimeError(f"Month ({month}) most be between 1-12!")

    return month


def validate_year(year):
    if type(year) != int and not year.isnumeric():
        raise TypeError(f"Year should be a number! [{year}]")
    year = int(year)

    if not year in VALID_YEARS:
        raise DateTimeError(f"Year ({year}) most be one of: {VALID_YEARS}")

    return year


def validate_hour(hour):
    if type(hour) != int and not hour.isnumeric():
        raise TypeError(f"Hour should be a number! [{hour}]")
    hour = int(hour)
    if not 0 <= hour <= 23:
        raise DateTimeError(f"Hour ({hour}) most be between 0-23!")

    return hour


def validate_minute(minute):
    if type(minute) != int and not minute.isnumeric():
        raise TypeError(f"Minute should be a number! [{minute}]")
    minute = int(minute)

    if not 0 <= minute <= 59:
        raise DateTimeError(f"Minute ({minute}) most be between 0-59!")

    return minute


def validate_duration(duration):
    if type(duration) != int and not duration.isnumeric():
        raise TypeError(f"Duration should be a number! [{duration}]")
    duration = int(duration)

    if not duration in VALID_DURATION:
        raise DateTimeError(f"Minute ({duration}) most be on of: {VALID_DURATION}")

    return duration
