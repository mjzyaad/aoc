filename = './inputs/day01.in'
with open(filename, 'r') as f:
    elf_calories = [map(int, str_calories.split()) for str_calories in f.read().split('\n\n')]

calories_sum = [sum(c) for c in elf_calories]
print(max(calories_sum))
print(sum(sorted(calories_sum, reverse=True)[:3]))
