from itertools import permutations

if __name__ == '__main__':
    filename = './inputs/day02.in'
    with open(filename, 'r') as f:
        spreadsheet = [list(map(int, s.split())) for s in f.readlines()]
    
    sol_a = sum([max(line) - min(line) for line in spreadsheet])

    sol_b = 0
    for line in spreadsheet:
        for a, b in permutations(line, 2):
            if a > b and b != 0 and a % b == 0:
                    sol_b += a // b

print(f'Solution to part A is {sol_a}')
print(f'Solution to part B is {sol_b}')