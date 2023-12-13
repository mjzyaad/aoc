'''
Advent of code day 09: https://adventofcode.com/2023/day/9
'''

filename = './inputs/day09_mirage_maintenance.in'
sum_part_one = 0
sum_part_two = 0

with open(filename, 'r') as f:
    for line in f.readlines():
        ls = list(map(int, line.split()))

        first_numbers = [ls[0]]
        last_numbers  = [ls[-1]]
        while any(n != 0 for n in ls):
            ls_tmp = []
            for i in range(1, len(ls)):
                diff = ls[i] - ls[i-1]
                ls_tmp.append(diff)
            
            ls = ls_tmp
            first_numbers.append(ls[0])
            last_numbers.append(ls[-1])

        last_numbers = list(reversed(last_numbers))
        first_numbers = list(reversed(first_numbers))
        first = 0
        last  = 0
        for i in range(len(last_numbers)):
            last = last + last_numbers[i]
            first = first_numbers[i] - first
        sum_part_one += last
        sum_part_two += first

print(sum_part_one)
print(sum_part_two)
