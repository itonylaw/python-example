"""
File: ex10-module-test.py
Author: TonyDeep
Date: 2020-07-02
desc: test to call module
"""

import module

test1 = module.add(3, 7)
print(test1)


from module import mult as mu

test2 = mu(5, 3)
print(test2)

