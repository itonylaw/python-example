"""
File: ex09-dict.py
Author: TonyDeep
Date: 2020-07-02
"""

print('#1 Dictionary dict1(key: value)')
dict1 = {'Alice': 123, 'Becky': 456, 'Candy': 789}
print(dict1)
print(dict1['Becky'])

dict1['Candy'] = 100
print(dict1)
print('\n')

for k, v in dict1.items():
    print(k, v)
