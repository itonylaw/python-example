"""
File: ex17_filter.py
Author: TonyDeep
Date: 2020-07-20
"""

a_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]
filter_data = filter(lambda x: x % 3 == 0, a_list)
new_list = list(filter_data)
print(new_list)

map_data = map(lambda x: x * 2 + 1, a_list)
new_list2 = list(map_data)
print(new_list2)

