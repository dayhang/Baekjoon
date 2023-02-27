# 13460
from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
      graph.append(list(input()))
      for j in range(m):
        if graph[i][j] == 'R':
          rx, ry = i, j
        elif graph[i][j] == 'B':
          bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
  queue = deque()
  queue.append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      rx, ry, bx, by = queue.popleft()
      if cnt > 10:
        print(-1)
        return

      if graph[rx][ry] == 'O':
        print(cnt)
        return
      
      for i in range(4):
        temprx = rx
        tempry = ry


        while True:
          temprx += dx[i]
          tempry += dy[i]
          
          if graph[temprx][tempry] == '#':
            temprx -= dx[i]
            tempry -= dy[i]
            break
          
          if graph[temprx][tempry] == 'O':
            break
        
        tempbx = bx
        tempby = by
        while True:
          tempbx += dx[i]
          tempby += dy[i]
          if graph[tempbx][tempby] == '#':
            tempbx -= dx[i]
            tempby -= dy[i]
            break
          if graph[tempbx][tempby] == 'O':
            break
        
        if graph[tempbx][tempby] == 'O':
          continue

        if temprx == tempbx and tempry == tempby:
          if abs(temprx - rx) + abs(tempry - ry) > abs(tempbx - bx) + abs(tempby - by):
            temprx -= dx[i]
            tempry -= dy[i]
          else:
            tempbx -= dx[i]
            tempby -= dy[i]
        
        if (temprx, tempry, tempbx, tempby) not in visited:
          queue.append((temprx, tempry, tempbx, tempby))
          visited.append((temprx, tempry, tempbx, tempby))

    cnt += 1
  print(-1)

bfs(rx, ry, bx, by)
