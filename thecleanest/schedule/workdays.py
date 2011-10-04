import datetime

WEEKDAYS = range(0, 5)
HOLIDAYS = (
    datetime.date(2011, 9, 5),      # labor day
    datetime.date(2011, 10, 10),    # columbus day
    datetime.date(2011, 11, 11),    # veterans day
    datetime.date(2011, 11, 24),    # thanksgiving
    datetime.date(2011, 11, 25),    # thanksgiving friday
    datetime.date(2011, 12, 26),    # winter break
    datetime.date(2011, 12, 27),    # winter break
    datetime.date(2011, 12, 28),    # winter break
    datetime.date(2011, 12, 29),    # winter break
    datetime.date(2011, 12, 30),    # winter break
)

def is_workday(date):
    """ Test to see if given date is a work day.
        Word days are defined as weekdays that are not paid holidays.
    """

    day_of_week = date.weekday()
    return day_of_week in WEEKDAYS and date not in HOLIDAYS

def date_range(start_date, end_date):
    """ Generate days from start_date to end_date, inclusive
    """

    days = (end_date - start_date).days
    for i in xrange(days + 1):
        yield start_date + datetime.timedelta(i)

def weekdays(date_range):
    for dt in date_range:
        if 0 <= dt.weekday() < 5:
            yield dt

def workdays(start_date):
    current = start_date
    while True:
        if is_workday(current):
            yield current
        current = current + datetime.timedelta(days=1)

        
def next_workday(after):
    days = date_range(after + datetime.timedelta(1), 
                      after + datetime.timedelta(days=365))
    for d in days:
        if is_workday(d):
            return d

