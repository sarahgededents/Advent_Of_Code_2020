def seat_id(boarding):
    rows = list(range(128))
    cols = list(range(8))
    for i in boarding:
        if i == 'F':
            rows = rows[:len(rows)//2]
        if i == 'B':
            rows = rows[len(rows)//2:]
        if i == 'L':
            cols = cols[:len(cols)//2]
        if i == 'R':
            cols = cols[len(cols)//2:]
    row = min(rows)
    col = max(cols)
    return row * 8 + col

def high_id(inp):
    high = 0
    for boarding in inp:
        id = seat_id(boarding)
        high = max(high, id)
    return high

def get_seat(inp):
    all_ids = sorted([seat_id(i) for i in inp])
    i = min(all_ids)
    while i in all_ids:
        i += 1
    return i

with open("input", "r") as inp:
    print(get_seat(inp))
