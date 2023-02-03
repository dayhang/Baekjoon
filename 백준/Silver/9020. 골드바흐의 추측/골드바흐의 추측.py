def prime(x):
  if x ==1:
    return False
  for j in range(2, int(x**0.5) +1):
    if x % j == 0:
      return False
  return True

for _ in range(int(input())):
  number = int(input())
  a, b = number//2, number//2
  while a > 0:
    if prime(a) and prime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1