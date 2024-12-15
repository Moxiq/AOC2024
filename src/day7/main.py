import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

operators = ["*", "+", "|"]

def p1():
    inp = [(x.strip("\n")) for x in inp_lines()]

    res = 0
    for x in inp:
        s = x.split(":")
        testval, nums = s[0], s[1].strip(" ").split(" ")
        ops = []
        N = len(nums) - 1
        for i in range(2 ** N):
            for j in range(N):
                if j == 0:
                    ops.append([])
                ops[i].append(operators[(i >> j)&1])

        # print(np.matrix(ops))
        for i in range(2**N):
            exp = []
            for (j, num) in enumerate(nums):
                exp.append(num)
                exp.append(operators[(i >> j)&1])

            if parse_exp(exp) == int(testval):
                res += int(testval)
                break

    assert(res == 4998764814652 or res == 3749)
    return res

def parse_exp(exp):
    sum = int(exp[0])
    for (i, v) in enumerate(exp[1:-1:2]):
        ind = 1 + i * 2
        if v == '+':
            sum += int(exp[ind+1])
        elif v == '*':
            sum *= int(exp[ind+1])
        elif v == '|':
            sum = int(str(sum) + exp[ind+1])

    return sum

def p2():
    inp = [(x.strip("\n")) for x in inp_lines()]

    res = 0
    c = 0
    for x in inp:
        c += 1
        s = x.split(":")
        testval, nums = s[0], s[1].strip(" ").split(" ")
        print("{:.2f}%".format(100*c/len(inp)), end="\r")
        for (i, comb) in enumerate(itertools.product(operators, repeat=len(nums))):
            exp = []
            for (j, num) in enumerate(nums):
                exp.append(num)
                exp.append(comb[j])

            if parse_exp(exp) == int(testval):
                res += int(testval)
                break

    return res

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
