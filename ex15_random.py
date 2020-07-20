"""
File: ex15_random.py
Author: TonyDeep
Date: 2020-07-16
"""

import random

print('#1 Random')
print(random.random())
print(random.uniform(10, 20))
print(random.randint(1, 100))
print(random.randrange(1, 20, 3)) # (1, 4, 7, 10, 13, 16, 19)

print('\n#2 Choice')
fruits = ['organe', 'apple', 'pear', 'banana', 'kiwi']
print(random.choice(fruits))
print(random.choices(fruits, k = 4)) # may repeat
print(random.sample(fruits, 4)) # not repeat

from random import shuffle
print('\n#3 Shuffle')
print(fruits)
for i in range(5):
    shuffle(fruits)
    print(fruits)



