import re

filename = './inputs/day13.in'

def solve(aX, aY, bX, bY, cX, cY):
    # Solving using simultaneous equation
    sol = 0
    if (cY*aX - aY*cX) % (bY*aX - bX*aY) == 0:
        B = (cY*aX - aY*cX) // (bY*aX - bX*aY)
        if (cX - B*bX) % aX == 0:
            A = (cX - B*bX) // aX
            sol += 3*A + B
    
    return sol

with open(filename, 'r') as f:
    input = f.read().split('\n\n')

    solA = 0
    solB = 0
    for section in input:
        nums = re.findall(r'\d+', section)
        aX, aY, bX, bY, cX, cY = [int(n) for n in nums]

        # bestCost = math.inf
        # found = False
        # for i in range(101):
        #     for j in range(101):
        #         posX = aX * i + bX * j
        #         posY = aY * i + bY * j

        #         if (posX, posY) == (cX, cY):
        #             found = True
        #             bestCost = min(bestCost, 3 * i + j)
        #             print(found, i, j)
        # solA += bestCost if found else 0

        solA += solve(aX, aY, bX, bY, cX, cY)
        solB += solve(aX, aY, bX, bY, 10000000000000 + cX, 10000000000000 + cY)

print(f'Solution to part A = {solA}')
print(f'Solution to part B = {solB}')
