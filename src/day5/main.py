import pathlib
import os
import re
import numpy as np

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = inp_line()
    split = [x.split("\n") for x in inp.split("\n\n")]
    # rules, updates = split[0], [x.split(',') for x in split[1][:-1]]
    rules, updates = split[0], [[int(a) for a in x.split(',')] for x in split[1][:-1]]

    correct = []
    for upd in updates:
        is_correct = True
        for rule in rules:
            r1, r2 = [int(x) for x in rule.split('|')]
            if r1 in upd and r2 in upd:
                if (upd.index(r1) > upd.index(r2)):
                    is_correct = False
                    
        if is_correct:
            correct.append(upd)

    sum = 0
    for c in correct:
        sum += c[len(c)//2]

    return sum

def p2():
    inp = inp_line()
    split = [x.split("\n") for x in inp.split("\n\n")]
    # rules, updates = split[0], [x.split(',') for x in split[1][:-1]]
    rules, updates = split[0], [[int(a) for a in x.split(',')] for x in split[1][:-1]]

    corrected = []
    for upd in updates:
        is_page = False
        while not is_correct(upd, rules):
            is_page = True

        if is_page:
            corrected.append(upd)

    sum = 0
    for c in corrected:
        sum += c[len(c)//2]

    return sum

def is_correct(upd, rules):
    for rule in rules: 
        r1, r2 = [int(x) for x in rule.split('|')]
        if r1 in upd and r2 in upd:
            ind_r1, ind_r2 = upd.index(r1), upd.index(r2)
            if (ind_r1 > ind_r2):
                tmp = upd[ind_r1]
                upd[ind_r1] = upd[ind_r2]
                upd[ind_r2] = tmp
                return False
    return True

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
