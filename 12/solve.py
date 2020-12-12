def action(dir, value, ship_pos):
    if dir == "N":
        ship_pos[1] += value
    if dir == "S":
        ship_pos[1] += -value
    if dir == "E":
        ship_pos[0] += value
    if dir == "W":
        ship_pos[0] += -value
    return ship_pos

def change_dir(dir, value):
    if dir == "R":
        return value // 90
    if dir == "L":
        return -value // 90
    return 0

def rotation(wp, rot):
    if rot == 90:
        return [wp[1], -wp[0]]
    if rot == 180:
        return [-wp[0], -wp[1]]
    if rot == 270:
        return [-wp[1], wp[0]]
    return [wp[0], wp[1]]

with open("input") as inp:
    instructions = [line.rstrip() for line in inp]
    directions = 'ESWN'
    ship_dir = 0
    ship_pos = [0, 0]
    for val in instructions:
        dir, value = val[0], int(val[1:])
        ship_dir = (ship_dir + change_dir(dir, value)) % 4
        if dir == "F":
            dir = directions[ship_dir]
        ship_pos = action(dir, value, ship_pos)
    print("Manhattan distance: ", abs(ship_pos[0]) + abs(ship_pos[1]))

with open("input") as inp:
    instructions = [line.rstrip() for line in inp]
    directions = 'ESWN'
    wp = [10, 1]
    ship_pos = [0, 0]
    for val in instructions:
        dir, value = val[0], int(val[1:])
        if dir == "F":
            for i in range(len(ship_pos)):
                ship_pos[i] += wp[i] * value
        if dir in "LR":
            if dir == "L":
                wp = rotation(wp, -value%360)
            elif dir == "R":
                wp = rotation(wp, value%360)
        wp = action(dir, value, wp)
    print("Manhattan distance: ", abs(ship_pos[0]) + abs(ship_pos[1]))