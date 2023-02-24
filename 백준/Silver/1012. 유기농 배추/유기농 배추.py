#1012
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
  # 이동 불가지점
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

t = int(input())

for i in range(t):
  m, n, k = map(int,input().split())
  graph = [[0]*m for _ in range(n)]
  
  for _ in range(k):
    x, y = map(int,input().split())
    graph[y][x] = 1

  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        result += 1

  print(result)

