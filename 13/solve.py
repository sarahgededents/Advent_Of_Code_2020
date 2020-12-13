import operator
from math import prod

def chinese_remainder(nums, rems):
    prod_N = prod(nums)
    sum_N = sum(rem * (prod_N // num) * pow(prod_N // num, -1, num) for num, rem in zip(nums, rems))
    return  sum_N % prod_N

with open("input") as inp:
    inp = [line.rstrip().split() for line in inp]
    depart = int(inp[0][0])
    ids = [i.split(',') for i in inp[1]][0]
    buses = {}
    for i, id in enumerate(ids):
        if id != 'x':
            buses[i] = int(id)

c = []
bus_ids = buses.values()
for id in bus_ids:
    c.append(id - depart % id)


print("Part 1: ", min(c) * list(bus_ids)[c.index(min(c))])
print("Part 2: ", chinese_remainder(buses.values(), map(operator.sub, list(bus_ids), list(buses.keys()))))