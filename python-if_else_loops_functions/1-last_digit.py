#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_idx = abs(number) % 10
if last_idx > 5:
    print(f"Last digit of {number} is {last_idx} and is greater than 5")
elif last_idx == 0:
    print(f"Last digit of {number} is {last_idx} and is 0")
else:
    print(f"Last digit of {number} is {last_idx} and is less than 6 and not 0")
