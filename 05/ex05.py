import math
import re

with open('data/input', 'r') as f:
    lines = re.split(r'\n\n', f.read())


def pair_iteration(elems):
    for i in range(0, len(elems), 2):
        yield elems[i:i + 2]


seed_list = list(map(int, lines[0].split(':')[1].strip().split(' ')))

def seeds_ex02(seed_list):
    for seed_start, seed_range in pair_iteration(seed_list):
        print(seed_start)
        for offset in range(seed_range):
            yield seed_start+offset


clean_maps = lambda line: list(
    map(lambda x: tuple(map(int, x.split(' '))) , # Parse map groups into tuple of ints
        line.split(':')[1].strip('\n').split('\n'))) # Split input into map groups


# number_mapping = lambda line: {source_r + offset: dest_r + offset
#                                for dest_r, source_r, r_length in clean_maps(line)
#                                for offset in range(0, r_length)}
# This approach quickly exploded once I saw the range is over 1M numbers per entry...
# First idea was to have all the dicts number_mappings in a list and apply
# for mapping in number_mappings:
#       data = mapping.get(data, data)



def transform(number, line):
    for dest, source, r_length in clean_maps(line):
        offset = number - source
        if offset >= 0 and offset <= r_length:
            return dest + offset
    return number


def solve(seeds: list):
    lowest_location = math.inf
    for seed in seeds:
        data = seed
        for line in lines[1:]:
            data = transform(data, line)
        lowest_location = min(data, lowest_location)
    print("Solved: ", lowest_location)


solve(seeds_ex02(seed_list))

