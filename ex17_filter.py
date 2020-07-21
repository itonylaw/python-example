"""
File: ex17_filter.py
Author: TonyDeep
Date: 2020-07-20
"""

print('#1 filter')
a_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]
filter_data = filter(lambda x: x % 3 == 0, a_list)
new_list = list(filter_data)
print(new_list)

print('\n#2 sorted')
b_list = [70, 60, -20, 10, -30]
sorted_list1 = sorted(b_list)
sorted_list2 = sorted(b_list, key = abs, reverse = True)
print(b_list)
print(sorted_list1)
print(sorted_list2)
print(b_list) # not change

b_list.sort(key = abs, reverse = True)
print()
print(b_list) # changed

