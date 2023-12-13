with open('data/data', 'r') as f:
    fields = list()
    c = list()
    for row in f.read().splitlines():
        if len(row) == 0:
            fields.append(c)
            c = list()
            continue
        c.append(row)
    fields.append(c)

f = fields[0]

def get_pairs(clist):
    for idx in range(1, len(clist)):
        yield (idx-1, idx)



count = 0
for idx, f in enumerate(fields):

    eq = None
    # Vertical reflection
    for id1, id2 in get_pairs(f[0]):
        c = 0
        while (id1 - c) >= 0 and (id2 + c) < len(f[0]):
            for row in f:
                if row[id1 - c] == row[id2 + c]:
                    #print(row[id1 - c], row[id2 + c], 'eq')
                    eq = (id1, id2)
                    continue
                #print(row[id1 - c], row[id2 + c])
                #print()
                eq = None
                break
            if eq is None:
                break
            c+= 1


        if eq:
            print(f'Found mirror in {idx} Vertical', id1 + 1)
            count += (id1 + 1)
            break


    eq = None
    # Horizontal reflection
    for id1, id2 in get_pairs(f):
        eq = None
        c = 0
        while (id1 - c) >= 0 and (id2 + c) < len(f):
            if f[id1 - c] == f[id2 + c]:
                eq = (id1, id2)
                c += 1
                continue

            eq = None
            break

        if eq:
            print(f'Found mirror in {idx} Horizontal', id1+1)
            count += (id1 + 1) * 100

print(count)