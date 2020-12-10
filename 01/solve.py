import functools
import itertools
import operator

def solve2(file):
    seen = set()
    for val in map(int, file):
        diff = 2020 - val
        if diff in seen:
            assert val + diff == 2020
            return val * diff
        seen.add(val)

def solve3(file):
    for a, b, c in itertools.combinations(map(int, file), 3):
        if a + b + c == 2020:
            return a * b * c

def solve(file, n):
    for vals in itertools.combinations(map(int, file), n):
        if sum(vals) == 2020:
            return functools.reduce(operator.mul, vals)

with open("input", "r") as inp:
    print(solve3(inp))
with open("input", "r") as inp:
    print(solve(inp, 3))
with open("input", "r") as inp:
    print(solve2(inp))
with open("input", "r") as inp:
    print(solve(inp, 2))