# 10812

n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m):
  i, j, k = map(int,input().split())
  # 새로운 바구니 순서
  basket[i-1:j] = basket[k-1:j] + basket[i-1:k-1]
  # i바구니 부터 j 바구니까지 = k바구니 부터 j-1바구니까지 + i바구니부터 k-1 바구니까지
print(*basket)
