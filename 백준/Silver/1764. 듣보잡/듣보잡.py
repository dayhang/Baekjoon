#1764

n, m = map(int, input().split())

a = set()
for i in range(n):
  name = input()
  a.add(name)

b = set()
for i in range(m):
  name = input()
  b.add(name)

answer = sorted(list(a&b))
print(len(answer))

for name in answer:
  print(name)