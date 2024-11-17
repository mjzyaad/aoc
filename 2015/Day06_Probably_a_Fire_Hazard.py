import re

filename = './inputs/Day06_Probably_a_Fire_Hazard.in'

grid_1 = [[False for r in range(1000)] for c in range(1000)]
grid_2 = [[0 for r in range(1000)] for c in range(1000)]

with open(filename, 'r') as f:
    for s in f.readlines():
        positions = list(map(int, re.findall('\d+', s)))
        top_left = (positions[0], positions[1])
        bottom_right = (positions[2], positions[3])

        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                if s.startswith('turn on'):
                    grid_1[i][j] = True
                    grid_2[i][j] += 1
                elif s.startswith('turn off'):
                    grid_1[i][j] = False
                    grid_2[i][j] = max(0, grid_2[i][j] - 1)
                else:
                    grid_1[i][j] = True if grid_1[i][j] == False else False
                    grid_2[i][j] += 2


    lights_on = 0
    brightness = 0
    for i in range(1000):
        for j in range(1000):
            if grid_1[i][j] == True: lights_on += 1
            brightness += grid_2[i][j]

    print('Solution to part 1:', lights_on)
    print('Solution to part 2:', brightness)
