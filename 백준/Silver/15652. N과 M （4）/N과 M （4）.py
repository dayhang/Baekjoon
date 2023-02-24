# 15652
n, m = map(int,input().split())
result = []

def dfs(x):
  # 탈출 조건
  if len(result) == m:
    print(' '.join(map(str,result)))
    return
  
  for i in range(x, n+1):
      result.append(i)
      dfs(i)
      result.pop()

dfs(1)
