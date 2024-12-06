from collections import Counter

filename = './inputs/day01.in'


lsA = []
lsB = []
with open(filename, 'r') as f:
    for s in f.readlines():
        a, b = map(int, s.split())
        lsA.append(a)
        lsB.append(b)

#   Part A
total_distance = 0
for a, b in zip(sorted(lsA), sorted(lsB)):
    total_distance += abs(a - b)

print('Solution to part 1: ', total_distance)

#   Part B
similarity_score = 0
mapA = Counter(lsA)
mapB = Counter(lsB)
for k in mapA:
    similarity_score += k * mapA[k] * mapB[k]

print('Solution to part 2: ', similarity_score)
