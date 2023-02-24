#15651

n, m = map(int,input().split())
result = []

def dfs(x):
  if len(result) == m:
    print(' '.join(map(str,result)))
    return
  
  for i in range(1, n+1):
    result.append(i)
    dfs(i+1)
    result.pop()
      
dfs(0)