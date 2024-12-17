filename = './inputs/day12.in'
with open(filename, 'r') as f:
    g = [s.strip() for s in f.readlines()]


visited = set()

def dfs(R, C, plant, i, j, plot):
    if 0 <= i < R and 0 <= j < C and (i, j) not in visited and g[i][j] == plant:
        visited.add((i, j))
        plot.append((i, j))
        dfs(R, C, plant, i + 1, j, plot)
        dfs(R, C, plant, i - 1, j, plot)
        dfs(R, C, plant, i, j + 1, plot)
        dfs(R, C, plant, i, j - 1, plot)

def fence_perimeter(R, C, plot):
    perimeter = 0
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    for (i, j) in plot:
        for dR, dC in directions:
            new_i = i + dR
            new_j = j + dC
            if 0 <= new_i < R and 0 <= new_j < C and g[i][j] != g[new_i][new_j]:
                perimeter += 1
            elif new_i < 0 or new_i >= R or new_j < 0 or new_j >= C:
                perimeter += 1
    return perimeter

def plot_sides(R, C, plant, plot):
    # Number of sides = number of corners.
    # How to detect a corner on a grid?
    # For a particular grid cell, there are are 2 types of corners:
    #   - inner corner
    #   - outer corner
    # To detect an inner corner, a cell should have 0 cells of same type in its horizontal and vertical directions
    # To detect an outer corner, a cell should have:
    #   - 2 cells in both horizontal and vertical directions
    #   - No cell in its diagonal

    # N, NE, E, SE, S, SW, W, NW
    corners = [(-1,0), (-1,+1), (0,+1), (+1,+1), (+1,0), (+1,-1), (0,-1), (-1,-1), (-1,0)]
    
    vertices = 0
    for (r, c) in plot:
        for i in range(4):
            deltas = corners[i * 2 : i * 2 +3]
            is_inner_corner = False
            is_outer_corner = False
            hv_inner, diag_inner = 0, 0
            hv_outer, diag_outer = 0, 0
            for j, delta in enumerate(deltas):
                dr, dc = delta
                new_r = r + dr
                new_c = c + dc

                if j % 2 == 0 and (new_r, new_c) in plot:      #   Horizontal and vertical checks
                        hv_inner += 1
                        hv_outer += 1
                elif j % 2 == 1 and (new_r, new_c) in plot:
                        diag_inner += 1
                        diag_outer += 1

            is_inner_corner |= hv_inner == 0
            is_outer_corner |= hv_outer == 2 and diag_outer == 0
            vertices += (is_inner_corner or is_outer_corner)

    return vertices

R = len(g)
C = len(g[0])
solA, solB = 0, 0
for i in range(R):
    for j in range(C):
        if (i, j) not in visited:
            plot = []
            dfs(R, C, g[i][j], i, j, plot)
            area = len(plot)
            perimeter = fence_perimeter(R, C, plot)
            sides = plot_sides(R, C, g[i][j], plot)
            solA += area * perimeter
            solB += area * sides

print(f'Solution to part A = {solA}')
print(f'Solution to part B = {solB}')
