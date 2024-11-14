filename = './inputs/day03_Perfectly_Spherical_Houses_in_a_Vacuum.in'

def get_visited_houses(s):
    x, y = 0, 0
    houses = { (x , y) }
    for c in s:
        if c == '^': y += 1
        elif c == 'v': y -= 1
        elif c == '>': x += 1
        else: x -= 1

        houses.add((x,y))

    return houses

with open(filename, 'r') as f:
    moves = f.readline()

    #   part one
    houses_1 = get_visited_houses(moves)
    print('Answer to part 1 =', len(houses_1))

    #   part two
    moves_santa = moves[::2]
    houses_santa = get_visited_houses(moves_santa)
    
    moves_robot = moves[1::2]
    houses_robot = get_visited_houses(moves_robot)

    houses_2 = houses_santa.union(houses_robot)
    print('Answer to part 2 =', len(houses_2))
