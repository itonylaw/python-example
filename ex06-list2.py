"""
File: ex06-list2.py
Author: TonyDeep
Date: 2020-06-30
"""

fruits = ['organe', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('abc'))
print(fruits.index('apple'))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

a = fruits.pop()
print(a)
print(fruits)

