import itertools
import more_itertools as mi

def is_valid(to_valid, numbers):
    for i in itertools.combinations(numbers, 2):
        if sum(i) == to_valid:
            return True
    return False

def find_target_sum(target, liste):
    for i in range(2, len(liste)):
        for window in mi.windowed(liste, i):
            if sum(window) == target:
                return window
    return

with open("input", 'r') as inp:
    complete_list = list(int(line) for line in inp)
    for *window, to_valid in mi.windowed(complete_list, 26):
        if not is_valid(to_valid, window):
            break
    print(to_valid)

    result = find_target_sum(to_valid, complete_list)
    if result:
        print(result)