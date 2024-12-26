import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = [int(x) for x in inp_line().strip("\n").split(' ')]
    BLINKS = 25

    print(' '.join([str(x) for x in inp]))
    for i in range(BLINKS):
        print(f"{i}/{BLINKS}")
        inp = blink(inp)

    return len(inp)

def p2():
    inp = [int(x) for x in inp_line().strip("\n").split(' ')]
    BLINKS = 25

    print(' '.join([str(x) for x in inp]))
    incs = list()
    last = 1
    for i in range(BLINKS):
        inp = blink(inp)
        if i != 0:
            incs.append(len(inp)/last)
        last = len(inp)

    print(f"avg inc: {sum(incs)/len(incs)}")

    return len(inp)

def blink(stones):
    to_add = list()
    for i, stone in enumerate(stones):
        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            strstone = str(stone)
            ls = int(strstone[:len(strstone)//2])
            rs = int(strstone[len(strstone)//2:])
            stones[i] = rs
            to_add.append((i,ls))
        else:
            stones[i] = stone * 2024

    for v in to_add:
        stones.insert(v[0], v[1])

    return stones

def inp_lines():
    return open(input, 'r').readlines()

def inp_line():
    return open(input, 'r').read()

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
