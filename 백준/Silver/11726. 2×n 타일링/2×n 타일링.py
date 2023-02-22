# 11726 
t = [1,2]    # first 2 cases 
for i in range(2,1000):
  t.append(t[i-2] + t[i-1])    # append nth case to t[n-1]
n = int(input())
print(t[n-1] % 10007)    # print nth case -> t[n-1] and %10007