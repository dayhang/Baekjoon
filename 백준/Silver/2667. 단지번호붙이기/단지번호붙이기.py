#2667
from collections import deque
n = int(input())
graph = []
# 그래프 작성
for _ in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 방식
def bfs(graph,x,y):
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  count = 1

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 그래프에서 이탈할 경우
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      # 1을 만날경우
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx,ny))
        count += 1
  return count

cnt = []
for i in range(n):
  for j in range(n):
    if graph[i][j] ==1:
      val = bfs(graph, i, j)
      cnt.append(val)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
  print(cnt[i])
