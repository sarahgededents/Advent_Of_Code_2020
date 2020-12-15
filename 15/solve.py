import itertools
import more_itertools as mi

START_NB = [1, 0, 18, 10, 19, 6]

def solve(starting_numbers):
    for n in starting_numbers:
        yield n
    history = {v: i for i, v in enumerate(starting_numbers[:-1])}
    last_spoken = starting_numbers[-1]
    for current_turn in itertools.count(len(starting_numbers)):
        previous_turn = current_turn - 1
        next_spoken = previous_turn - history[last_spoken] if last_spoken in history else 0
        history[last_spoken] = previous_turn
        yield next_spoken
        last_spoken = next_spoken

for turn in [2020, 30000000]:
    print(mi.nth(solve(START_NB), turn - 1))