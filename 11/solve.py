import itertools
from collections import Counter

def count_occupied_neighbours(layout, i, j):
    i_start = max(i - 1, 0)
    i_end = min(i + 2, len(layout))
    j_start = max(j - 1, 0)
    j_end = min(j + 2, len(layout[0]))
    neighbourhood = itertools.chain.from_iterable(line[j_start:j_end] for line in layout[i_start:i_end])
    return sum(seat == '#' for seat in neighbourhood) - (layout[i][j] == '#')

def count_occ(layout, i, j, di, dj):
    i += di
    j += dj
    while i in range(len(layout)) and j in range(len(layout[0])):
        if layout[i][j] == '#' or layout[i][j] == 'L':
            return layout[i][j] == '#'
        i += di
        j += dj
    return False

def new_count(layout, i, j):
    c = count_occ(layout, i, j, 1, 0)
    c += count_occ(layout, i, j, 1, 1)
    c += count_occ(layout, i, j, 0, 1)
    c += count_occ(layout, i, j, 1, -1)
    c += count_occ(layout, i, j, 0, -1)
    c += count_occ(layout, i, j, -1, -1)
    c += count_occ(layout, i, j, -1, 0)
    c += count_occ(layout, i, j, -1, 1)
    return c

def next_layout(layout, func):
    out = []
    if func == count_occupied_neighbours:
        max_seat_occ = 4
    if func == new_count:
        max_seat_occ = 5
    for i in range(len(layout)):
        line = []
        for j in range(len(layout[0])):
            if layout[i][j] == 'L' and func(layout, i, j) == 0:
                line.append('#')
            elif layout[i][j] == '#' and func(layout, i, j) >= max_seat_occ:
                line.append('L')
            else:
                line.append(layout[i][j])
        out.append(''.join(line))
    return out

def pl(layout):
    print('\n'.join(layout))

funcs = [count_occupied_neighbours, new_count]
for func in funcs:
    with open("input") as inp:
        layout = [seats.rstrip() for seats in inp]
        new_layout = next_layout(layout, func)
        while layout != new_layout:
            layout, new_layout = new_layout, next_layout(new_layout, func)
        print("occupied seats: ", Counter(itertools.chain.from_iterable((i) for i in new_layout))['#'])