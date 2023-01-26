a,b = map(str, input().split())
c = str()
d = str()
for i in range(1,4):
    c += a[-i]
    d += b[-i]
print(max(c,d))