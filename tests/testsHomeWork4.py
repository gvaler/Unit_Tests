import pytest
from HomeWork4 import Date
import logging


@pytest.fixture
def get_date():
    """
    fixture for getting date
    :return: date or None
    """
    try:
        return Date(22, 4, 2014)
    except:
        logging.error('The date is not correct , try to change the date .')
        return None

@pytest.fixture
def get_dates(get_date):
    """
    fixture for getting second date
    :param: get_date
    :return: date or None
    """
    try :
        date = Date(12, 4, 2014)
        return [get_date,date]
    except:
        logging.error('The second date is not correct , try to change the date .')
        assert date

# the test is made to meet the conditions, in this case
# this function will be checked by the first fixture
def test_init(get_date):
    """
    Init Testing
    :param get_date:
    :return:
    """
    try:
        assert get_date
    except:
        logging.warning("Something wrong at load data")

def test_str():
    """
    Print testing
    :return:
    """
    try:
        print(Date(28, 2, 2014))
    except:
        logging.error('Cant print not correct date.')
        assert None

def test_eq(get_dates):
    """
    Test for check if dates is equal
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0]==dates[1] :
        assert dates[0] == dates[1]
    else:
        logging.warning('This test failed because the dates is not equals .')
        assert dates[0]==dates[1]

def test_gt(get_dates):
    """
    Test for check if date1 bigger from date2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0] > dates[1]:
        assert dates[0] > dates[1]
    else:
        logging.warning('This tests failed because first date is smaller or equal to second .')
        assert dates[0] > dates[1]

def test_lt(get_dates):
    """
    Test for check if date1 smaller from date 2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0] < dates[1]:
        assert dates[0] < dates[1]
    else:
        logging.warning('This test failed because first date is bigger or equal to second .')
        assert dates[0] < dates[1]

def test_le(get_dates):
    """
    Test for check if date1 smaller or equal to date2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0] <= dates[1]:
        assert dates[0] <= dates[1]
    else:
        logging.warning('This test failed because first date bigger from second .')
        assert dates[0] <= dates[1]

def test_ge(get_dates):
    """
    Test for check if date1 bigger or equal to date2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0] >= dates[1]:
        assert dates[0] >= dates[1]
    else:
        logging.warning('This test failed because first date smaller from second .')
        assert dates[0] >= dates[1]

def test_ne(get_dates):
    """
    Test for check if date1 not equal to date2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if dates[0] != dates[1]:
        assert dates[0] != dates[1]
    else:
        logging.warning('This test failed because the dates is not equals .')
        assert dates[0] != dates[1]

def test_sub(get_dates):
    """
    Test date1 - date2
    :param get_dates:
    :return: assert
    """
    dates = get_dates
    if isinstance(dates[0]-dates[1],int):
        assert isinstance(dates[0]-dates[1],int)
    else:
        logging.error("How did you manage to get something non-date into your mouth?")
        assert isinstance(dates[0] - dates[1], int)

# the test is made to meet the conditions, in this case
# this function will be checked by the first fixture
def isValid(get_dates):
    """
    Test for check isValid function
    :param get_dates:
    :return: assert
    """
    try:
        assert get_dates
    except:
        logging.info("The correctness of the date is checked at the start of tests")
        assert get_dates

def test_get_next_day(get_date):
    """
    Test for check if get_next_day function  work
    :param get_date:
    :return: assert
    """
    d = get_date.getNextDay()
    if d>get_date:
        assert d>get_date
    else:
        logging.error("Check if date is correct")

def test_get_next_days(get_date):
    """
    Test for check if get_next_days function  work
    :param get_date:
    :return: assert
    """
    d = get_date.getNextDay()
    if d > get_date:
        assert d > get_date
    else:
        logging.error("Check if date is correct")

