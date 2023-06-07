arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a, b = map(int, input().split())
digit = ""

while a != 0:
    digit += str(arr[a % b])
    a = a//b

print(digit[::-1])