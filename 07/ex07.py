import math
from functools import cmp_to_key

CARD_RANKS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_RANKS_EX02 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

from collections import defaultdict

get_counter = lambda: defaultdict(int)

def count_cards(cards):
    counter = get_counter()
    for c in cards:
        counter[c] += 1
    return counter


five_of_a_kind = "AAAAA"

counter = get_counter()
for c in five_of_a_kind:
    counter[c] += 1

card_checks = [
    ("is_five_of_a_kind", lambda c: len(c.values()) == 1 and max(c.values()) == 5),
    ("is_four_of_a_kind", lambda c: len(c.values()) == 2 and max(c.values()) == 4),
    ("if_full_house", lambda c: len(c.values()) == 2 and max(c.values()) == 3 and min(c.values()) == 2),
    ("is_three_of_a_kind", lambda c: len(c.values()) == 3 and max(c.values()) == 3),
    ("is_two_pair", lambda c: len(c.values()) == 3 and max(c.values()) == 2),
    ("is_one_pair", lambda c: len(c.values()) == 4 and max(c.values()) == 2),
    ("is_high_card", lambda c: len(c.values()) == 5),
]

def get_card_type(hand):
    for idx, (ctype, check) in enumerate(card_checks):
        if check(count_cards(hand)):
            return ctype, idx

def transform_joker_hand(hand: str):
    highest_hand = math.inf

    if 'J' not in hand:
        return get_card_type(hand)[0]

    for card_rank in CARD_RANKS_EX02[:-1]:
        temp_hand = hand.replace('J', card_rank)
        _, idx = get_card_type(temp_hand)
        highest_hand = min(highest_hand, idx)

    return card_checks[highest_hand][0]

def stronger_high_card(current, other):
    current, other = current[0], other[0]
    for c, o in zip(current, other):
        if CARD_RANKS_EX02.index(c) == CARD_RANKS_EX02.index(o):
            continue
        return 1 if CARD_RANKS_EX02.index(c) < CARD_RANKS_EX02.index(o) else -1
    return 0

with open('data/data', 'r') as f:
    cards = list(map(lambda c: c.split(' '), f.read().splitlines()))

priority_queue = defaultdict(list)

# EX01
#for card, rank in cards:
#     current_card_type = None
#
#     for ctype, check in card_checks:
#         if check(count_cards(card)):
#             current_card_type = ctype
#             break
#
#     priority_queue[current_card_type].append((card, rank))

for hand, rank in cards:
    current_card_type = transform_joker_hand(hand)
    priority_queue[current_card_type].append((hand, rank))



print(priority_queue)
for e in priority_queue.values():
    e.sort(key=cmp_to_key(stronger_high_card))

rank_result = 0
curr_rank = 0
for name, _ in card_checks[::-1]:
    for _, value in priority_queue[name]:
        curr_rank += 1
        rank_result += int(value) * curr_rank

print(rank_result)

