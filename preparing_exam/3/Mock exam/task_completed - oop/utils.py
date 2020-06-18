import hashlib
import base64
from datetime import datetime


def input_datetime(msg):
    while True:
        st = input(msg)
        try:
            datetime.strptime(st, "%Y-%m-%d %H:%M")
            return st
        except ValueError:
            print("Incorrect format. Use YYYY-MM-DD HH:mm")


def input_number(msg, min_value, max_value):
    while True:
        try:
            num = int(input(msg))
            if num >= min_value and num <= max_value:
                return num
            print("Incorrect value")
        except:
            print("Incorrect format")


def input_value_from_list(msg, possible_values):
    while True:
        val = input(msg)
        if val in possible_values:
            return val
        else:
            print("Please enter one of the following values: " + ','.join(possible_values))


def get_hash(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    hash = m.digest()
    return bytes.decode(base64.b64encode(hash))
