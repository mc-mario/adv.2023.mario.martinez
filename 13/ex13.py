with open('data/data', 'r') as f:
    fields = list()
    reflection_idx = list()
    for row in f.read().splitlines():
        if len(row) == 0:
            fields.append(reflection_idx)
            reflection_idx = list()
            continue
        reflection_idx.append(row)
    fields.append(reflection_idx)


def get_pairs(clist):
    for idx in range(1, len(clist)):
        yield (idx - 1, idx)


SMUDGE_LIMIT = 0

def vertical_count(id1, id2, f, _c):
    vc = 0
    for row in f:
        if row[id1 - reflection_idx] == row[id2 + reflection_idx]:
            continue
        vc += 1
    return vc


def horizontal_count(row1, row2):
    hc = 0
    for e1, e2 in zip(row1, row2):
        if e1 == e2:
            continue
        hc += 1
    return hc


count = 0
for idx, f in enumerate(fields):

    # Vertical reflection
    for id1, id2 in get_pairs(f[0]):
        reflection = False
        reflection_idx, smudge_count = 0, 0
        while (id1 - reflection_idx) >= 0 and (id2 + reflection_idx) < len(f[0]):
            smudge_count += vertical_count(id1, id2, f, reflection_idx)
            if smudge_count > SMUDGE_LIMIT:
                reflection = False
                break
            reflection = True
            reflection_idx += 1

        if reflection and smudge_count == SMUDGE_LIMIT:
            print(f'Found mirror in {idx} Vertical', id1 + 1)
            count += (id1 + 1)
            break

    # Horizontal reflection
    for id1, id2 in get_pairs(f):
        reflection = False
        reflection_idx = 0
        smudge_count = 0
        while (id1 - reflection_idx) >= 0 and (id2 + reflection_idx) < len(f):
            smudge_count += horizontal_count(f[id1 - reflection_idx], f[id2 + reflection_idx])
            if smudge_count > SMUDGE_LIMIT:
                reflection = False
                break

            reflection = True
            reflection_idx += 1

        if reflection and smudge_count == SMUDGE_LIMIT:
            print(f'Found mirror in {idx} Horizontal', id1 + 1)
            count += (id1 + 1) * 100

print(count)