"""
File: ex12-output.py
Author: TonyDeep
Date: 2020-07-10
"""

print('#1 output')
year = 2020
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

print('\n#2 str() for human, repr() for interpreter')
hello = 'Hello, World\n'
print(str(hello))
print(repr(hello))

x = 10 * 3.25
s = 'x is ' + repr(x)
print(s)

score = {'Alice': 78, 'Becky': 156, 'Candy': 93}
for n, s in score.items():
    print(f'{n:10} ==> {s:10d}')

print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other = 'Georg'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
