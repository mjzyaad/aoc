filename = './inputs/day08.in'
with open (filename, 'r') as f:
    g = [line.strip() for line in f.readlines()]

r = len(g)
c = len(g[0])
mp = {}
antenna_pos = set()
for i in range(r):
    for j in range(c):
        if g[i][j] != '.':
            antenna = g[i][j]
            antenna_pos.add((i,j))
            if antenna in mp:
                mp[antenna].append((i,j))
            else:
                mp[antenna] = [(i,j)]

antinodes_A = set()
antinodes_B = set()
for antenna in mp:
    f = len(mp[antenna])
    for i in range(f):
        for j in range(i +1, f):
            r1, c1 = mp[antenna][i]
            r2, c2 = mp[antenna][j]
            dr = r1 - r2
            dc = c1 - c2

            #   Part A
            if 0 <= r1 + dr < r and 0 <= c1 + dc < c:
                antinodes_A.add((r1 + dr, c1 + dc))
            if 0 <= r2 - dr < r and 0 <= c2 - dc < c:
                antinodes_A.add((r2 - dr, c2 - dc))

            #   Part B
            r1B, c1B = r1, c1
            while 0 <= r1B + dr < r and 0 <= c1B + dc < c:
                r1B = r1B + dr
                c1B = c1B + dc
                antinodes_B.add((r1B, c1B))
            
            r2B, c2B = r2, c2
            while 0 <= r2B - dr < r and 0 <= c2B - dc < c:
                r2B = r2B - dr
                c2B = c2B - dc
                antinodes_B.add((r2B, c2B))

print(len(antinodes_A))
print(len(antinodes_B.union(antenna_pos)))
