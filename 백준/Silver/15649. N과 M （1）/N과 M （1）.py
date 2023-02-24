# 15649 back tracking

n,m = map(int,input().split())
result = []
visited = [False] * (n+1)

def bt(x):
  if x == m:
    print(' '.join(map(str, result)))
    return
  for i in range(1, n+1):
    if i not in result:
      result.append(i)
      bt(x+1)
      result.pop()

bt(0)
