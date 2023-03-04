# 2810

n = int(input())
a = input()

count = 1

for i in range(len(a)):
  if a[i] == 'S':
    count += 1
  elif a[i] == 'L':
    count += 0.5

if count > len(a):
  print(len(a))
else:
  print(int(count))
  