#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)
last_digit = int(str_number[-1])
state = ''
if last_digit > 5:
    state = "and is greater than 5"
elif last_digit == 0:
    state = "and is 0"
elif last_digit < 6 and last_digit != 0:
    state = "and is less than 6 and not 0"

print("Last digit of", number, "is", last_digit, state)
