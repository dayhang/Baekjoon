# 4153

while True:
  a = list(map(int,input().split()))
  if sum(a) == 0:
    break
  maxn = max(a)
  a.remove(maxn)

  if a[0]**2 + a[1]**2 == maxn**2:
    print('right')
  else:
    print('wrong')
