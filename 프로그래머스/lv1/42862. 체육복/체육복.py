def solution(n, lost, reserve):
    # 1. set 을 만든다
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    
    # 2. 여분 기준으로 앞뒤 확인 하여 체육복 빌려준다
    for reserve in reserve_only:
        front = reserve -1
        back = reserve +1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    
    # 3. 전체 에서 lost_only 에 남은 학생 수 빼기
    return n - len(lost_only)
    