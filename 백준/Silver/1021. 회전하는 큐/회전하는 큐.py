# 1021
from collections import deque

n, m = map(int,input().split())
arr = list(map(int,input().split()))

dlist = [i for i in range(1, n+1)]
queue = deque(dlist)
count = 0

for num in arr:
  while True:
    if queue[0] == num:
      queue.popleft()
      break
    else:
      if queue.index(num) < len(queue)/2:
        while queue[0] != num:
          queue.append(queue.popleft())
          count += 1
      else:
        while queue[0] != num:
          queue.appendleft(queue.pop())
          count += 1

print(count)