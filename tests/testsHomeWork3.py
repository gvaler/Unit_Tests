import pytest
from HomeWork3 import *
import logging


@pytest.fixture
def data_set():
    data_set = {1: {"name": "Tal", "sex": "male", "age": 22},
                2: {"height": 1.77, "sex": "male", "age": 65, "name": "Oren"},
                3: {"height": 0.77, "sex": "male", "age": 2, "name": "Igor"},
                4: {"age": 32, "hobby": "play tennis", "name": "Noa", "sex": "female"}
                }
    return data_set

def test_split_male_female(data_set):
    data_set_m, data_set_f = split_male_female(data_set)
    if len(data_set_m)+len(data_set_f) == len(data_set):
        assert len(data_set_m)+len(data_set_f) == len(data_set)
    else:
        logging.warning('Something wrong at split')
        assert len(data_set_m) + len(data_set_f) == len(data_set)

def test_median_avg(data_set):
    avg = 121/4
    median = statistics.median([2,22,32,65])
    a,m = find_median_average(data_set)
    if a!=avg and m!=median:
        logging.error('Error in calculating avg and median ')
        assert find_median_average(data_set)

def test_print(data_set):
    try:
        print_values_above(data_set,20)
    except:
        logging.error('Nothing to print')
        assert None

