n,m = map(int,input().split())
result = []

def dfs(x):
  if len(result) == m:
    print(' '.join(map(str,result)))
    return
  
  for i in range(x, n+1):
    if i not in result:
      result.append(i)
      dfs(i+1)
      result.pop()

dfs(1)