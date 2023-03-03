# 2522

n = int(input())

for i in range(1, n+1):
  print(' ' * abs(n-i) + '*'*i)
for i in range(n+1, 2*n):
  print(' ' * abs(n-i) + '*'*(2*n-i))