# 11478

s = input()
house = set()

for i in range(len(s)):
  for j in range(i, len(s)):
    house.add(s[i:j+1])

print(len(house))