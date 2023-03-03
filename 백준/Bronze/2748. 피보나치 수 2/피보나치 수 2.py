f = int(input())
# f 번째 피보나치 수

arr = [0] * (f+1)
arr[0] = 0
arr[1] = 1

for i in range(2, f+1):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[f])
                      