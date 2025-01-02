filename = './inputs/day04.in'
with open(filename, 'r') as f:
    pass_phrases = f.read().splitlines()

sol_a = 0
sol_b = 0
for pass_phrase in pass_phrases:
    words = pass_phrase.split()
    sol_a += len(words) == len(set(words))
    sol_b += len(words) == len(set([''.join(sorted(s)) for s in words]))

print(f'Solution to part A = {sol_a}')
print(f'Solution to part B = {sol_b}')
