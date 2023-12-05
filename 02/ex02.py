import re
from dataclasses import dataclass
from typing import List


@dataclass
class Bag:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class GameInstance:
    game_id: int
    bags: List[Bag]


content_re = re.compile(r'(\d+) (red|green|blue)')


def split_input(line: str) -> GameInstance:
    game_id, bag_contents = line.split(':')
    game_id_int = int(game_id.split(' ')[1])
    parsed_content = list(map(lambda bag: content_re.findall(bag),bag_contents.split(';')))
    return GameInstance(
        game_id=game_id_int,
        bags=list(Bag(**{k: int(v) for v, k in c}) for c in parsed_content)
    )


def ex_01_criteria(g: GameInstance, red_criteria, green_criteria, blue_criteria) -> bool:
    for g in g.bags:
        if red_criteria < g.red or green_criteria < g.green or blue_criteria < g.blue:
            return False
    return True


def ex_02_criteria(g: GameInstance) -> int:
    acc_red, acc_green, acc_blue = 0, 0, 0

    for g in g.bags:
        acc_blue = max(g.blue, acc_blue)
        acc_green = max(g.green, acc_green)
        acc_red = max(g.red, acc_red)

    return acc_red * acc_blue * acc_green


if __name__ == '__main__':
    game_id_sum = 0
    power_cubes = 0

    with open('data/input', 'r') as f:
        for line in f.readlines():
            game = split_input(line)

            if ex_01_criteria(game, 12, 13, 14):
                game_id_sum += game.game_id

            power_cubes += ex_02_criteria(game)

    print("Ex01: ", game_id_sum)
    print("Ex02: ", power_cubes)

