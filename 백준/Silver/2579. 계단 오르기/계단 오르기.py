n = int(input())
s = [0 for i in range(301)]
sc = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
sc[0] = s[0]
sc[1] = s[0] + s[1]
sc[2] = max(s[1]+s[2], s[0]+s[2])
for i in range(3, n):
    # 마지막 전 계단을 밟는 경우, 밟지 않는 경우
    sc[i] = max(sc[i-3]+ s[i-1] + s[i], sc[i-2]+s[i])
print(sc[n-1])