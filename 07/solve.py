def can_hold1(key, rules):
    children = rules[key]
    if 'shiny gold' in children:
        return key
    else:
        for child in children:
            if can_hold1(child, rules):
                return key
        return None

def can_hold(rules):
    shinys = set()
    for rule in rules:
        shiny = can_hold1(rule, rules)
        if shiny:
            shinys.add(shiny)
    return len(shinys)

def bag_count(key, rules):
    children = rules[key]
    counter = 1
    for child, count in children.items():
        counter += (bag_count(child, rules) * int(count))
    return counter

def bags(rules):
    return bag_count('shiny gold', rules) - 1

with open("input", "r") as inp:
    rules = {}
    for line in inp:
        line = line.replace("bags", "bag")
        line = line.replace("contain ", ":")
        line = line.replace(",", "")
        line = line.replace(".", " ")
        line = line.split(":")
        line[0] = line[0].split(" bag ")[0]
        line[1] = line[1].split(" bag ")[:-1]
        r = {}
        for rule in line[1]:
            rule = rule.split()
            bag = ' '.join(rule[1:])
            if bag != 'other':
                r[bag] = rule[0]
        rules[line[0]] = r
    #rules => {'bag':{'bag':number, ....}, 'bag1':{}}
    print(bags(rules))