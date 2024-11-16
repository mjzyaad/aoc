import itertools as it
from itertools import groupby

filename = './inputs/day05_Doesnt_He_Have_Intern_Elves_For_This.in'

def part_1(s):
    forbidden_words = ['ab', 'cd', 'pq', 'xy']

    is_nice_string = len(list(filter(lambda x : x in 'aeiou', s))) >= 3
    if len([k for k, g in groupby(s) if len(list(g)) > 1]) == 0 : is_nice_string = False
    if any(forbidden_word in s for forbidden_word in forbidden_words): is_nice_string = False

    return is_nice_string

def part_2(s):
    #   Condition 1:
    #   It contains a pair of any two letters that appears
    #   at least twice in the string without overlapping,
    #   like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    condition_a = False
    pairs = zip(s, s[1:])
    for x in pairs:
        t = ''.join(x)
        if s.count(t) > 1:
            condition_a = True
            break
        
    #   Condition 2:
    #   It contains at least one letter which repeats with exactly one
    #   letter between them, like xyx, abcdefeghi (efe), or even aaa.
    condition_b = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            condition_b = True
            break
    
    return condition_a and condition_b

if __name__ == '__main__':
    nice_string_count_1 = 0
    nice_string_count_2 = 0

    with open(filename, 'r') as f:
        for s in f.readlines():
            if part_1(s) == True: nice_string_count_1 += 1
            if part_2(s) == True: nice_string_count_2 += 1

print('Solution to part 1:', nice_string_count_1)
print('Solution to part 2:', nice_string_count_2)
