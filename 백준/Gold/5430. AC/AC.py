# 5430
from collections import deque

n = int(input())

for i in range(n):
  a = input().strip()
  m = int(input())
  
  check = 1
  arr = input()[1:-1].split(',')
  queue = deque(arr)
  if m == 0:
    queue = deque()

  R = 0
  for i in range(len(a)):
    if a[i] == 'R':
      R += 1
    if a[i] == 'D':
      if len(queue) == 0:
        print('error')
        check = 0
        break
      else:
        if R%2 ==0:
          queue.popleft()
        else:
          queue.pop()

  if check ==0:
    continue

  else:
    if R % 2 == 0:
      print('[' + ",".join(queue) + ']')
    else:
      queue.reverse()
      print('[' + ",".join(queue) + ']')



