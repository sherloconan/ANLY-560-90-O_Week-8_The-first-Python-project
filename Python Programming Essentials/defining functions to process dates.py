import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    # check year is between 1 and 9999
    if year < datetime.MINYEAR or year > datetime.MAXYEAR or not isinstance(year, int):
        return 0

    # check month is valid
    if month < 1 or month > 12 or not isinstance(month, int):
        return 0

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        # month == 2
        if (year % 4 == 0 and year % 100 != 0) or (year >= 400 and year % 400 == 0):
            # determine whether year is leap
            return 29
        else:
            return 28


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        # check year is between 1 and 999
        return False
    elif days_in_month(year, month) < day or day < 1:
        # check day is valid
        return False
    elif isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
        return True
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        # check date is valid
        return 0
    elif datetime.date(year2, month2, day2) < datetime.date(year1, month1, day1):
        # check second date is after the first date
        return 0
    else:
        difference = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        return difference.days


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if not is_valid_date(year, month, day):
        # check date is valid
        return 0
    elif datetime.date(year, month, day) > datetime.date.today():
        # check date is not in the future
        return 0
    else:
        difference = datetime.date.today() - datetime.date(year, month, day)
        return difference.days
