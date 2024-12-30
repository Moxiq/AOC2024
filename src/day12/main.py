import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]

    regions = dict()
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] in regions and any((x, y) in regs for regs in regions[inp[y][x]]):
                continue

            reg = list()
            reg = find_region(inp, x, y, reg)
            if inp[y][x] not in regions:
                regions[inp[y][x]] = list()
            if reg not in regions[inp[y][x]]:
                regions[inp[y][x]].append(reg)

    res = 0
    for k, v in regions.items():
        for reg in v:
            area = len(reg)
            perimeter = find_peri(inp, reg)
            res += (area * perimeter)

    return res

def p2():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]

    return 42

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
rc = 0
def find_region(grid, x, y, reg):
    if (x, y) in reg:  # Check if we already handled this pos
        return reg

    reg.append((x, y))

    for dir in dirs:
        dx, dy = x + dir[0], y + dir[1]
        if dx >= len(grid[0]) or dx < 0 or dy >= len(grid) or dy < 0:
            continue
        if grid[dy][dx] != grid[y][x]:
            continue

        find_region(grid, dx, dy, reg)

    return reg

def find_peri(grid, region):
    perimeter = 0
    for x, y in region:
        for dir in dirs:
            dx, dy = x + dir[0], y + dir[1]
            if dx >= len(grid[0]) or dx < 0 or dy >= len(grid) or dy < 0:
                perimeter += 1
                continue
            if grid[y][x] != grid[dy][dx]:
                perimeter += 1
                continue

    return perimeter

def inp_lines():
    return open(input, 'r').readlines()

def inp_line():
    return open(input, 'r').read()

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
