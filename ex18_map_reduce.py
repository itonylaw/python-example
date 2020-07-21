"""
File: ex17_map_reduce.py
Author: TonyDeep
Date: 2020-07-21
"""

from functools import reduce

print('#1 map')
a_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]
map_data = map(lambda x: x * 2 + 1, a_list)
new_list = list(map_data)
print(new_list)

print('\n#2 reduce')
b_list = [1, 2, 3, 4, 5]
reduce_data = reduce(lambda x, y: x + y, b_list)
print(reduce_data)





