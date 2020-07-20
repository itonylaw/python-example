"""
File: ex16_lambda.py
Author: TonyDeep
Date: 2020-07-20
"""

print('\n#1 def')
def add(x, y):
    return x + y

print(add(3, 5))

print('\n#2 lambda')
new_add = lambda x, y: x + y
print(new_add(3, 5))
