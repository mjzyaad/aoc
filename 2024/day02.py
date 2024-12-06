filename = './inputs/day02.in'

def is_safe(ls):
    safe = ls == sorted(ls) or ls == sorted(ls, reverse=True)

    for i in range(1, len(ls)):
        diff = abs(ls[i] - ls[i-1])
        if diff < 1 or diff > 3:
            safe = False

    return safe


with open(filename, 'r') as f:
    ls = []
    safe_counter_A = 0
    safe_counter_B = 0

    for s in f.readlines():
        ls = list(map(int, s.split()))
        if is_safe(ls):
            safe_counter_A += 1
            safe_counter_B += 1
        else:
            for i in range(len(ls)):
                x = ls.pop(i)
                if is_safe(ls):
                    safe_counter_B += 1
                    break
                ls.insert(i, x)

    print(safe_counter_A)
    print(safe_counter_B)
