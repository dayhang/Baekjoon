n = str(input())
k = int(n)
ssz = 0
for i in range(1, k+1):
  arr = list(map(int, str(i)))
  ssz = i + sum(arr)
  if ssz == k:
    print(i)
    break
  if i == k:
    print(0)
    break