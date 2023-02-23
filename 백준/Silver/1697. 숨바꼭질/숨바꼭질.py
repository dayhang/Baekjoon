import sys
from collections import deque
input = sys.stdin.readline
def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= m and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
m = 100000
n, k = map(int, input().split())
visited = [0 for i in range(m+1)]
print(bfs(n))