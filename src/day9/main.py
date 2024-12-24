import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/tinput.txt"

def p1():
    inp = inp_line().strip("\n")
    map = list()

    for (id, num) in enumerate(inp[::2]):
        i = id * 2
        size_file = int(inp[i])
        free_space = int(inp[i+1]) if i < len(inp)-1 else 0 
        [map.append(str(id)) for x in range(size_file)]
        [map.append('.') for x in range(free_space)]

    done = False
    last_j = 0
    for (i, c) in reversed(list(enumerate(map))):
        if c == '.':
            continue
        if done:
            break
        for (j, c2) in enumerate(map):
            if j >= i:
                done = True
                break
            if c2 == '.':
                tmp = map[i]
                map[i] = map[j]
                map[j] = tmp
                last_j = j
                break

    res = 0
    for i,v in enumerate(map):
        if v == '.':
            break
        res += i*int(v)

    return res

class Entry:
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def __repr__(self):
        return f"[{self.id}, {self.size}]"

def p2():
    inp = inp_line().strip("\n")
    map = list()

    for (id, num) in enumerate(inp[::2]):
        i = id * 2
        size_file = int(inp[i])
        free_space = int(inp[i+1]) if i < len(inp)-1 else 0 
        map.append(Entry(id, size_file))
        map.append(Entry('.', free_space))

    print(map)

    for (i, bw) in reversed(list(enumerate(map))):
        if bw.id == '.':
            continue
        for (j, fw) in enumerate(map):
            if fw.id == '.' and fw.size >= bw.size:
                tmp = copy.deepcopy(bw)
                bw.id = fw.id
                bw.size = fw.size
                fw.size = fw.size - tmp.size
                map.insert(j, Entry(tmp.id, tmp.size))
                break

    print(map)

    res = 0
    id = 0
    for i,v in enumerate(map):
        if v.id == '.' and v.size > 0:
            break
        if v.id != '.':
            res += id*int(v)
            id += 1

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
