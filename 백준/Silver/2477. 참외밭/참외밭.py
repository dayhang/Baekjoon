# 2477

k = int(input())
arr = [list(map(int,input().split())) for _ in range(6)]

w = 0
wid = 0
h = 0
hid = 0

for i in range(len(arr)):
  if arr[i][0] == 1 or arr[i][0] == 2:
    if w < arr[i][1]:
      w = arr[i][1]
      wid = i
  elif arr[i][0] == 3 or arr[i][0] == 4:
    if h < arr[i][1]:
      h = arr[i][1]
      hid = i

sw = abs(arr[(wid - 1)%6][1] - arr[(wid+1)%6][1])
sh = abs(arr[(hid - 1)%6][1] - arr[(hid+1)%6][1])

total = ((w*h)-(sw*sh))*k
print(total)