#implementation 1

# 33 + 3 + 3 = 39
def f(n):
  num = n + sum(map(int, str(n)))
  return num

x = set()

for i in range(0, 10000):
  x.add(f(i))

for i in range(0, 10000):
  if i not in x:
    print(i)
