import pathlib
import os
import re

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

def p1():
    inp = inp_line()
    
    sum = 0
    muls = re.findall(r"mul\(\d+,\d+\)", inp)
    for mul in muls:
        (lnum,rnum) = re.findall(r"(\d+)", mul)
        sum += int(lnum) * int(rnum)

    return sum

def p2():
    inp = inp_line().strip("\n")
    # Remove newlines cause messed with regex
    inp = inp.replace("\n", "")

    pattern = r"^.*?don't|do\(\).*?(?=don't|$)"

    sum = 0
    dos = re.findall(pattern, inp)
    comb = ' '.join(dos)

    sum = 0
    muls = re.findall(r"mul\(\d+,\d+\)", comb)
    for mul in muls:
        (lnum,rnum) = re.findall(r"(\d+)", mul)
        sum += int(lnum) * int(rnum)

    return sum

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
