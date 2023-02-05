import sys

n = int(int(sys.stdin.readline()))
agelist = []
for i in range(n):
  x, y = map(str, input().split())
  agelist.append([int(x),i,y])

agelist.sort()

for i in range(n):
  print(agelist[i][0],agelist[i][2])