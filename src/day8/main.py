import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]

    antinodes = set()
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            char = inp[x][y]
            if char != '.' and char != '#':
                for (px, py) in find_pairs(char, inp):
                    if (px,py) == (x, y):
                        continue
                    ax, ay = x-(px-x), y-(py-y)
                    if ax >= 0 and ax < len(inp[0]) and ay>= 0 and ay < len(inp):
                        antinodes.add((ax, ay))


    return len(antinodes)

def find_pairs(char, grid):
    res = list()
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == char:
                res.append((x,y))

    return res


def p2():
    inp = [(list(x.strip("\n"))) for x in inp_lines()]

    antinodes = set()
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            char = inp[x][y]
            if char != '.' and char != '#':
                for (px, py) in find_pairs(char, inp):
                    if (px,py) == (x, y):
                        continue
                    d = 0
                    while True:
                        ax, ay = x-(d*(px-x)), y-(d*(py-y))
                        if not (ax >= 0 and ax < len(inp[0]) and ay>= 0 and ay < len(inp)):
                            break
                        antinodes.add((ax, ay))
                        d += 1

    for (x,y) in antinodes:
        inp[x][y] = '#'
    print(np.matrix(inp))

    return len(antinodes)

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
