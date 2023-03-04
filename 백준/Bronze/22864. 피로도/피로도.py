# 22864

a,b,c,m = map(int, input().split())

cnt = 0

work = 0
piro = 0
# 조건 1 m이 10 보다 낮으면안됨.
# 조건 2 cnt 가 0 보다 작으면안됨.
# 조건 3 

if a>m:
  print(0)
else:
  while cnt != 24:
    cnt += 1
  # can work
    if piro + a <= m :
      work += b
      piro += a
    else:
      if piro - c >= 0:
        piro -=c
      else:
        piro = 0
  print(work)
