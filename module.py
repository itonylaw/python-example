"""
File: ex10-module.py
Author: TonyDeep
Date: 2020-07-02
desc: this file as module
"""

def add(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    # module test
    print(add(3, 4))
    print(mult(3, 4))
