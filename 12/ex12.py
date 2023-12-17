import functools

with open('data/input', 'r') as f:
    nonogram = list(map(lambda line: line.split(' '), f.read().splitlines()))

import re

from itertools import product


def get_record(line):
    records = re.findall('(#+)', line)
    return ','.join(str(len(record)) for record in records)


# Brute Force
def solve():
    # line_combinations_ex_01_bf = 0
    line_combinations_ex_01 = 0
    line_combinations_ex_02 = 0
    for line, record in nonogram:
        line_combinations_ex_01 += find_line_combinations_cache(line, tuple(map(int, record.split(','))))
        # line_combinations_ex_01_bf += find_line_combinations_bf(line, tuple(map(int, record.split(','))))
        line_combinations_ex_02 += find_line_combinations_cache(
            '?'.join(line for _ in range(5)),
            tuple(map(int, record.split(','))) * 5
        )

    print('Sol1:', line_combinations_ex_01)
    # print('Brute force Sol1: ', line_combinations_ex_01_bf)
    print('Sol2:', line_combinations_ex_02)


def find_line_combinations_bf(line, record):
    max_hashtags = sum(record)
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


@functools.cache
def find_line_combinations_cache(line, records):
    while True:
        if not len(records):
            # Records exhausted, if we still have
            # hashtags we did not satisfy
            return int('#' not in line)

        if not line:
            # No line left but records to match
            # We did not satisfy
            return 0

        c, line = line[0], line[1:]

        # Clean dots from beginning of line
        if c == '.':
            line = line
            continue

        if c == '?':
            total = (
                    find_line_combinations_cache('.' + line, records) +
                    find_line_combinations_cache('#' + line, records)
            )
            return total

        # Check next springs
        c_record, records = records[0], records[1:]
        if len(line) < c_record:
            # Not enough line to fill c_record
            # ex: #?## 5
            return 0

        if '.' in line[:c_record - 1]:
            # Enough line but a dot in the way
            # ex: ##.# 4
            return 0

        if len(line) >= c_record and '#' in line[c_record - 1]:
            # Record is followed by another spring
            # therefore this group length is invalid
            # ex: (###)# 3
            return 0

        # We found a match!
        # Skip over the next group since the separator
        # is either a '.' or a ? converted to one
        # ex: c_record 4, record 3
        # line ####.???# 4,3 -> (####) 4 (.) ??? 3
        # line ####????# 4,3 -> (####) 4 (? -> .) ??? 3
        line = line[c_record:]


solve()
