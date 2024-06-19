import re

def task1(input_str):
    txt = r'^[a-z0-9]+$'
    return bool(re.match(input_str, txt))

def task2(input_str):
    txt = r'^[A-Za-z]+$'
    return bool(re.match(input_str, txt))

def task3(input_str):
    txt = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[0-9])\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[0-9])\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[0-9])\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[0-9])$'
    return bool(re.match(txt, input_str))

def task4(input_str):
    txt = r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$'
    return bool(re.match(txt, input_str))

def task5(input_str):
    txt = r'^\d{5}(?:-\d{4})?$'
    return bool(re.match(txt, input_str))

def task6(input_str):
    txt = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(txt, input_str))

def task7(input_str):
    txt = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    return bool(re.match(txt, input_str))

def task8(input_str):
    txt = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(txt, input_str))

def task9(input_str):
    txt = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(txt, input_str))

def task10(input_str):
    txt = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(txt, input_str))