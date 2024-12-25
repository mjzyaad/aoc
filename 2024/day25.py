import sys

def get_num(a):
    num = ''
    for j in range(len(a[0])):
        count = 0
        for i in range(len(a)):
            if a[i][j] == '#':
                count += 1
        num += str(count)
    return num

if __name__ == '__main__':
    filename = './inputs/day25.in'

    with open(filename, 'r') as f:
        inputs = f.read().split('\n\n')
    
    locks = set()
    keys = set()
    for x in inputs:
        num = get_num(x.splitlines())
        if x.startswith('#'):
            locks.add(num)
        else:
            keys.add(num)
        
    sol_a = 0
    for lock in locks:
        for key in keys:
            sol_a += all([int(x) + int(y) <= 7 for x,y in zip(lock, key)])

    print(sol_a)