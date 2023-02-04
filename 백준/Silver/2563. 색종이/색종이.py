plain = [[False]*100 for i in range(100)]

papercount = int(input())
for _ in range(papercount):
  x, y = map(int, input().split())

  for i in range(x, x+10):
    for j in range(y, y+10):
      plain[i][j] = True

area = 0
for k in range(100):
  area += plain[k].count(True)

print(area)