import operator
from math import prod
from collections import OrderedDict

def chinese_remainder(nums, rems):
    prod_N = prod(nums)
    sum_N = sum(rem * (prod_N // num) * pow(prod_N // num, -1, num) for num, rem in zip(nums, rems))
    return  sum_N % prod_N

with open("input") as inp:
    inp = [line.rstrip().split() for line in inp]
    depart = int(inp[0][0])
    ids = [i.split(',') for i in inp[1]][0]
    buses = OrderedDict()
    for i, id in enumerate(ids):
        if id != 'x':
            buses[i] = int(id)

c = [bid - depart % bid for bid in buses.values()]

print("Part 1: ", min(c) * list(buses.values())[c.index(min(c))])
print("Part 2: ", chinese_remainder(buses.values(), map(operator.sub, list(buses.values()), list(buses.keys()))))