from collections import deque
n = int(input())
card = [i for i in range(1,n+1)]
q = deque()
for num in card:
  q.append(num)

while q:
  if len(q) == 1:
    break
  q .popleft()
  temp = q.popleft()
  q.append(temp)

ans = q[0]
print(ans)