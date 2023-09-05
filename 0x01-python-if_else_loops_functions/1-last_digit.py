#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
lastDigit = number % 10
if (lastDigit > 5):
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif (lastDigit == 0):
    print(f"Last digit of {number} is {lastDigit} is 0")
elif (6 < lastDigit and lastDigit != 0):
    print(f"Last digit of {number} is {lastDigit} and is less 6 and not 0")
