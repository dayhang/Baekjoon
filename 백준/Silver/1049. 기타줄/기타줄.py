a, b = map(int, input().split())

answer = 0
price_list = []

for _ in range(b):
    price = tuple(map(int, input().split()))
    price_list.append(price)

six_list = sorted(price_list, key=lambda x : x[0])
one_list = sorted(price_list, key=lambda x : x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer = six_list[0][0] * (a // 6) + one_list[0][1] * (a % 6)
    if six_list[0][0] < one_list[0][1] * (a % 6):
        answer = six_list[0][0] * (a//6 + 1)
else:
    answer = one_list[0][1] * a

print(answer)