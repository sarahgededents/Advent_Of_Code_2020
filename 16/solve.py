import numpy as np

with open("input") as inp:
    inp = [line.strip() for line in inp]

rules = {}
for rule in inp[:20]: #til zone
    fields = rule.split(': ')
    field_name = fields[0]
    ranges = [tuple(map(int, i.split('-'))) for i in fields[1].split(' or ')]
    for i in range(len(ranges)):
        ranges[i] = range(ranges[i][0], ranges[i][1] + 1)
    rules[field_name] = ranges

def get_min_max(rules):
    return range(min([c for r in rules.values() for c in r], key=lambda r: r.start).start, max([c for r in rules.values() for c in r], key=lambda r: r.stop).stop)


error_rate = 0
nearby_tickets = [[int(nb) for nb in i.split(',')] for i in inp[25:]]
for c, ticket in enumerate(nearby_tickets):
    error_rate += sum(field for field in ticket if field not in get_min_max(rules))

valid_tickets = [ticket for ticket in nearby_tickets if all(field in get_min_max(rules) for field in ticket)]

def valid(rule, col_value):
    return all((val in rule[0] or val in rule[1]) for val in col_value)

rulenames = list(rules)
my_ticket = [int(i) for i in inp[22].split(',')]
to_confirm = np.ndarray((len(rulenames), len(my_ticket)), dtype=int)
transpose_valid_tickets = np.array(valid_tickets).T.tolist()
for j, col_values in enumerate(transpose_valid_tickets):
    for i, rulename in enumerate(rulenames):
        to_confirm[i, j] = valid(rules[rulename], col_values)

confirm = [None] * len(my_ticket)
for _ in confirm:
    row = np.where(np.sum(to_confirm, axis=1) == 1)[0][0]
    line = to_confirm[row]
    col = np.where(line == 1)[0][0]
    confirm[col] = rulenames[row]
    to_confirm -= line

def where_departure(confirm, my_ticket):
    res = 1
    for field, name in zip(my_ticket, confirm):
        if name.startswith('departure'):
            res *= field
    return res

print("Part 1: ", error_rate)
print("Part 2: ", where_departure(confirm, my_ticket))