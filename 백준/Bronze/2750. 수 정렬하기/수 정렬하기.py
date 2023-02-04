n = int(input())
s = []
for _ in range(n):
  s.append(int(input()))
  s.sort()
for i in range(n):
  print(s[i])