n = int(input())
h = []
for _ in range(n):
    h.append(list(map(int, input().split())))

for i in range(1,len(h)):
    h[i][0] = min(h[i-1][1],h[i-1][2]) + h[i][0]
    h[i][1] = min(h[i-1][0],h[i-1][2]) + h[i][1]
    h[i][2] = min(h[i-1][0],h[i-1][1]) + h[i][2]
    
print(min(h[n-1]))