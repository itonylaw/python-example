"""
File: ex08-set.py
Author: TonyDeep
Date: 2020-07-02
"""

print('#1 set create')
set1 = set([123, 456, 123, 789])
print(set1)
set1.add(100)
print(set1)
set1.add(100)
print(set1)

set1.remove(456)
print(set1)

set2 = {'apple', 'orange', 'banana', 'pear'}
print(set2)
print('\n')

print('#2 set function')
a = set('hello')
b = set(['p', 'y', 't', 'h', 'o', 'n'])
print(a)
print(b)

print('\nIntersection set 交集 (a & b)')
print(a & b)

print('\nUnion set 并集 (a | b)')
print(a | b)

print('\nDifference set 差集 (a - b)')
print(a - b)

print('\nDifference set 差集 (b - a)')
print(b - a)





