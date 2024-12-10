def hike(g, i, j, visited):
    if 0 <= i < len(g) and 0 <= j < len(g[0]):
        if g[i][j] == 9:
            visited.add((i,j))
            return (len(visited), 1)

        _, up    = hike(g, i - 1, j, visited) if i - 1 >= 0        and g[i-1][j] == g[i][j] + 1 else (0,0)
        _, down  = hike(g, i + 1, j, visited) if i + 1 < len(g)    and g[i+1][j] == g[i][j] + 1 else (0,0)
        _, left  = hike(g, i, j - 1, visited) if j - 1 >= 0        and g[i][j-1] == g[i][j] + 1 else (0,0)
        _, right = hike(g, i, j + 1, visited) if j + 1 < len(g[0]) and g[i][j+1] == g[i][j] + 1 else (0,0) 

        return (len(visited), up + down + left + right)

    return (len(visited), 0)


filename = './inputs/day10.in'
with open(filename, 'r') as f:
    input = f.read().splitlines()

    g = []
    for line in input:
        g.append([int(digit) for digit in line])

    solA = 0
    solB = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                a, b = hike(g, i, j, set())
                solA += a
                solB += b
    
    print(solA)
    print(solB)
