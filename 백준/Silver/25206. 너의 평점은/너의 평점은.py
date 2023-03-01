#25206

count = 0
countb = 0
for i in range(20):
  a, b, c = map(str, input().split())
  b = float(b)
  c = str(c)
  if c[0] == "A":
    countb += b
    if c[1] == "+":
      count += (b * 4.5)
    else:
      count += (b * 4.0)
  elif c[0] == "B":
    countb += b
    if c[1] == "+":
      count += (b * 3.5)
    else:
      count += (b * 3.0)
  elif c[0] == "C":
    countb += b
    if c[1] == "+":
      count += (b * 2.5)
    else:
      count += (b * 2.0)
  elif c[0] == "D":
    countb += b
    if c[1] == "+":
      count += (b * 1.5)
    else:
      count += (b * 1.0)
  elif c[0] == "P":
    continue
  else:
    countb += b

print(round(count/countb,6))