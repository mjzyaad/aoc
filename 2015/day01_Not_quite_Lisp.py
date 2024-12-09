filename = './inputs/day01_Not_quite_Lisp.in'
with open(filename, 'r') as f:
    s = f.read()

    sol_A = s.count('(') - s.count(')')
    
    floor = 0
    sol_B = 0
    for c in s:
        sol_B += 1
        floor += 1 if c == '(' else -1
        if floor == -1: break

    print(sol_A)
    print(sol_B)
