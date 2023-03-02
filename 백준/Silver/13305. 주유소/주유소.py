# 13305

n = int(input())

# 최소비용 -> 제일 싼 도시까지 가는 비용
d = list(map(int, input().split()))
m = list(map(int, input().split()))

# 가장 저렴한 주유소 찾기 마지막 주유소 제외
min_index = m.index(min(m[:-1]))

total = 0
# 가장 저렴한 주유소 까지 가기
for i in range(min_index):
  pay = d[i] * m[i]
  total += pay

# 가장 저렴한 주유소 에서 끝까지 가기
for i in range(min_index, len(d)):
  pay = m[min_index]*d[i]
  total += pay

print(total)