filename = './inputs/day04.in'

def search_word(word, grid, r, c, direction):
    #   check if the word exists at position (r, c) in the grid
    #   by searching in the direction 'direction'
    delta_r, delta_c = direction
    for i in range(len(word)):
        # if 0 > r >= len(grid) or 0 > c >= len(grid[0]): return False
        if r < 0 or r >= len(grid): return False
        if c < 0 or c >= len(grid[0]): return False
        if grid[r][c] != word[i]: return False

        r += delta_r
        c += delta_c
    
    return True

if __name__ == '__main__':
    with open(filename, 'r') as f:
        grid = f.read().splitlines()

    directions = [(-1,0), (+1,0), (0,-1), (0,+1), (-1,-1), (-1,+1), (+1,-1), (+1,+1)]

    sol_A = 0
    sol_B = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in directions:
                sol_A += search_word('XMAS', grid, r, c, d)

            sol_B += (search_word('MAS', grid, r, c, (+1,+1)) or search_word('SAM', grid, r, c, (+1,+1))) \
                 and (search_word('MAS', grid, r, c+2, (+1,-1)) or search_word('SAM', grid, r, c+2, (+1,-1)))
    
    print(sol_A)
    print(sol_B)
