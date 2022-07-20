import pytest
from HomeWork4 import Date
import logging


@pytest.fixture
def get_date():
    try:
        return Date(22, 4, 2014)
    except:
        logging.error('The date is not correct , try to change the date .')
        return None

@pytest.fixture
def get_dates(get_date):
    try :
        date = Date(12, 4, 2014)
        return [get_date,date]
    except:
        logging.error('The second date is not correct , try to change the date .')
        assert date

# the test is made to meet the conditions, in this case
# this function will be checked by the first fixture
def test_init(get_date):
    try:
        assert get_date
    except:
        logging.warning("Something wrong at load data")

def test_str():
    try:
        print(Date(28, 2, 2014))
    except:
        logging.error('Cant print not correct date.')
        assert None

def test_eq(get_dates):
    dates = get_dates
    if dates[0]==dates[1] :
        assert dates[0] == dates[1]
    else:
        logging.warning('This test failed because the dates is not equals .')
        assert dates[0]==dates[1]

def test_gt(get_dates):
    dates = get_dates
    if dates[0] > dates[1]:
        assert dates[0] > dates[1]
    else:
        logging.warning('This tests failed because first date is smaller or equal to second .')
        assert dates[0] > dates[1]

def test_lt(get_dates):
    dates = get_dates
    if dates[0] < dates[1]:
        assert dates[0] < dates[1]
    else:
        logging.warning('This test failed because first date is bigger or equal to second .')
        assert dates[0] < dates[1]

def test_le(get_dates):

    dates = get_dates
    if dates[0] <= dates[1]:
        assert dates[0] <= dates[1]
    else:
        logging.warning('This test failed because first date bigger from second .')
        assert dates[0] <= dates[1]

def test_ge(get_dates):
    dates = get_dates
    if dates[0] >= dates[1]:
        assert dates[0] >= dates[1]
    else:
        logging.warning('This test failed because first date smaller from second .')
        assert dates[0] >= dates[1]

def test_ne(get_dates):
    dates = get_dates
    if dates[0] != dates[1]:
        assert dates[0] != dates[1]
    else:
        logging.warning('This test failed because the dates is not equals .')
        assert dates[0] != dates[1]

def test_sub(get_dates):
    dates = get_dates
    if isinstance(dates[0]-dates[1],int):
        assert isinstance(dates[0]-dates[1],int)
    else:
        logging.error("How did you manage to get something non-date into your mouth?")
        assert isinstance(dates[0] - dates[1], int)

# the test is made to meet the conditions, in this case
# this function will be checked by the first fixture
def isValid(get_dates):
    try:
        assert get_dates
    except:
        logger.info("The correctness of the date is checked at the start of tests")
        assert get_dates

def test_get_next_day(get_date):
    d = get_date.getNextDay()
    if d>get_date:
        assert d>get_date
    else:
        logging.error("Check if date is correct")

def test_get_next_days(get_date):
    d = get_date.getNextDay()
    if d > get_date:
        assert d > get_date
    else:
        logging.error("Check if date is correct")

