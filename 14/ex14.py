import functools
import math

with open('data/data', 'r') as f:
    matrix = list(map(list, f.read().splitlines()))

import numpy as np


def _move_up(elem, matrix):
    c_idy, c_idx = elem
    while c_idy > 0:
        if matrix[c_idy - 1][c_idx] != '.':
            break
        matrix[c_idy - 1][c_idx], matrix[c_idy][c_idx] = matrix[c_idy][c_idx], matrix[c_idy - 1][c_idx]
        c_idy -= 1


@functools.cache
def move_and_rot(matrix):
    matrix = [list(row) for row in matrix]
    for idy in range(len(matrix)):
        for idx in range(len(matrix[0])):
            if idy == 0:
                continue

            if matrix[idy][idx] == 'O':
                _move_up((idy, idx), matrix)
    return tuple(tuple(row) for row in np.rot90(matrix, axes=(1, 0)))


CYCLES = 1000000000


def tilt(matrix):
    cycle = 1
    cycle_detection = dict()

    matrix = tuple(tuple(row) for row in matrix)
    while cycle < CYCLES:
        for _c in range(4):
            matrix = move_and_rot(matrix)

        cycle_found = cycle_detection.get(matrix, False)
        if cycle_found:
            diff = cycle - cycle_found
            factor = (CYCLES - cycle) // math.floor(diff)
            cycle += (factor * diff)

        cycle_detection[matrix] = cycle
        cycle += 1

    for _c in range(4):
        matrix = move_and_rot(matrix)

    print(sum_load(matrix))


def sum_load(matrix):
    load_sum = 0
    for idy in range(len(matrix)):
        rocks = len(list(filter(lambda x: x == 'O', matrix[idy])))
        load_multiplication = len(matrix) - idy
        load_sum += rocks * load_multiplication
    return load_sum


tilt(matrix)
