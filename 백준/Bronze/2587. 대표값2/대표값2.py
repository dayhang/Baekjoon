list=[]
for _ in range(5):
  s = int(input())
  list.append(s)
list.sort()

print(int(sum(list)/5))
print(list[2])