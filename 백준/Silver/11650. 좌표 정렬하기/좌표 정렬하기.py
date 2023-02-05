import sys
input = sys.stdin.readline
n = int(input())
list = []
for i in range(n):
  [x, y] = map(int, input().split())
  list.append([x, y])

sort_list = sorted(list)

for i in range(n):
  print(sort_list[i][0], sort_list[i][1])