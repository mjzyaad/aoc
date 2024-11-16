import hashlib

i = 0
secret_key = 'yzbqklnj'
sol_1 = 0
sol_2 = 0
while True:
    s = secret_key + str(i)
    md5 = hashlib.md5(s.encode()).hexdigest()
    if sol_1 == 0 and md5.startswith('00000'):
        sol_1 = i
    elif sol_2 == 0 and md5.startswith('000000'):
        sol_2 = i
    elif sol_1 > 0 and sol_2 > 0:
        break
    
    i += 1

print('Solution to part 1 =', sol_1)
print('Solution to part 2 =', sol_2)
