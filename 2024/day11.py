from functools import cache

@cache
def f(n, i):
    if i == 0:
        return 1
    if n == 0:
        return f(1, i - 1)
    elif len(str(n)) % 2 == 0:
        s = str(n)
        mid = len(s) // 2
        return f(int(s[:mid]), i - 1) + f(int(s[mid:]), i - 1)
    else:
        return f(n * 2024, i - 1)

# s = '125 17'
s = '5 62914 65 972 0 805922 6521 1639064'

nums = [int(x) for x in s.split()]
print('Solution to part A:', sum(f(n, 25) for n in nums))
print('Solution to part B:', sum(f(n, 75) for n in nums))
