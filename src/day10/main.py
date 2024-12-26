import pathlib
import os
import re
import numpy as np
import copy
import itertools
import sys

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = [[int(y) for y in (list(x.strip("\n")))] for x in inp_lines()]

    res = 0
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            visited = set()
            if inp[x][y] != 0:
                continue
            res += recurse_path(inp, x, y, visited)

    return res


def p2():
    inp = [[int(y) for y in (list(x.strip("\n")))] for x in inp_lines()]

    res = 0
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[x][y] != 0:
                continue
            res += recurse_path(inp, x, y, None)

    return res

dirs = {(0,-1), (1,0), (0,1), (-1,0)}
def recurse_path(grid, x, y, visited):
    sum = 0
    if visited is not None and (x,y) in visited:
        return sum
    if visited is not None:
        visited.add((x,y))
    if grid[x][y] == 9:
        return sum + 1
    for dir in dirs:
        if x + dir[0] >= len(grid[y]) or x + dir[0] < 0 or y + dir[1] >= len(grid) or y + dir[1] < 0:
            continue
        if grid[x+dir[0]][y+dir[1]] - grid[x][y] != 1:
            continue
        sum += recurse_path(grid, x+dir[0], y+dir[1], visited)

    return sum

def inp_lines():
    return open(input, 'r').readlines()

def inp_line():
    return open(input, 'r').read()

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
