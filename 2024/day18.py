from queue import Queue

def dfs(g):
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    R = len(g)
    C = len(g[0])
    q = Queue()
    u = (0, 0)
    visited = {u : 0}
    q.put(u)
    while not q.empty():
        u = q.get()
        for d in directions:
            r, c = u
            dr, dc = d
            rr = r + dr
            cc = c + dc
            v = (r + dr, c + dc)

            if 0 <= rr < R and 0 <= cc < C and v not in visited and g[rr][cc] == '.':
                visited[v] = visited[u] + 1
                q.put(v)
    
    return visited

if __name__ == '__main__':
    g = [['.'] * 71 for _ in range(71)]
    filename = './inputs/day18.in'
    with open(filename, 'r') as f:
        positions = [(int(a), int(b)) for a, b in [s.split(',') for s in f.readlines()]]

        for i, p in enumerate(positions):
            c, r = p
            g[r][c] = '#'

            if i == 1023:
                steps = dfs(g)
                print(f'Solution to part A = {steps[(70, 70)]}.')
            elif i >= 1024:
                steps = dfs(g)
                if (70, 70) not in steps:
                    print(f'Solution to part B = {p}')
                    break
