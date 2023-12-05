import math

with open('data/input', 'r') as f:
    lines = f.read().splitlines()


def get_score(card: str):
    winning, current = list(map(lambda number_list: number_list.split(' '), card.split(':')[1].split('|')))
    return set(filter(lambda x: x != '', current)).intersection(set(filter(lambda x: x != '', winning)))


# Ex01
points = 0
for card in lines:
    score = get_score(card)
    points += math.floor(2 ** (len(score) - 1))

print("Sol01", points)

# Ex02
cards = {k: 1 for k in range(1, len(lines) + 1)}
for idx, card in enumerate(lines, 1):
    score = get_score(card)
    for e in range(1, len(score) + 1):
        cards[idx + e] += cards[idx]

print("Sol02: ", sum(cards.values()))
