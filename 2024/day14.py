import re

def display(moves, positions):
    print(f'After {moves + 1} moves:')
    coordinates = set([(x,y) for x, y, _, _ in positions])
    for i in range(103):
        for j in range(101):
            if (j, i) in coordinates:
                print('*', end="")
            else:
                print('.', end='')
        print()
    print('-' * 125)

filename = './inputs/day14.in'
with open(filename, 'r') as f:
    input = f.readlines()
    positions = [list(map(int, re.findall(r'-{0,1}\d+', s))) for s in input]

width = 101
breadth = 103
for moves in range(10000):
    for i, p in enumerate(positions):
        x, y, vx, vy = p
        new_x = x + vx
        new_y = y + vy
        if new_x < 0: new_x = width + new_x
        if new_y < 0: new_y = breadth + new_y
        if new_x >= width: new_x = new_x - width
        if new_y >= breadth: new_y = new_y - breadth
        positions[i] = [new_x, new_y, vx, vy]

    display(moves, positions)

mid_x = width // 2
mid_y = breadth // 2
quadrant_a = 0
quadrant_b = 0
quadrant_c = 0
quadrant_d = 0
for p in positions:
    quadrant_a += 1 if 0 <= x < mid_x and 0 <= y < mid_y else 0
    quadrant_b += 1 if mid_x < x < width and 0 <= y < mid_y else 0
    quadrant_c += 1 if 0 <= x < mid_x and mid_y < y < breadth else 0
    quadrant_d += 1 if mid_x < x < width and mid_y < y < breadth else 0

sol_a = quadrant_a * quadrant_b * quadrant_c * quadrant_d
print(sol_a)

#   For the solution to part B, output a simulation to a text file using command:
#   python3 day14.py > day14.out
#   Once the output file is generated, search for 10 consecutive '*' manually.
