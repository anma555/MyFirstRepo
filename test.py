import datetime

start_time_str = "2024-08-24T10:49:00z"
end_time_str = "2024-08-24T12:49:00z"
duration = datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M:%Sz") - datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%Sz")


from datetime import date 

def get_end_of_month(year: int, month: int) -> date:
    """
    Calculate the last day of a given month in a given year.

    Args:
        year (int): The year for which to calculate the end of the month.
        month (int): The month (1-12) for which to calculate the end of the month.

    Returns:
        date: The last day of the specified month in the specified year.
    """
    if month == 12:
        return date(year + 1, 1, 1) - date.resolution
    else:
        return date(year, month + 1, 1) - date.resolution
    

from enum import Enum

class State(Enum):
    BEFORE = 1
    SCHEDULED = 2
    IN_PROGRESS = 3
    COMPLETED = 4
    CANCELED = 5
    FAILED = 6