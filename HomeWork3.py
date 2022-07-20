"""
    Created by Valery Grey
    EX 1 Home work 3
    Version : 1.0
"""

import statistics

def split_male_female(data):
    """
    The function split dictionary by gender
    :param data: dictionary
    :return: data_set_m and data_set_f , male and female dictionaries
    """
    data_set_m ,data_set_f= {} , {}

    for key , value in data.items():
            for k, v in value.items():
                 if k == "sex" and v == "male":
                     data_set_m.update({key:value})
                 if k == "sex" and v == "female":
                     data_set_f.update({key:value})

    return data_set_m , data_set_f

def find_median_average(data):
    """
    The function count average and median
    :param data: dictionary
    :return: avg , median , of all ages of all people
    """

    avg , median , arr = 0,0,[]

    for key, value in data.items():
        for k , v in value.items():
            if k == "age" :
                avg+=v
                arr.append(v)

    avg/=len(data)
    avg=round(avg,2)
    median=statistics.median(arr)
    return avg,median

def print_values_above(data,num=-1):
    """
    The function print all ages bigger of num ,
    if num was not received - print all ages
    :param data: dictionary
    :param num: integer number , default value -1
    :return: Print all ages bigger of num
    """

    for key, value in data.items():
        for k,v, in value.items():
            if k == "age" and v>num:
                print(v,end=' ')


def main():
    data_set = {1: {"name": "Tal", "sex": "male", "age": 22},
                2: {"height": 1.77, "sex": "male", "age": 65, "name": "Oren"},
                3: {"age": 32, "hobby": "play tennis", "name": "Noa", "sex": "female"}
                }
    data_set_m , data_set_f = split_male_female(data_set)
    find_median_average(data_set)
    print_values_above(data_set,23)

if __name__ == "__main__":
    main()
