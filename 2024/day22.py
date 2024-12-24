mix = lambda value, secret : value ^ secret
prune = lambda value : value % 16777216

sol_a = 0
filename = './inputs/day22.in'
secrets = []
with open(filename, 'r') as f:
    for secret in [int(s) for s in f.readlines()]:
        ls = [secret]
        for _ in range(2000):
            secret = prune(mix(secret * 64, secret))
            secret = prune(mix(secret // 32, secret))
            secret = prune(mix(secret * 2048, secret))
            ls.append(secret)
        sol_a += secret
        secrets.append(ls)

print(f'Answer to part A = {sol_a}')

dict = {}
for i, secret in enumerate(secrets):
    price_changes = [x % 10 - secret[i - 1] % 10 for i, x in enumerate(secret)][1:]
    visited = set()
    for j in range(len(price_changes) - 3):
        sub = tuple(price_changes[j:j + 4])
        if sub not in visited:
            visited.add(sub)
            if sub not in dict:
                dict[sub] = secret[j + 4] % 10
            else:
                dict[sub] += secret[j + 4] % 10

sol_b = max(dict.values())
print(f'Answer to part B = {sol_b}')
