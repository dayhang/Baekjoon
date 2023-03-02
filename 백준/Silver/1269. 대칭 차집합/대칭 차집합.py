# 1269
a, b = map(int,input().split())
# a, b 원소 개수

# a, b 원소 리스트
a_list = set(list(map(int,input().split())))
b_list = set(list(map(int,input().split())))

# 대칭 차집합
k = a_list.symmetric_difference(b_list)

print(len(k))