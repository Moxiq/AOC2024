import pathlib
import os
import re
import numpy as np

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

word = "xmas"

def p1():
    inp = [x.strip("\n") for x in inp_lines()]
    XMAX = len(inp[0]) - 1
    YMAX = len(inp) - 1
    WORD = "XMAS"

    # for y in range(len(inp)):
    #     for x in range(len(inp[0])):
    #         print(inp[y][x], end='')
    #     print()
    # print("---------------")
    # print(inp[1][4:0:-1])
    # print([x[XMAX] for x in inp[0:4]])

    used = [['.']*(XMAX+1) for i in range(YMAX+1)]

    sum = 0
    tsum = 0
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            fsum = sum
            # Vertical down 
            if y+3 <= YMAX:
                if "".join([a[x] for a in inp[y:y+4]]) == WORD:
                    sum += 1
            # Vertical up
            if y-3 >= 0:
                if "".join([a[x] for a in inp[y:y-4:-1]]) == WORD:
                    sum += 1
            # Horizontal right
            if x+3 <= XMAX:
                if inp[y][x:x+4] == WORD:
                    sum += 1
            # Horizontal left
            if x-3 >= 0:
                if inp[y][x:x-4:-1] == WORD:
                    sum += 1
            # Diag ydown xright
            if x+3 <= XMAX and y+3 <= YMAX:
                if inp[y][x] + inp[y+1][x+1] + inp[y+2][x+2] + inp[y+3][x+3] == WORD:
                    sum += 1
            # Diag ydown xleft
            if x-3 >= 0 and y+3 <= YMAX:
                if inp[y][x] + inp[y+1][x-1] + inp[y+2][x-2] + inp[y+3][x-3] == WORD:
                    sum += 1
            # Diag yup xright
            if x+3 <= XMAX and y-3 >= 0:
                if inp[y][x] + inp[y-1][x+1] + inp[y-2][x+2] + inp[y-3][x+3] == WORD:
                    sum += 1
            # Diag yup xleft
            if x-3 >= 0 and y-3 >= 0:
                if inp[y][x] + inp[y-1][x-1] + inp[y-2][x-2] + inp[y-3][x-3] == WORD:
                    sum += 1
            if fsum != sum:
                used[y][x] = inp[y][x]


    print(np.matrix(used))
    print(tsum)

    return sum

def p2():
    inp = inp_lines()

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
