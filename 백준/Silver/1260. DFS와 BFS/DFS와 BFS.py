from collections import deque

n, m, v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_d = [0] * (n+1)
visited_b = [0] * (n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited_d[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited_d[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_b[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited_b[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited_b[i] = 1
                
dfs(v)
print()
bfs(v)
        
        