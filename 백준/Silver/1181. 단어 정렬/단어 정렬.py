import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    l.append(sys.stdin.readline().strip())
set_l = set(l)
l = list(set_l)
l.sort()
l.sort(key = len)

for i in l:
    print(i)