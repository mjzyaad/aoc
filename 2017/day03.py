def get_number(grid, row, col):
    total = 0
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
    for d in directions:
        dr, dc = d
        rr = row + dr
        cc = col + dc
        if (rr, cc) in grid:
            total += grid[(rr, cc)]
    
    return total

if __name__ == '__main__':
    stop = 312051
    directions = [(0, +1), (-1, 0), (0, -1), (+1, 0)]   #   right, top, left, bottom
    steps = [1, 1, 2, 2]
    number = 1
    row, col = 0, 0
    idx = 0
    grid = {(0,0): 1}
    sol_a = sol_b = None
    while sol_a is None or sol_b is None:
        for i in range(steps[idx]):
            d_row, d_col = directions[idx]
            row += d_row
            col += d_col
            number += 1
            grid[(row, col)] = get_number(grid, row, col)

            if number == stop:
                sol_a = abs(row) + abs(col)
            
            if sol_b is None and grid[(row, col)] > stop:
                sol_b = grid[(row, col)]

        steps[idx] += 2
        idx = (idx + 1) % 4

    print(f'Solution to part A = {sol_a}')
    print(f'Solution to part B = {sol_b}')
