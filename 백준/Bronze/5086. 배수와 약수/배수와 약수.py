a=1
b=1
while a!=0 and b!= 0:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  elif b%a == 0:
    print("factor")
  elif a%b == 0:
    print("multiple")
  else:
    print("neither")