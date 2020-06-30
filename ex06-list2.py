"""
File: ex06-list2.py
Author: TonyDeep
Date: 2020-06-30
"""
print('#1 List Function')
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
print('\n')

print('#2 List as Stacks (LIFO)')
stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.append(7)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)
print('\n')

print('#3 List Comprehensions')
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# same as follow
squares = [x**2 for x in range(10)]
print(squares)
print('\n')

print('#4 Nested List Comprehensions')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

transposed = list(zip(*matrix))
print(transposed)

