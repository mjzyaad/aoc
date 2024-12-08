filename = './inputs/day05.in'

with open(filename, 'r') as f:
    order_rules, page_number_updates = f.read().split('\n\n')

g = {}
for order_rule in order_rules.split():
    #   Read page dependencies and build an adjacency list
    u,v = tuple(map(int, order_rule.strip().split('|')))
    if (u in g):
        g[u].add(v)
    else:
        g[u] = {v}

# pp.pprint(g)

part_a_sol = 0
part_b_sol = 0
page_numbers = page_number_updates.splitlines()
for numbers in page_numbers:
    valid_sequence = True
    pages = list(map(int, numbers.split(',')))        
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            u = pages[i]
            v = pages[j]
            if v in g and u in g[v]:
                valid_sequence = False
                pages[i], pages[j] = pages[j], pages[i]
            

    mid_page = pages[len(pages) // 2]
    if valid_sequence:
        part_a_sol += mid_page
    else:
        part_b_sol += mid_page

print(part_a_sol)
print(part_b_sol)