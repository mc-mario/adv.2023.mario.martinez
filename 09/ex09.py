with open('data/input', 'r') as f:
    number_lists = list(map(lambda ns: list(map(lambda n: int(n), ns.split(' '))), f.read().splitlines()))


def get_pairs(clist):
    for idx in range(1, len(clist)):
        yield (clist[idx - 1], clist[idx])

# EX01
final_sum = 0
for nl in number_lists:
    print(nl)
    reduced_numbers, current = [], [e for e in nl]
    sum_numbers = [nl[-1]]
    while True:
        lo = []
        for e1,e2 in get_pairs(current):
            lo.append(e2-e1)

        sum_numbers.append(lo[-1])

        if all(map(lambda lo: lo == 0, lo)):
            break

        current = lo

    final_sum += sum(sum_numbers)

#EX02
final_sum = 0
for nl in number_lists:
    print(nl)
    reduced_numbers, current = [], [e for e in nl]
    sum_numbers = [nl[0]]
    while True:
        lo = []
        for e1,e2 in get_pairs(current):
            lo.append(e2-e1)

        sum_numbers.append(lo[0])

        if all(map(lambda lo: lo == 0, lo)):
            break

        current = lo

    c = 0
    for e in sum_numbers[::-1]:
        c = e-c

    final_sum += c



print(final_sum)

