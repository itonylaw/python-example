"""
File: ex02-list.py
Author: TonyDeep
Date: 2020-06-20
"""

print('#0 列表(List)\n')

print('#1')
squares = [1, 3, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[:])
print(squares + [36, 49])
print('\n')


print('#2')
cubes = [1, 8, 27, 65, 125]  # something wrong
print(cubes)

cubes[3] = 64
print(cubes)

cubes.append(216)
print(cubes)
print('\n')


print('#3')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(len(letters))

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)
print('\n')

print('#4')
num = list(range(10))
del num[2:8:2]  # list[start:stop:step]
print(num)

num2 = list(range(10))
del num2[::3]
print(num2)
print('\n')


print('#5')
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(a)
print(n)
print(x)
print(x[0])
print(x[0][1])
