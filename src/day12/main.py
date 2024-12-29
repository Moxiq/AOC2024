import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/tinput.txt"

def p1():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]
    print(np.matrix(inp))

    regions = dict()
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            skip = False
            # if inp[y][x] in regions and any((x, y) in x for x in regions[inp[y][x]]):
            #     continue
            if inp[y][x] in regions:
                for regs in regions[inp[y][x]]:
                    if (x, y) in regs:
                        skip = True
                        break
            if skip:
                continue

            reg = list()
            reg = find_region1(inp, x, y, reg)
            if inp[y][x] not in regions:
                regions[inp[y][x]] = list()
            if reg not in regions[inp[y][x]]:
                regions[inp[y][x]].append(reg)

    for k, v in regions.items():
        for reg in v:
            print(f"{k}: {len(reg)}")
    print(regions)
    return 42

def p2():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]

    return 42

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
rc = 0
# def find_region(grid, x, y, regs=dict(), reg=list(), done=set()):
#     if (x, y) in done:
#         return regs
#
#     # TODO: Make reg into set
#     if grid[y][x] not in regs:
#         regs[grid[y][x]] = list()
#
#     if (x, y) not in regs[grid[y][x]]:  # Check if we already handled this pos
#         reg.append((x, y))
#         done.add((x, y))
#
#     for dir in dirs:
#         dx, dy = x + dir[0], y + dir[1]
#         if dx >= len(grid[0]) or dx < 0 or dy >= len(grid) or dy < 0:
#             continue
#         if grid[dy][dx] != grid[y][x]:
#             continue
#
#         # regs[grid[dy][dx]].append((dx, dy))
#         # reg.append((dx, dy))
#         find_region(grid, dx, dy, regs, reg)
#
#     if reg not in regs[grid[y][x]]:
#         regs[grid[y][x]].append(copy.deepcopy(reg))
#         reg.clear()
#
#     return regs

def find_region1(grid, x, y, reg):
    if (x, y) in reg:  # Check if we already handled this pos
        return reg

    reg.append((x, y))

    for dir in dirs:
        dx, dy = x + dir[0], y + dir[1]
        if dx >= len(grid[0]) or dx < 0 or dy >= len(grid) or dy < 0:
            continue
        if grid[dy][dx] != grid[y][x]:
            continue

        find_region1(grid, dx, dy, reg)

    return reg

def inp_lines():
    return open(input, 'r').readlines()

def inp_line():
    return open(input, 'r').read()

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
