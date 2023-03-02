# 1874
n = int(input())
check = True
stack = []
ans = []
count = 1

for i in range(n):
  a = int(input())
  while count <= a:
    stack.append(count)
    ans.append('+')
    count += 1

  if stack[-1] == a:
    stack.pop()
    ans.append('-')
  
  else:
    check = False
    break

if check:
  for num in ans:
    print(num)
else:
  print('NO')