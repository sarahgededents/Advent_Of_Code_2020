import more_itertools as mi

with open("input", "r") as inp:
    adapters = [0] + sorted([int(adapt) for adapt in inp])
    adapters.append(adapters[-1] + 3)
    c_1 = []
    c_2 = []
    c_3 = []
    for a, b in mi.pairwise(adapters):
        if abs(a - b) == 1:
            c_1.append(a)
        if abs(a - b) == 2:
            c_2.append(a)
        if abs(a - b) == 3:
            c_3.append(a)
    print(c_1, c_2, c_3)



    c = [1] + [0] * adapters[-1]
    for adapt in adapters[1:]:
        c[adapt] = sum(c[max(0,adapt-3):adapt])
    print(c[-1])
