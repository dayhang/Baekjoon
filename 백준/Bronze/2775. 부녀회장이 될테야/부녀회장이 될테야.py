t = int(input())
for a in range(t):
    k = int(input())
    n = int(input())
    kn = [x for x in range(1, n+1)] #0층호수 
    for b in range(k):
        for i in range(1,n):
            kn[i] += kn[i-1]
    print(kn[-1])