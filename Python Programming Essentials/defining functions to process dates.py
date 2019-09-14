import datetime

def days_in_month(year, month):
    """
    :param year: an integer between datetime.MINYEAR and datetime.MAXYEAR representing the year
    :param month: an integer between 1 and 12 representing the month
    :return: the number of days in the input month
    """

    #check year is between 1 and 999
    if year < datetime.MINYEAR or year > datetime.MAXYEAR or not isinstance(year, int):
        return 0