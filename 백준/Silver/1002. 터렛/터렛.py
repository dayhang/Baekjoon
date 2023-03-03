# 1002
import math
t = int(input())

for i in range(t):
  arr = list(map(int,input().split()))
  d = math.sqrt((arr[0]-arr[3])**2 + (arr[1]-arr[4])**2)
  if d == 0 and arr[2] == arr[5]:
    print(-1)
  elif abs(arr[2] - arr[5]) == d or arr[2] + arr[5] == d:
    print(1)
  elif abs(arr[2] - arr[5]) < d < arr[2] + arr[5]:
    print(2)
  else:
    print(0)
