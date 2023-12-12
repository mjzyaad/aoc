'''
Advent of code day 08: https://adventofcode.com/2023/day/8
'''
import functools
import re
import pprint
from math import lcm

filename = './inputs/day08_haunted_wasteland.in'
pp = pprint.PrettyPrinter()

def to_nodes(s):
    rx = re.compile('\W+')
    res = rx.sub(' ', s)
    
    u, v_left, v_right = res.split()

    return (u, (v_left, v_right))

def get_graph():
    with open(filename, 'r') as f:
        directions, graph = f.read().split('\n\n')
        
    nodes = map(to_nodes, graph.splitlines())
    graph = dict(nodes)
    
    return (directions, graph)

def traverse_part_one(graph, directions, source, destination):
    u = source
    direction_index = 0
    steps = 0

    while u != destination:
        direction = directions[direction_index]
        v = graph[u][0] if direction == 'L' else graph[u][1]
        
        u = v
        direction_index = (direction_index + 1) % len(directions)
        steps += 1

    return steps

def traverse_part_two(graph, directions):
    direction_index = 0
    steps = 0
    u_nodes = list(filter(lambda x : x[-1] == 'A', graph))   

    ls_steps = []
    for u in u_nodes:
        direction_index = 0
        steps = 0

        while u[-1] != 'Z':
            direction = directions[direction_index]
            v = graph[u][0] if direction == 'L' else graph[u][1]
            
            u = v
            direction_index = (direction_index + 1) % len(directions)
            steps += 1

        ls_steps.append(steps)
        
    return lcm(*ls_steps)

if __name__ == '__main__':
    directions, graph = get_graph()
    
    # Part one
    print(traverse_part_one(graph, directions, 'AAA', 'ZZZ'))
    
    # part two
    print(traverse_part_two(graph, directions))
