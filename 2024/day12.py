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

# +-+-+-+-+
# |A A A A|
# +-+-+-+-+     +-+
#               |D|
# +-+-+   +-+   +-+
# |B B|   |C|
# +   +   + +-+
# |B B|   |C C|
# +-+-+   +-+ +
#           |C|
# +-+-+-+   +-+
# |E E E|
# +-+-+-+

def plot_sides(R, C, plant, plot):
    # How to detect a corner on a grid?
    # N, NE, E, SE, S, SW, W, NW
    corners = [(-1,0), (-1,+1), (0,+1), (+1,+1), (+1,0), (+1,-1), (0,-1), (-1,-1), (-1,0)]
    
    vertices = 0
    for (r, c) in plot:
        for i in range(4):
            deltas = corners[i * 2 : i * 2 +3]
            is_inner_corner = False
            is_outer_corner = False
            hv_inner = 0
            diag_inner = 0
            hv_outer = 0
            diag_outer = 0
            for j, d in enumerate(deltas):
                dr, dc = d
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

            if is_inner_corner == True or is_outer_corner == True:
                print(f'Plant {plant} : ({r},{c}) is a corner.  Inner corner = {is_inner_corner} [{hv_inner}, {diag_inner}], Outer corner = {is_outer_corner}. Deltas = {deltas}')

            vertices += (is_inner_corner or is_outer_corner)

    print(f'Region {plant} with {vertices} sides.')

    return vertices

R = len(g)
C = len(g[0])
plots = []
solA = 0
solB = 0
for i in range(R):
    for j in range(C):
        if (i, j) not in visited:
            plot = []
            dfs(R, C, g[i][j], i, j, plot)
            area = len(plot)
            perimeter = fence_perimeter(R, C, plot)
            # print(f'A region of {g[i][j]} plants with price {area} * {perimeter} = {area * perimeter}.')
            plots.append(plot)
            solA += area * perimeter
            # print(plot)
            sides = plot_sides(R, C, g[i][j], plot)
            solB += area * sides

print(f'Solution to part A = {solA}')
print(f'Solution to part B = {solB}')
