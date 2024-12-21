import functools

filename = './inputs/day19.in'
with open(filename, 'r') as f:
    options, patterns = f.read().split('\n\n')
    options = options.split(', ')
    patterns = patterns.splitlines()

@functools.cache
def make_pattern(pattern):
    if pattern == '': return 1

    r = 0
    for opt in options:
        if pattern.endswith(opt):
            r += make_pattern(pattern.removesuffix(opt))
    
    return r

sol_a = 0
for p in patterns:
    sol_a += make_pattern(p)

print(sol_a)
