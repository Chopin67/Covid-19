def agreement(i1, i2):
    if i1 == i2:
        empty = i1
    empty = []
    for i in i1:
        if i in i2:
            empty.append(i)
    return empty
#print(agreement(['games', 'museums', 'food'], []))


def disagreement(i1, i2):
    empty = []
    if len(i1) >= len(i2):
        for l in i1:
            if l not in i2:
                empty.append(l)
        for j in i2:
            if j not in i1:
                empty.append(j)
    elif len(i1) < len(i2):
        for m in i2:
            if m not in i1:
                empty.append(m)
        for e in i1:
            if e not in i2:
                empty.append(e)

    return empty

def compatibility(i1, i2):
    shared = len(agreement(i1, i2))
    notshared = len(disagreement(i1, i2))
    score = (shared)/(shared + notshared)
    return score


def bestmatch(me, others):
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility(me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom

