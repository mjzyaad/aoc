import re

filename = './inputs/day03.in'
sol_part_A = 0
sol_part_B = 0
enable_mul = True

with open(filename, 'r') as f:
    for s in f.readlines():
        # x = re.findall('mul\((\d+),(\d+)\)', s)
        # sol_part_A += sum(int(a) * int(b) for a, b in x)

        for match in re.findall('(mul\(\d+,\d+\)|don\'t\(\)|do\(\))', s):
            if match == 'do()':
                enable_mul = True
            elif match == "don't()":
                enable_mul = False
            else:
                a, b = re.findall('\d+', match)
                sol_part_A += int(a) * int(b)
                if enable_mul: sol_part_B += int(a) * int(b)

print(sol_part_A)
print(sol_part_B)