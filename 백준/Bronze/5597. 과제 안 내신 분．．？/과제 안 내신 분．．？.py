c = list(range(1,31))

for _ in range(28):
    a = int(input())
    c.remove(a)

print(min(c))
print(max(c))