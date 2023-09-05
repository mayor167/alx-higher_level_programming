#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# check for +ve, -ve number and Zero
if (number > 0):
    print(f"{number} is positive")
elif (number == 0):
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
