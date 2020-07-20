"""
File: ex14_json.py
Author: TonyDeep
Date: 2020-07-16
"""

import json

print('#1 dict to json')
data = {
    'code' : 'TSLA',
    'name' : 'Tesla',
    'price' : 1546
}
json_str = json.dumps(data)
print(json_str)

print('\n#2 json to dict')
data1 = json.loads(json_str)
print(data1)



