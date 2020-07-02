"""
File: ex07-tuple.py
Author: TonyDeep
Date: 2020-07-02
"""

print('#1 Tuple create')
tuple1 = ('tuple_test', '中文', 123, 456)
tuple2 = () # empyt
tuple3 = (123,) # is tuple
tuple4 = (123) # is not tuple

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple1[1])
print('\n')

print('#2 tuple change')
list1 = [123, 456]
tuple5 = ('tuple_test', '中文', list1)
print(tuple5)
list1[0] = 789 # just can change the list1
print(tuple5)
print('\n')

print('#3 tuple function')
print(tuple5 * 2)
print(len(tuple5))
print('\n')

print('#4 tuple transfer from list')
list2 = [1, 2, 3, 4, 5]
print(list2)
tuple6 = tuple(list2)
print(tuple6)
print(max(tuple6))
print(min(tuple6))



