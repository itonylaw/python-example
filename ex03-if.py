"""
File: ex03-if.py
Author: TonyDeep
Date: 2020-06-23
"""

import random

x = random.randint(1, 100)
y = int(input('Please enter an integer(1-100):'))

if y < 0 or y > 100:
    print('out of range')
elif x < y:
    print(x, '<', y)
    print('You Win')
elif x > y:
    print(x, '>', y)
    print('You Loss')
else:
    print(x, '=', y)
    print('Super')