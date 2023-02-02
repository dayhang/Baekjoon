m = int(input())
n = int(input())
pri_list=[]
for j in range(m,n+1):
  notprime = 0
  if j > 1:
    for i in range(2, j):
      if j % i == 0:
        notprime += 1
        break
    if notprime == 0:
      x = pri_list.append(j)
      
if len(pri_list) > 0:
  print(sum(pri_list))
  print(min(pri_list))
else:
  print(-1)