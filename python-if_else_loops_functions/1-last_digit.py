#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digito = abs(number) % 10
if number < 0:
    digito = -digito
print("Last digit of {} is {} and is ".format(number, digito), end="")
if digito > 5:
    print("greater than 5")
elif digito == 0:
    print("0")
else:
    print("less than 6 and not 0")
