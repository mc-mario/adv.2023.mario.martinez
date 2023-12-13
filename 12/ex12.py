import functools

with open('data/test', 'r') as f:
    nonogram = list(map(lambda line: line.split(' '), f.read().splitlines()))

import re

from itertools import product

def get_record(line):
    records = re.findall('(#+)', line)
    return ','.join(str(len(record)) for record in records)

# Brute Force
def solve():
    line_combinations_ex_01 = 0
    line_combinations_ex_02 = 0
    for line, record in nonogram:
        line_combinations_ex_01 += find_line_combinations_cache(line, 0, list(map(int, record.split(','))))
        #line_combinations_ex_02 += find_line_combinations_cache(
        #    '?'.join(line for _ in range(5)),
        #    list(map(int, record.split(','))) * 5
        #)

    print('Sol1:', line_combinations_ex_01)
    print('Sol2:', line_combinations_ex_02)

@functools.cache
def find_line_combinations_bf(line, record):
    max_hashtags = sum(map(int, record.split(',')))
    curr_hashtags = line.count('#')
    _line_combos = 0
    for combination in product('#.', repeat=len(re.findall('\?', line))):
        aux_line = line
        if len(list(filter(lambda x: x == '#', combination))) + curr_hashtags > max_hashtags:
            continue

        for replacement in combination:
            aux_line = aux_line.replace('?', replacement, 1)

        if get_record(aux_line) == record:
            _line_combos += 1

    return _line_combos


def find_line_combinations_cache(line, cindex, records):
    if len(records) == 0:
        print('idk')
        return 1


    if len(re.findall('\?', line))  == 0:
        groups = re.findall('#+', line)
        if len(groups) > len(records):
            return 0

        if len(groups) == len(records):
            for e1, e2 in zip(groups, records):
                if len(e1) != e2:
                    return 0

    current = line[0]

    count = 0

    # Nothing to do here
    if current == '.':
        find_line_combinations_cache(line[1:],  records[1:])
    else:
        count += find_line_combinations_cache('#'+line[1:], records)
        count += find_line_combinations_cache('.' + line[1:], records)

    return count


solve()