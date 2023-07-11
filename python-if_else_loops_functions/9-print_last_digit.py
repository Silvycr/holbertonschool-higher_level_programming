#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ult = number % 10
    else:
        ult = (number * -1) % 10
    print("{:d}".format(ult), end="")
    return (ult)
