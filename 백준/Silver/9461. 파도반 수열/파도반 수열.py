# 9461
pn = [0] * 100
pn[1:11] = [1,1,1,2,2,3,4,5,7,9,12]
for i in range(11, 101):
  pn[i] = pn[i-1] + pn[i-5]
t = int(input())
for i in range(t):
  c= int(input())
  print(pn[c])