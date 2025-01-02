def f(s, step):
    r = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == s[i-step]:
            r += int(s[i])
    return r

s = input()
print(f'Solution to part A = {f(s, 1)}')
print(f'Solution to part A = {f(s, len(s) // 2)}')
