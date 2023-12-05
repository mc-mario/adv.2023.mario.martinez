import re

is_symbol = re.compile('[^a-zA-Z0-9.]')
is_gear = re.compile('\*')


def get_symbols_positions(line, regex) -> list[int]:
    return [match.start() for match in regex.finditer(line)]


def get_adjacents(x, y, matrix) -> list[tuple[int]]:
    adjacents = list()
    adjacent = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                (x + 1, y + 1)]

    for adjacency in adjacent:
        adjacent_x, adjacent_y = adjacency

        if adjacent_x < 0 or adjacent_x >= len(matrix[0]):
            continue

        if adjacent_y < 0 or adjacent_y >= len(matrix):
            continue

        adjacents.append(adjacency)

    return adjacents


numbers = set(e for e in range(10))


def find_number(x, y, matrix) -> (int, range):
    i, j = 0, 0

    if matrix[y][x] not in numbers:
        return 0, range(0)

    # right
    while True:
        if x + i + 1 >= len(matrix[0]):
            break
        if not matrix[y][x + i + 1] in numbers:
            break
        i += 1

    # left
    while True:
        if x + j - 1 < 0:
            break
        if not matrix[y][x + j - 1] in numbers:
            break
        j -= 1

    return int(''.join(matrix[y][x + j: x + i + 1])), range(x + j, x + i + 1)


def ex_01(lines: list):
    numbers = 0
    found_numbers = dict()
    for idy, line in enumerate(lines):
        character_pos = get_symbols_positions(line, is_symbol)

        for idx in character_pos:
            for x, y in get_adjacents(idx, idy, lines):
                number, _range = find_number(x, y, lines)

                add = True

                for _idx in _range:
                    if found_numbers.get((y, _idx), False):
                        add = False
                        break
                    found_numbers[(y, _idx)] = number

                if add:
                    numbers += number
    return numbers


def ex_02(lines: list):
    numbers = 0
    found_numbers = dict()
    for idy, line in enumerate(lines):
        character_pos = get_symbols_positions(line, is_gear)

        for idx in character_pos:
            gear_numbers = list()
            for x, y in get_adjacents(idx, idy, lines):
                number, _range = find_number(x, y, lines)
                add = True
                for _idx in _range:
                    if found_numbers.get((y, _idx), False):
                        add = False
                        break
                    found_numbers[(y, _idx)] = number

                if add and number != 0:
                    gear_numbers.append(number)

            if len(gear_numbers) == 2:
                numbers = numbers + gear_numbers[0] * gear_numbers[1]

    return numbers


if __name__ == '__main__':
    with open('data/test', 'r') as f:
        lines = f.read().splitlines()
        print("Sol 1:", ex_01(lines))

    with open('data/test', 'r') as f:
        lines = f.read().splitlines()
        print("Sol 2:", ex_02(lines))
