import pathlib
import os
import re
import numpy as np
import copy

input = f"{pathlib.Path(__file__).parent.resolve()}/tinput.txt"

operators = ["*", "+"]

def p1():
    inp = [(x.strip("\n")) for x in inp_lines()]

    for x in inp:
        s = x.split(":")
        testval, nums = s[0], s[1].strip(" ").split(" ")
        # test all operators
        for (i, num) in enumerate(nums[:-1]):
            print(i, num)





    return 42

def p2():
    inp = [list(x.strip("\n")) for x in inp_lines()]

    return 42

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
