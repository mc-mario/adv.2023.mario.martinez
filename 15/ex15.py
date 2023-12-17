with open('data/data', 'r') as f:
    sequences = f.read().splitlines()[0].split(',')

def holiday_ascii_string_helper(sequence):
    hash = 0
    for c in sequence:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

acc = 0
for s in sequences:
    acc += holiday_ascii_string_helper(s)

print(acc)

hash_map = [[] for _ in range(256)]

# Bold asumption Mario, boild asumption...
LABEL_LENGTH = 2
def holiday_ascii_string_helper_manual_arrangement_procedure(label):
    if '-' in label:
        l_text = label.split('-')[0]
        pop_out = None
        for idx, e in enumerate(hash_map[holiday_ascii_string_helper(l_text)]):
            if e.split('=')[0] == l_text:
                pop_out = idx
                break

        if pop_out is not None:
            hash_map[holiday_ascii_string_helper(l_text)].pop(pop_out)
        return

    l_text = label.split('=')[0]
    replace = None
    for idx, e in enumerate(hash_map[holiday_ascii_string_helper(l_text)]):
        if e.split('=')[0] == l_text:
            replace = idx
            break

    if replace is not None:
        hash_map[holiday_ascii_string_helper(l_text)][replace] = label
        return

    hash_map[holiday_ascii_string_helper(l_text)].append(label)


for s in sequences:
    holiday_ascii_string_helper_manual_arrangement_procedure(s)

ex02_acc = 0
for idx, box in enumerate(hash_map, 1):
    for idy, lens in enumerate(box, 1):
        ex02_acc += (idx * idy * int(lens[-1]))

print(ex02_acc)


