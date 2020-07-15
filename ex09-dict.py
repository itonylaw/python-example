"""
File: ex09-dict.py
Author: TonyDeep
Date: 2020-07-02
"""

print('#1 Dictionary score(key: value)')
score = {'Alice': 78, 'Becky': 56, 'Candy': 93}
print(score)
print(score['Becky'])

score['Candy'] = 100
print(score)
print('\n')

print(score.keys())
print(score.values())

for k in score:
    print(k)

for k, v in score.items():
    print(k, v)
