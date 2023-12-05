import math
import re

with open('data/input', 'r') as f:
    lines = re.split(r'\n\n', f.read())


def pair_iteration(elems):
    for i in range(0, len(elems), 2):
        yield elems[i:i + 2]


seed_list = list(map(int, lines[0].split(':')[1].strip().split(' ')))


def seeds_ex02(seed_list):
    return [(seed_start, seed_range) for seed_start, seed_range in pair_iteration(seed_list)]


clean_maps = (
    lambda line: sorted(
        list(map(lambda x: tuple(map(int, x.split(' '))),  # Parse map groups into tuple of ints
                 line.split(':')[1].strip('\n').split('\n'))),  # Split input into map groups
        key=lambda m: m[1])
)

maps = [clean_maps(line) for line in lines[1:]]


# number_mapping = lambda line: {source_r + offset: dest_r + offset
#                                for dest_r, source_r, r_length in clean_maps(line)
#                                for offset in range(0, r_length)}
# This approach quickly exploded once I saw the range is over 1M numbers per entry...
# First idea was to have all the dicts number_mappings in a list and apply
# for mapping in number_mappings:
#       data = mapping.get(data, data)


def transform(number, map):
    for dest, source, r_length in map:
        offset = number - source
        if offset >= 0 and offset <= r_length:
            return dest + offset
    return number


def transform_2(range_list: list[tuple], maps) -> list[tuple]:
    output = list()
    frontier = range_list

    while len(frontier) > 0:
        curr = frontier.pop()
        intersect_found = False

        for r_dest, r_source, r_length in maps:
            curr_min, curr_offset = curr
            curr_max = curr_min + curr_offset

            # Intersection calcs
            inter_start = max(curr_min, r_source)
            inter_end = min(curr_max, r_source + r_length)
            inter_len = max(inter_end - inter_start, 0)

            if inter_len == 0:
                # No intersection found
                continue

            # Add the intersection with offset (r_dest-r_source)
            intersect_found = True
            output.append(((r_dest - r_source) + inter_start, inter_len))

            # Thankfully the mapping range contains the current range
            if curr_offset == inter_len:
                break

            # Leftover range on the left
            if inter_start > curr_min:
                frontier.append((curr_min, inter_start - curr_min))

            # Left over range on the right
            else:
                frontier.append((inter_end, curr_max - inter_end))
            break

        # After applying all maps if no range is found do 1-1 mapping
        if not intersect_found:
            output.append(curr)

    return output


def solve_ex01(seeds: list):
    lowest_location = math.inf
    for seed in seeds:
        data = seed
        for map in maps:
            data = transform(data, map)
        lowest_location = min(data, lowest_location)
    print("Solved: ", lowest_location)


def solve_ex02(seeds: list):
    lowest_location = math.inf
    for seed in seeds:
        print('Run with seed', seed)
        data = [seed]
        for map in maps:
            data = transform_2(data, map)
        lowest_location = min(sorted(data, key=lambda x: x[0])[0][0], lowest_location)

    print("Solved: ", lowest_location)


solve_ex01(seed_list)
solve_ex02(seeds_ex02(seed_list))
