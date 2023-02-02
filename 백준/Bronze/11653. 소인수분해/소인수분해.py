n = int(input())
p = n
if p > 1:
  for i in range(2,n+1):
    while p % i == 0:
      print(i)
      p = p//i