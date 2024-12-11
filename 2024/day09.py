def part_a(s):
    file_id = 0
    drive = []
    for i in range(len(s)):
        if i % 2 == 0:
            drive += [file_id] * s[i]
            file_id += 1
        else:
            drive += [-1] * s[i]
    
    l, r = 0, len(drive) - 1
    while l < r:
        if drive[l] >= 0: l += 1
        if drive[r] <  0: r -= 1
        if drive[l] < 0 and drive[r] >= 0:
            drive[l], drive[r] = drive[r], drive[l]

    solA = 0
    for i in range(len(drive)):
        solA += drive[i] * i if drive[i] >= 0 else 0

    print(solA)

def part_b(s):
    file_id = 0
    files = []
    free = []
    address = 0
    for j in range(len(s)):
        block_address = (address, address + s[j] - 1)
        if j % 2 == 0 :
            files.append((file_id, block_address))
            file_id += 1
        else:
            free.append(block_address)
        address += s[j]

    files.reverse()
    for i in range(len(files)):
        f = files[i]
        for j in range(len(free)):
            file_id, file_address = f
            free_address = free[j]

            if free_address[0] > file_address[0]:
                break

            file_size = file_address[1] - file_address[0] + 1
            free_size = free_address[1] - free_address[0] + 1

            if file_size <= free_size:
                file_address = (free_address[0], free_address[0] + file_size - 1)
                files[i] = (file_id, file_address)
                free[j] = (file_address[1] + 1, free_address[1])
                break

    solB = 0
    for f in files:
        file_id, address = f
        a, l = address
        n = l - a + 1
        solB += file_id * (a + l) * n // 2
    
    print(solB)

filename = './inputs/day09.in'
with open(filename, 'r') as f:
    s = list(int(c) for c in f.read().strip())
    part_a(s)
    part_b(s)
