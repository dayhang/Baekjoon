# 2630
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

countzero = 0
countone = 0
def fn(x, y, n):
  global countzero, countone
  col = graph[x][y]

  for i in range(x, x+n):
    for j in range(y, y+n):
      if col != graph[i][j]:
        fn(x, y, n//2)
        fn(x,y+n//2, n//2)
        fn(x+n//2, y, n//2)
        fn(x+n//2, y+n//2, n//2)
        return
  if col == 0:
    countzero += 1
  else:
    countone += 1

fn(0,0,n)
print(countzero)
print(countone)
