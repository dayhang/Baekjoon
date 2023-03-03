# 2455
count = 0
top = 0
for i in range(4):
  a, b = map(int,input().split())
  count += b - a

  if count>= top:
    top = count

print(top)
