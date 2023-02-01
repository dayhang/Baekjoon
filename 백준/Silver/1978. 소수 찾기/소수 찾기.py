n = int(input())
number = map(int, input().split())
prime = 0
for i in number:
    noprime = 0
    if i > 1:
        for j in range(2, i):
            if i%j ==0:
                noprime+=1
        if noprime==0:
            prime+=1
print(prime)