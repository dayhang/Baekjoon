n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
    
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif i == j:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else:
            tri[i][j] = max(tri[i-1][j-1],tri[i-1][j]) + tri[i][j]

print(max(tri[n-1]))