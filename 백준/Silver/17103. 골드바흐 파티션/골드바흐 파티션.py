# goldbach partition
import sys

sosu = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        sosu.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 0
    n = int(sys.stdin.readline())
    for i in sosu:
        if i >= n:
            break
        if not check[n - i] and i <= n-i:  # 순서만 다른거 counting 하지 않기 위해
            cnt += 1
    print(cnt)
