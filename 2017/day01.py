def solve(s, step):
    r = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == s[i-step]:
            r += int(s[i])
    return r

if __name__ == '__main__':
    filename = './inputs/day01.in'
    with open(filename, 'r') as f:
        s = f.readline()

    print(f'Solution to part A = {solve(s, 1)}')
    print(f'Solution to part A = {solve(s, len(s) // 2)}')
