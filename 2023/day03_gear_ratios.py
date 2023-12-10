import pprint 

pp = pprint.PrettyPrinter()

filename = './inputs/day03_gear_ratios.in'

def get_number(row, col, max_row, max_col, grid):
    if row < 0 or col < 0: return 0
    if row > max_row or col > max_col: return 0
    if not grid[row][col].isdigit(): return 0

    str_number = ''

    # scan to the left
    j = col
    while (j >= 0 and grid[row][j].isdigit()):
        str_number = grid[row][j] + str_number
        grid[row][j] = '.'
        j = j - 1
    
    # scan to the right
    j = col + 1
    while (j <= max_row and grid[row][j].isdigit()):
        str_number = str_number + grid[row][j]
        grid[row][j] = '.'
        j = j + 1

    number = int(str_number)
    return number

def part_one():
    sum = 0
    with open(filename, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line.strip()))

        height = len(grid)
        width  = len(grid[0])
        for i in range(height):
            for j in range(width):
                if not grid[i][j].isdigit() and not grid[i][j] == '.':
                    grid[i][j] = '.'
                    sum += get_number(i - 1, j    , height - 1, width - 1, grid)
                    sum += get_number(i + 1, j    , height - 1, width - 1, grid)
                    sum += get_number(i    , j - 1, height - 1, width - 1, grid)
                    sum += get_number(i    , j + 1, height - 1, width - 1, grid)
                    sum += get_number(i - 1, j - 1, height - 1, width - 1, grid)
                    sum += get_number(i - 1, j + 1, height - 1, width - 1, grid)
                    sum += get_number(i + 1, j - 1, height - 1, width - 1, grid)
                    sum += get_number(i + 1, j + 1, height - 1, width - 1, grid)

        #pp.pprint(grid)
        print('Answer to part 1 =', sum)

def part_two():
    sum = 0
    with open(filename, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line.strip()))

        height = len(grid)
        width  = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '*':
                    grid[i][j] = '.'
                    numbers = []
                    numbers.append(get_number(i - 1, j    , height - 1, width - 1, grid))
                    numbers.append(get_number(i + 1, j    , height - 1, width - 1, grid))
                    numbers.append(get_number(i    , j - 1, height - 1, width - 1, grid))
                    numbers.append(get_number(i    , j + 1, height - 1, width - 1, grid))
                    numbers.append(get_number(i - 1, j - 1, height - 1, width - 1, grid))
                    numbers.append(get_number(i - 1, j + 1, height - 1, width - 1, grid))
                    numbers.append(get_number(i + 1, j - 1, height - 1, width - 1, grid))
                    numbers.append(get_number(i + 1, j + 1, height - 1, width - 1, grid))

                    numbers = list(filter(lambda x : x > 0, numbers))
                    if len(numbers) == 2:
                        sum += numbers[0] * numbers[1]

        #pp.pprint(grid)
        print('Answer to part 2 =', sum)

if __name__ == '__main__':
    #part_one()
    part_two()
