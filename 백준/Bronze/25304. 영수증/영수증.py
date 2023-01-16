X = int(input())
N = int(input())
s = 0

for _ in range(N):
    A, B = map(int, input().split())
    s = s + A*B
    
if s == X:
    print("Yes")
else:
    print("No")