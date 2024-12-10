import pathlib
import os
import re
import numpy as np
import copy

input = f"{pathlib.Path(__file__).parent.resolve()}/input.txt"

dirs = ['^', '>', 'v', '<']

class Guard:
    def __init__(self, init_dir, x, y):
        self.dir = '^'
        self.x = x
        self.y = y

def p1():
    inp = [list(x.strip("\n")) for x in inp_lines()]

    guard = None
    #Find guard initial
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] in dirs:
                guard = Guard(inp[y][x], x, y)
                break


    while not sim(inp, guard):
        pass

    # count x
    positions = 0
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            if inp[x][y] == 'X': 
                positions += 1

    return positions

def p2():
    inp_initial = [list(x.strip("\n")) for x in inp_lines()]
    loop_initial = [[[] for _ in range(len(inp_initial[0]))] for _ in range(len(inp_initial))]

    guard_initial = None
    #Find guard initial
    for y in range(len(inp_initial)):
        for x in range(len(inp_initial[0])):
            if inp_initial[y][x] in dirs:
                guard_initial = Guard(inp_initial[y][x], x, y)
                break

    result = 0
    # Place obstacle for every position
    for y in range(len(inp_initial)):
        for x in range(len(inp_initial[0])):
            # Ignore already places obstacles or guard initial pos
            if inp_initial[y][x] == '#' or (y == guard_initial.y and guard_initial.x == x):
                continue
            print("{:.1f}%".format(100*(y*len(inp_initial)+x)/(len(inp_initial[0])*len(inp_initial))))
            inp = copy.deepcopy(inp_initial)
            guard = copy.deepcopy(guard_initial)
            loop = copy.deepcopy(loop_initial)
            inp[y][x] = '#'

            while True:
                simres = sim(inp, guard, loop)
                if simres == 2:
                    result += 1
                    print(f"res found at {x, y}")
                    break
                if simres == 1:
                    break

    return result

# returns true if outside grid
def sim(grid, guard: Guard, loop=None) -> int:
    # Check if we are in a loop
    # The guard is stuck if it is in a previous position with the same dir
    if loop:
        if guard.dir in loop[guard.y][guard.x]:
            return 2
        # Add guard dir and pos to loop
        loop[guard.y][guard.x].append(guard.dir)

    # Mark current pos as X
    grid[guard.y][guard.x] = 'X'

    dx,dy = get_dxdy(guard.dir)
    newx, newy = guard.x+dx, guard.y+dy

    # Check if outside 
    if newx >= len(grid[0]) or newy >= len(grid) or newx < 0 or newy < 0:
        return 1

    # Update guard position
    if grid[newy][newx] == '#':
        # Update direction on obstacle
        guard.dir = get_next_dir(guard.dir)
    
    # Possible new dir
    dx,dy = get_dxdy(guard.dir)
    newx, newy = guard.x+dx, guard.y+dy

    # Step forward
    guard.x = newx
    guard.y = newy

    return 0

def get_next_dir(dir):
    return dirs[(dirs.index(dir) + 1) % len(dirs)] 

def get_dxdy(dir) -> (int,int):
    if dir == '^': return (0,-1)
    if dir == '>': return (1,0)
    if dir == 'v': return (0,1)
    if dir == '<': return (-1,0)

def inp_lines():
    return open(input, 'r').readlines();

def inp_line():
    return open(input, 'r').read();

if __name__ == "__main__":
    print(f"{os.path.basename(pathlib.Path(__file__).parent.resolve())}")
    print(f"---------------------")
    print(f"p1: {p1()}")
    print(f"p2: {p2()}")
