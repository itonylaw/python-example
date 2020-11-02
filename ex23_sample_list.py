"""
File: ex23_sample_list.py
Author: TonyDeep
Date: 2020-11-02
"""

from random import shuffle

def sample_list(sample_range):
    sample_list = []
    sample_list = list(range(sample_range))
    shuffle(sample_list)
    return sample_list

if __name__ == "__main__":
    alist = sample_list(15)
    print(alist)


