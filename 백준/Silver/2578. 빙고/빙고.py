import sys

bingo = [list(map(int, input().split())) for _ in range(5)]  

numbers = []  
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

def check_bingo():
    cnt = 0 
    # 가로 체크
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt += 1

    # 세로 체크
    for i in range(5):
        if sum([bingo[j][i] for j in range(5)]) == 0:
            cnt += 1

    # 대각선 체크
    if sum([bingo[i][i] for i in range(5)]) == 0:
        cnt += 1
    if sum([bingo[i][4-i] for i in range(5)]) == 0:
        cnt += 1

    return cnt


for i, num in enumerate(numbers):
    
    for j in range(5):
        if num in bingo[j]:
            bingo[j][bingo[j].index(num)] = 0
            break

    if check_bingo() >= 3:
        print(i+1)  
        sys.exit() 

