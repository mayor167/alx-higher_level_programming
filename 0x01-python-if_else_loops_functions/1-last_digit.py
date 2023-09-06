#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
lastDigit = abs(number) % 10
if (number < 0):
    lastDigit = -lastDigit
if (lastDigit > 5):
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
    elif (lastDigit < 6 and lastDigit != 0):
    print(f"Last digit of {number} is {lastDigit} and is less 6 and not 0")
elif (lastDigit == 0):
    print(f"Last digit of {number} is {lastDigit} is 0")
