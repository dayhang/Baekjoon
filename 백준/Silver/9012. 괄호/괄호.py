t = int(input())

for _ in range(t):
  stack = []
  a = input()
  check = True

  for val in a:
    if val == '(':
      stack.append('(')
    if val == ')':
      if stack:
        stack.pop()
      elif not stack:
        check = False
        break
  if not stack and check:
    print('YES')
  else:
    print('NO')
