#10866
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ans = deque()
for _ in range(n):
  a = input().split()
    
  if a[0] == 'push_front':
    ans.appendleft(int(a[1]))
  elif a[0] == 'push_back':
    ans.append(int(a[1]))
  elif a[0] == 'pop_front':
    if len(ans) > 0:
      temp = ans.popleft()
      print(temp)
    else:
      print(-1)
  elif a[0] == 'pop_back':
    if len(ans) > 0:
      temp = ans.pop()
      print(temp)
    else:
      print(-1)
  elif a[0] == 'size':
    print(len(ans))
  elif a[0] == 'empty':
    if len(ans) == 0:
      print(1)
    else:
      print(0)

  elif a[0] == 'front':
    if len(ans) >0:
      print(ans[0])
    else:
      print(-1)
  
  elif a[0] == 'back':
    if len(ans) > 0:
      print(ans[-1])
    else:
      print(-1)
