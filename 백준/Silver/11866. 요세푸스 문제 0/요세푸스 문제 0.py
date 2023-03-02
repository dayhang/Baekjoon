# 11866
from collections import deque
n, k = map(int,input().split())
# 1부터 n 까지 원을 그리며 앉아있다
# k번째 사람을 제거한다.

stack = deque([i for i in range(1,n+1)])
print('<', end='')
# 1 2 3 4 5 6 7
# 4 5 6 7 1 2 
while stack:
  for i in range(k-1):
    stack.append(stack[0])
    stack.popleft()
  print(stack.popleft(), end='')
  if stack:
    print(', ',end='')
print('>')

  