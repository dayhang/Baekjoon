n = set(range(1,10000))
a = set()
for num in n:
    for i in str(num):
        num += int(i)
    a.add(num)

b = n - a
for k in sorted(b):
    print(k)