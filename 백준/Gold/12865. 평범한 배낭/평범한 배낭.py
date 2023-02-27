# 12865

n, k = map(int,input().split())

a = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
  a.append(list(map(int,input().split())))

for i in range(1, n+1):
  for j in range(1, k+1):
    w, v = a[i][0], a[i][1]
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k]) 