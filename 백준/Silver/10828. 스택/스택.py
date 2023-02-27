#10828
import sys
input = sys.stdin.readline
n = int(input())
push = []

for i in range(n):
  a = input().split()

  if a[0] == 'push':
    push.append(a[1])
  
  elif a[0] == 'pop':
    if len(push) == 0:
      print(-1)
    else:
      print(push.pop())
  
  elif a[0] == 'size':
    print(len(push))
  
  elif a[0] == 'empty':
    if len(push)==0:
      print(1)
    else:
      print(0)

  elif a[0] == 'top':
    if len(push)==0:
      print(-1)
    else:
      print(push[-1])
