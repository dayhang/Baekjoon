def solution(numer1, denom1, numer2, denom2):
    a = denom1 * denom2 
    b = numer2 * denom1 + numer1 * denom2
    
    findgcd = max(a, b)
    gcd = 1
    
    for num in range(findgcd, 0, -1):
        if a % num == 0 and b % num == 0:
            gcd = num
            break
            
    answer = [b / gcd, a / gcd]
    return answer