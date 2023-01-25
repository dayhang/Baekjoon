t = int(input())
for i in range(t):
    n, s = input().split()
    f = ''
    for i in s:
        f += int(n) * i 
    print(f)