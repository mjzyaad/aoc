from functools import reduce
from operator import concat
from os import system, name
from time import sleep
from colorama import Fore, Back

def clear():
    _ = system('cls') if name == 'nt' else system('clear')

def get_position(g, e):
    for i, s in enumerate(g):
        for j, c in enumerate(s):
            if c == e:
                return (i, j)

    return(-1, -1)

def can_move_robot(g, rr, rc, dr, dc):
    if g[rr][rc] == '#': return False
    if g[rr][rc] == '.': return True

    if g[rr][rc] in '@O' or dr == 0:
        return can_move_robot(g, rr + dr, rc + dc, dr, dc)
    elif g[rr][rc] == '[':
        return can_move_robot(g, rr + dr, rc + dc, dr, dc) and can_move_robot(g, rr + dr, rc + 1, dr, dc)
    elif g[rr][rc] == ']':
        return can_move_robot(g, rr + dr, rc + dc, dr, dc) and can_move_robot(g, rr + dr, rc - 1, dr, dc)

    return False

def move_robot(g, rr, rc, dr, dc):
    if g[rr][rc] in '.#': return
    
    if g[rr][rc] in '@O' or dr == 0:
        move_robot(g, rr + dr, rc + dc, dr, dc)
        g[rr][rc], g[rr + dr][rc + dc] = g[rr + dr][rc + dc], g[rr][rc]
    elif g[rr][rc] == '[' and dr in [+1, -1]:
        move_robot(g, rr + dr, rc + dc, dr, dc)
        move_robot(g, rr + dr, rc + 1,  dr, dc)
        g[rr][rc], g[rr + dr][rc + dc] = g[rr + dr][rc + dc], g[rr][rc]
        g[rr][rc + 1], g[rr + dr][rc + 1]  = g[rr + dr][rc + 1], g[rr][rc + 1]
    elif g[rr][rc] == ']' and dr in [+1, -1]:
        move_robot(g, rr + dr, rc + dc, dr, dc)
        move_robot(g, rr + dr, rc - 1,  dr, dc)
        g[rr][rc], g[rr + dr][rc + dc] = g[rr + dr][rc + dc], g[rr][rc]
        g[rr][rc - 1], g[rr + dr][rc - 1]  = g[rr + dr][rc - 1], g[rr][rc - 1]
    
def sum_gps(warehouse):
    sol = 0
    for i, x in enumerate(warehouse):
        for j, c in enumerate(x):
            if c in ['O','[']:
                sol += i * 100 + j

    return sol

def animate(title, warehouse):
    clear()
    print_warehouse(warehouse)
    sleep(0.05)
    
def simulate_moves(warehouse, to_animate):
    if to_animate:
        animate('Initial position of robot', warehouse)

    for i, m in enumerate(reduce(concat, moves)):
        robot = get_position(warehouse, '@')
        
        if   m == '>' : dr, dc = 0, +1
        elif m == '<' : dr, dc = 0, -1
        elif m == '^' : dr, dc = -1, 0
        elif m == 'v' : dr, dc = +1, 0
        else          : continue

        if can_move_robot(warehouse, robot[0], robot[1], dr, dc):
            move_robot(warehouse, robot[0], robot[1], dr, dc)

        if to_animate:
            animate(f'#{i}, moving {m}', warehouse)

    return sum_gps(warehouse)

def print_warehouse(warehouse):
    for s in warehouse:
        s = ''.join(s)
        s = s.replace('[', Back.GREEN + '[' + Back.RESET)
        s = s.replace(']', Back.GREEN + ']' + Back.RESET)
        s = s.replace('#', Back.LIGHTWHITE_EX + '#' + Back.RESET)
        s = s.replace('@', Back.RED + '@' + Back.RESET)
        s = s.replace('.', Fore.WHITE + '.' + Fore.RESET)

        print(s)

filename = './inputs/day15.in'
with open(filename, 'r') as f:
    part1, part2 = f.read().split('\n\n')
    warehouse_a = [list(x) for x in part1.splitlines()]
    warehouse_b = []
    for row in warehouse_a:
        x = ''
        for c in row:
            if   c == '#': x += '##'
            elif c == '.': x += '..'
            elif c == 'O': x += '[]'
            elif c == '@': x += '@.'

        warehouse_b.append(list(x))

    moves = part2.splitlines()

print(simulate_moves(warehouse_a, False))

print(simulate_moves(warehouse_b, False))
