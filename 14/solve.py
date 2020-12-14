import itertools

def get_max_index(inp):
    return max([int(i[0][4:-1]) for i in inp if i[0] != 'mask'])

def calc_with_mask(value, mask):
    value = list(format(value, 'b').zfill(36)) # get 36 bits repr of value
    for bitpos in range(len(mask)):
        if mask[bitpos] != 'X':
            value[bitpos] = mask[bitpos]
    return int("".join(value), 2)

def calc_with_mask2(mem, mask):
    mem_val = list(format(mem, 'b').zfill(36))
    for bitpos in range(len(mask)):
        if mask[bitpos] == 'X' or mask[bitpos] == '1':
            mem_val[bitpos] = mask[bitpos]
    mem_val = "".join(mem_val)
    len_X = mem_val.count('X')
    combs = list(itertools.product([0, 1], repeat=len_X))
    mem = []
    for comb in combs:
        mem.append(int(mem_val.replace('X', '{}').format(*comb), 2))
    return mem


with open("input") as inp:
    inp = [line.strip().split(' = ') for line in inp]

mem = [0] * (get_max_index(inp) + 1) # to have sufficient value to put in memory
mask = 0
mem_val = {}
for i in inp:
    if i[0] == 'mask':
        mask = i[1]
        continue
    else:
        mem[int(i[0][4:-1])] = calc_with_mask(int(i[1]), mask)
        for val in calc_with_mask2(int(i[0][4:-1]), mask):
            mem_val[val] = int(i[1])

print("Part 1: ", sum(mem))
print("Part 2: ", sum(mem_val.values()))