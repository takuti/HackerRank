def add(s, W):
    for c in W:
        s.append(c)
    return s

def remove(s, k):
    return s[:-k]

s = []
undos = []

Q = int(raw_input())
for _ in range(Q):
    ops = raw_input().split(' ')
    if ops[0] == '1':
        s = add(s, ops[1])
        undos.append(['2', len(ops[1])])
    elif ops[0] == '2':
        k = int(ops[1])
        undos.append(['1', s[-k:]])
        s = remove(s, k)
    elif ops[0] == '3':
        k = int(ops[1])
        print(s[k - 1])
    else:  # undo
        op, val = undos.pop(-1)
        func = add if op == '1' else remove
        s = func(s, val)
