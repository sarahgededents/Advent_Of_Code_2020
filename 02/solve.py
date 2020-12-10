def values(val):
    indices, letter, pwd = val.split()
    indices = map(int, indices.split('-'))
    letter = str(letter.strip(':'))
    return indices, letter, pwd

def is_valid_1(line):
    (mincount, maxcount), letter, pwd = values(line)
    return pwd.count(letter) in range(mincount, maxcount+1)

def is_valid_2(line):
    (idx, idx2), letter, pwd = values(line)
    return (letter == pwd[idx - 1]) ^ (letter == pwd[idx2 - 1])

def solve(iterable, predicate):
    return sum(map(predicate, iterable))

with open("input", "r") as inp:
    print(solve(inp, is_valid_1))

with open("input", "r") as inp:
    print(solve(inp, is_valid_2))