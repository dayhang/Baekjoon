n = int(input())
i = 0
s = n

while True:
  a = s//10
  b = s%10
  c = (a+b)%10
  s = (b*10)+c
  i += 1
  if n == s:
    break

print(i)
