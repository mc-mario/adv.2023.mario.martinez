with open('data/input', 'r') as f:
    instructions, _, *nodes = f.read().splitlines()

import re

node_parser = re.compile(r'\w{3}')
nav_map = {}
for node in nodes:
    initial, left, right = node_parser.findall(node)
    nav_map[initial] = (left, right)


def walk():
    current = 'AAA'
    steps = 0
    while True:
        for curr_instr in instructions:
            steps += 1
            idx = 0 if curr_instr == 'L' else 1
            current = nav_map[current][idx]
            if current == 'ZZZ':
                return steps


def walk_02():
    current = [e for e in nav_map.keys() if e.endswith('A')]
    solution = [0] * len(current)
    steps = 0
    while True:
        for curr_instr in instructions:
            steps += 1
            idx = 0 if curr_instr == 'L' else 1
            current = [nav_map[c][idx] for c in current]
            if any(map(lambda e: e.endswith('Z'), current)):
                for idx, e in enumerate(current):
                    if e.endswith('Z') and solution[idx] == 0:
                        solution[idx] = steps
                    print(solution)
                    print(math.lcm(*solution))
            if all(map(lambda e: e != 0, solution)):
                break


import math

print(walk_02())
