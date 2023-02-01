n = int(input())   #3kg, 5kg
b = 0
while n >= 0:
    if n % 5 ==0:
        b += (n//5)
        print(b)
        break
    n -= 3
    b += 1
else:
    print(-1)