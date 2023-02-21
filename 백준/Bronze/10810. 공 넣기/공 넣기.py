n, m = map(int, input().split())

arr = [0 for _ in range(n)]

for _ in range(m):
  i, j, k = map(int,input().split())
  # 3 3 0 0 0
  for num in range(i-1, j):
    arr[num] = k

print(*arr)
