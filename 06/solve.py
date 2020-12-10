def yes_answer(group, ex):
    if ex == 1:
        return len(set(''.join(group)))
    else:
        sorted_group = [''.join(sorted(answer)) for answer in group]

        print(sorted_group)
        yes = []
        while sorted_group:
            sorted_group = sorted(sorted_group)
            print(sorted_group)
            if len(min(sorted_group, key=len)) < 1:
                break
            if len(set([x[0] for x in sorted_group])) == 1:
                yes.append(sorted_group[0][0])
                sorted_group = [s[1:] for s in sorted_group]
            else:
                sorted_group[0] = sorted_group[0][1:]
        return len(yes)


def total_count(groups, ex):
    count = 0
    for group in groups:
        count += yes_answer(group, ex)
    return count

with open("input", "r") as f:
    groups =[[]]
    for line in f:
        elmts = line.split()
        for elmt in elmts:
            groups[-1].append(elmt)
        if not elmts:
            groups.append([])
    print(total_count(groups, 1))
    print(total_count(groups, 2))
