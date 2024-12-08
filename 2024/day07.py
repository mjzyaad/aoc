filename = './inputs/day07.in'

def can_reach_target(target, calculation, numbers, operators):
    if numbers == []:
        return calculation == target
    
    for op in operators:
        if can_reach_target(target, eval(f'{calculation}{op}{numbers[0]}'), numbers[1:], operators):
            return True

    return False

if __name__ == '__main__':
    sol_A = 0
    sol_B = 0
    with open(filename, 'r') as f:
        for s in f.readlines():
            #   Extract input
            ls_num = list(map(int, s.replace(':', '').split(' ')))
            target = ls_num[0]
            numbers = ls_num[1:]

            #   Check if we can reach the target calculation
            #   replace concatenation '||' with '' to be used with eval
            if can_reach_target(target, numbers[0], numbers[1:], ['+', '*']):
                sol_A += target
                sol_B += target
            elif can_reach_target(target, numbers[0], numbers[1:], ['+', '*', '']):
                sol_B += target

    print(sol_A)
    print(sol_B)
