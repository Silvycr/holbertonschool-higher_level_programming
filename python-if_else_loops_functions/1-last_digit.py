#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ult_dig = abs(number) % 10

if number < 0:
    ult_dig = -ult_dig
print("Last digit of {} is {} ".format(number, ult_dig), end="")

if ult_dig == 0:
    print("and is 0")
if ult_dig > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
