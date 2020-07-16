"""
File: ex13_comprehensions.py
Author: TonyDeep
Date: 2020-07-16
"""

lista = [1, 2, 3]
listb = [2, 7]

listc = [(a, b) for a in lista for b in listb]
print(listc)

listd = [(a, b) for a in lista for b in listb if a !=b]
print(listd)
