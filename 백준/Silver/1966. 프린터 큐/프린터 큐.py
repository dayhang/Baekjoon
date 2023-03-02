#1996

#queue = (a,b,c,d)
# n 은 문서의 개수, m 번째로 인쇄, 아래로 중요도 나열.
from collections import deque
t = int(input())

# 4 2
# 1 2 3 4
# 2 는 3번째문서를 의미하므로, 4 다음 3이니, 2번째.

for i in range(t):
  n, m = map(int, input().split())
  # 문서는 0~n-1 까지
  q = deque(list(map(int,input().split())))
  count = 0

  while q:
    top = max(q) 
    f = q.popleft()
    m -= 1

    if top == f:
      count += 1
      if m < 0:
        print(count)
        break
    else:
      q.append(f)
      if m < 0:
        m = len(q) - 1

  


    
