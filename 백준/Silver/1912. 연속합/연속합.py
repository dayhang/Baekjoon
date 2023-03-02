#1912
n = int(input())
li = list(map(int,input().split()))
tot = [li[0]]
for i in range(len(li)-1):
  tot.append(max(tot[i]+ li[i+1],li[i+1]))
print(max(tot))