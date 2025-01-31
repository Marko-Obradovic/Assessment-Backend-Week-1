"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    datetime_object = datetime.strptime(date_val, "%d/%m/%Y")
    return datetime_object
    


def get_days_between(first: datetime, last: datetime) -> int:
    difference = last - first
    days_difference = difference.days

    return days_difference


def get_day_of_week_on(date_val: datetime) -> str:
    date_object = convert_to_datetime(date_val)
    day_of_the_week_name = date_object.strftime("%A")
    return day_of_the_week_name

def get_current_age(birthdate: date) -> int:
    pass
