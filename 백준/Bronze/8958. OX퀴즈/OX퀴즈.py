a = int(input())

for _ in range(a):
    o = list(input())
    s = 0
    t = 0
    for ox in o:
        if ox == 'O':
            s += 1
            t += s
        else:
            s = 0
    print(t)