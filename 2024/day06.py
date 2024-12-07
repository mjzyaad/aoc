def get_guard_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return (i, j)
    return (-1,-1)

def discover_grid(grid, guard_position, new_obstacle):
    #   In ordered sequence: up, right, down, left
    direction_index = 0     #   initially facing up
    directions = [(-1,0),(0,+1),(+1,0),(0,-1)]

    visit_states = set()
    positions = { guard_position }
    fall_out = False
    while (guard_position, direction_index) not in visit_states:
        visit_states.add((guard_position, direction_index))
        positions.add(guard_position)
        r,c = guard_position
        deltaR, deltaC = directions[direction_index]

        tmpR = r + deltaR
        tmpC = c + deltaC

        if tmpR < 0 or tmpR >= len(grid) or tmpC < 0 or tmpC >= len(grid[0]):
            fall_out = True
            break
        elif grid[tmpR][tmpC] == '#' or new_obstacle == (tmpR, tmpC):    #   turn clockwise
            direction_index = (direction_index + 1) % 4
        else:
            guard_position = (tmpR, tmpC)
    
    return (positions, fall_out)


filename = './inputs/day06.in'
with open(filename, 'r') as f:
    grid = f.read().splitlines()
    guard_position = get_guard_position(grid)

    # Part A
    discovered_positions, fall_out = discover_grid(grid, guard_position, (-1,-1))
    print(len(discovered_positions))

    # Part B
    obstacle_count = 0
    for new_obstacle in discovered_positions:
        if new_obstacle != guard_position:
            _, fall_out = discover_grid(grid, guard_position, new_obstacle)
            obstacle_count += not fall_out

    print(obstacle_count)
