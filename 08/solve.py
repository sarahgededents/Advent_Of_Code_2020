with open("input", 'r') as inp:
    lines = [line.rstrip() for line in inp]

    acc, idx = 0, 0
    potential_bugs, seen = [], []
    while idx not in seen:
        seen.append(idx)
        cmd, inc = lines[idx].split()
        inc = int(inc)
        if cmd == 'acc':
            acc += inc
            idx += 1
        if cmd == 'jmp':
            potential_bugs.append(idx)
            idx += inc
        if cmd == 'nop':
            potential_bugs.append(idx)
            idx += 1

    print(acc)

    for bug in potential_bugs:
        acc, idx = 0, 0
        seen = []
        while idx not in seen and idx < len(lines):
            seen.append(idx)

            cmd, inc = lines[idx].split()
            inc = int(inc)
            if idx == bug:
                if cmd == 'nop':
                    cmd = 'jmp'
                else:
                    cmd = 'nop'

            if cmd == 'acc':
                acc += inc
                idx += 1
            if cmd == 'jmp':
                potential_bugs.append(idx)
                idx += inc
            if cmd == 'nop':
                potential_bugs.append(idx)
                idx += 1

        if idx == len(lines):
            print(acc)
            break