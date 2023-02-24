# 9663
n = int(input())
row = [0] * n
count = 0

# 퀸이 합당한 위치에 놓여져 있는지 확인하기
def check(x):
  for i in range(x):
    # 다음 퀸의 위치는 가로, 새로, 대각선에 있을 수 없다.
    if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
      # 따라서 위치하는 경우 -> False
      return False
  return True

def dfs(x):
  global count
  # 조건 충족시 경우의 수 +1
  if x == n:
    count += 1
    return
  for i in range(n):
    row[x] = i
    # 만약에 check -> True일 경우(합당한 위치일 경우)
    if check(x):
      dfs(x+1)

dfs(0) # 0 부터
print(count)
