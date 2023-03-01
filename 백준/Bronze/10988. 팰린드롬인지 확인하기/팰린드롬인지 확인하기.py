word = str(input())
b = str()
for i in range(1, len(word)+1):
  a = word[-i]
  b = b + a

if word == b:
  print(1)
else:
  print(0)