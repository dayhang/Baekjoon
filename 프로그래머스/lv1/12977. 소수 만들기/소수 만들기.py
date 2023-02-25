from itertools import combinations

def prime(num):
    if num==0 or num==1:
        return False
    else:
        for i in range(2, (num//2)+1):
            if num%i == 0:
                return False
    return True

def solution(nums):
    answer = 0
    c = list(combinations(nums,3))
    for arr in c:
        if prime(sum(arr)):
            answer += 1
    return answer
    