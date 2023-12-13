with open('data/test', 'r') as f:
    galaxy = list(map(lambda line: list(line), f.read().splitlines()))

expand_rows = []
for idx, row in enumerate(galaxy):
    if '#' not in set(row):
        expand_rows.append(idx)
    continue

expand_cols = []
for idy in range(len(galaxy[0])):
    if '#' not in set(e[idy] for e in galaxy):
        expand_cols.append(idy)
    continue

EXP_CTE = 9

empty_row = [['.'] * len(galaxy[0])]*EXP_CTE
for c, ex_row in enumerate(expand_rows):
    galaxy = galaxy[:ex_row+(c*EXP_CTE)] + empty_row + galaxy[ex_row+(c*EXP_CTE):]

for idx in range(len(galaxy)):
    for c, idy in enumerate(expand_cols):
        galaxy[idx] = galaxy[idx][:idy+(c*EXP_CTE)] + ['.']*EXP_CTE + galaxy[idx][idy+(c*EXP_CTE):]

galaxy_positions = []
for idx, row in enumerate(galaxy):
    for idy, elem in enumerate(row):
        if elem != '#':
            continue
        galaxy_positions.append((idx, idy))
        c += 1

def manhattan_distance(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    c1, c2 = 0, 0

    return abs(x1 - x2 - c1) + abs(y1 - y2 - c2)

from itertools import combinations

manhattan_sum = 0
for p1, p2 in combinations(galaxy_positions, 2):
    print(p1, p2, manhattan_distance(p1, p2))
    manhattan_sum += manhattan_distance(p1, p2)

print(manhattan_sum)