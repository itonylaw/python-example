"""
File: ex04-for-range.py
Author: TonyDeep
Date: 2020-06-24
"""

animal = ['cat', 'dog', 'human', 'horse', 'pig']

for i in range(len(animal)):
    print(i, animal[i])

print('\n')

for i, v in enumerate(animal):
    print(i, v)
