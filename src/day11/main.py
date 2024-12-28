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

    for i in range(BLINKS):
        print(f"{i}/{BLINKS}")
        inp = blink(inp)

    return len(inp)

def p2():
    inp = [int(x) for x in inp_line().strip("\n").split(' ')]
    BLINKS = 75

    memo = blink_p2(inp, BLINKS)
    return sum(memo.values())

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

# TODO
# Create a map that contains the count of stone with a specific number.
# When new stones come in, check if there is any match and add to the count if so, else, add new entry with 1
# Go through the map and append/delete entries based on each stone and their count, count times
# In the end, we can just sum up the counts for each entry in the map
def blink_p2(stones, iter):
    memo = {}
    [memo.update({x: stones.count(x)}) for x in stones]

    for it in range(iter):
        for stone, count in copy.deepcopy(memo).items():
            if count <= 0:
                continue
            to_add = []
            if stone == 0:
                to_add.append(1)
            elif len(str(stone)) % 2 == 0:
                strstone = str(stone)
                ls = int(strstone[:len(strstone)//2])
                rs = int(strstone[len(strstone)//2:])
                to_add.extend((ls, rs))
            else:
                to_add.append(stone*2024)

            memo[stone] -= count
            for add in to_add:
                if add in memo:
                    memo[add] += count
                else:
                    memo[add] = count

    return memo

def inp_lines():
    return open(input, 'r').readlines()

def inp_line():
    return open(input, 'r').read()

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
