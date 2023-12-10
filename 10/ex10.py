from collections import defaultdict

with open('data/test3', 'r') as f:
    matrix = list(map(lambda line: list(line), f.read().splitlines()))


mapping = defaultdict(lambda: lambda y, x: ())
mapping['|'] = lambda y, x: ((y - 1, x), (y + 1, x))
mapping['-'] = lambda y, x: ((y, x - 1), (y, x + 1))
mapping['L'] = lambda y, x: ((y - 1, x), (y, x + 1))
mapping['J'] = lambda y, x: ((y - 1, x), (y, x - 1))
mapping['7'] = lambda y, x: ((y + 1, x), (y, x - 1))
mapping['F'] = lambda y, x: ((y + 1, x), (y, x + 1))
mapping['S'] = lambda y, x: ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1))
STARTING_POINT = 'S'


def get_starting_point(matrix) -> tuple:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'S':
                return row, col


def walk():
    start_y, start_x = get_starting_point(matrix)
    pipes_to_visit = mapping['S'](start_y, start_x)
    frontier = list()
    for pipe_y, pipe_x in pipes_to_visit:
        elem = matrix[pipe_y][pipe_x]
        for is_starting_y, is_starting_x in mapping[elem](pipe_y, pipe_x):
            if is_starting_y == start_y and is_starting_x == start_x:
                frontier.append((pipe_y, pipe_x))
                break

    walk_1, walk_2 = frontier
    visited = list()
    visited.append((start_y, start_x))
    count = 0
    while True:
        count += 1

        if walk_1 == walk_2:
            visited.append(walk_1)
            print('End')
            break

        # Had to adapt the exercise to use an array instead of a set (easier to maintain and pseudo O(1) time to search)
        visited = visited[:] + [walk_1]
        visited = [walk_2] + visited[:]

        w_1_1, w_1_2 = mapping[matrix[walk_1[0]][walk_1[1]]](walk_1[0], walk_1[1])
        w_2_1, w_2_2 = mapping[matrix[walk_2[0]][walk_2[1]]](walk_2[0], walk_2[1])

        walk_1 = w_1_1 if w_1_2 in visited else w_1_2
        walk_2 = w_2_1 if w_2_2 in visited else w_2_2

    print('Ex 01: ', count)
    return visited


visited = walk()

# I gave up on raycast algorithm and just used Shapely
# raycast attempt below
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

polygon = Polygon(visited)
points_contained = 0
for idy in range(len(matrix)):
    for idx in range(len(matrix[0])):
        if polygon.contains(Point(idy, idx)):
            points_contained += 1
            matrix[idy][idx] = 'I'

print(points_contained)

# Failed attempt at using raycast to see how many intersections we find
# def paint(main_pipe):
#     inside_count = 0
#     for idy in range(len(matrix)):
#         for idx in range(len(matrix[0])):
#
#             # Main Loop does not have to be checked
#             if (idy, idx) in main_pipe:
#                 continue
#
#
#             visited = [0, 0, 0, 0]
#             for c_idx in range(idx, len(matrix[0])):
#                 if (idy, c_idx) in main_pipe and matrix[idy][c_idx] in ('|','S','L','F','7','J'):
#                     visited[0] += 1
#
#             # Izq
#             for c_idx in range(0, idx):
#                 if (idy, c_idx) in main_pipe and matrix[idy][c_idx] in ('|','S','L','F','7','J'):
#                     visited[1] += 1
#
#             # Abajo
#             for c_idy in range(idy, len(matrix)):
#                 if (c_idy, idx) in main_pipe and matrix[c_idy][idx] in ('-','S','L','F','7','J'):
#                     visited[2] += 1
#
#             for c_idy in range(0, idy):
#                 if (c_idy, idx) in main_pipe and matrix[c_idy][idx] in ('-','S', 'L','F','7','J'):
#                     visited[3] += 1
#
#             inside = any([e % 2 == 1 for e in visited])
#
#             if inside:
#                 inside_count += 1
#                 matrix[idy][idx] = 'I'
#             else:
#                 matrix[idy][idx] = 'O'
#
#     print(inside_count)

# Pretty Printing the exercise
replace_elem = {
    '|': '│',
    '-': '─',
    'L': '└',
    'J': '┘',
    '7': '┐',
    'F': '┌',
    'I': '▓',
    'O': '░',
}

for row in matrix:
    for elem in row:
        print(replace_elem.get(elem, elem), end='')
    print()
