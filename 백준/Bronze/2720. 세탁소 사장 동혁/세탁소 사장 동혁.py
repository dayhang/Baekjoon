# 2720

t = int(input())
arr = [25, 10, 5, 1]
cnt = [0] * 4

for i in range(t):
    a = int(input())

    for j in range(len(arr)):
        cnt[j] = a // arr[j]
        a = a % arr[j]

    print(' '.join(map(str, cnt)))