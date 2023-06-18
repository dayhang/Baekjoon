def solution(clothes):
    # 1. 옷을 종류 별로 구분한다.
    
    hash_map = {}
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        
        
    # 2. 입지 않는 경우를 추가하여 모든 경우를 계산한다.
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    
    # 3. 아무 종류의 옷을 입지 않았을 경우를 제외 한다.
    return answer - 1