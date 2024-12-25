import pathlib
import os
import re
import numpy as np
import copy
import itertools

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

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

    for i in range(len(map)-1, -1, -1):
        bw = map[i]
        if bw.id == '.':
            continue
        for j in range(len(map)):
            fw = map[j]
            if j >= i:
                break
            if fw.id == '.' and fw.size >= bw.size:
                tmp = copy.deepcopy(bw)
                bw.id = fw.id
                fw.size = fw.size - tmp.size
                map.insert(j, Entry(tmp.id, tmp.size))
                break

    res = 0
    pos = 0
    for i,v in enumerate(map):
        if v.id != '.':
            for file in range(v.size):
                res += pos * v.id
                pos += 1
        else:
            pos += v.size

    return res

def printp2(map):
    res = list()
    for i, e in enumerate(map):
        if e.size == 0:
            continue
        res.append(e.size * str(e.id))

    print(''.join(res))

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
