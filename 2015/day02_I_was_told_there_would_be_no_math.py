import itertools as it
from functools import reduce
from operator import mul
from operator import add

filename = './inputs/day02_I_was_told_there_would_be_no_math.in'

with open(filename, 'r') as f:
    total_sq_feet = 0
    ribbon_length = 0
    for s in f.readlines():
        dimensions = list(map(int, s.split('x')))
        x = list(it.combinations(dimensions, 2))
        
        #   Part one
        total_sq_feet += sum(it.starmap(mul, x)) * 2 + min(it.starmap(mul, x))

        #   Part two
        ribbon_length += min(it.starmap(add, x)) * 2 + reduce(mul, dimensions)

    print('Answer to part 1 = ', total_sq_feet)
    print('Answer to part 2 = ', ribbon_length)
