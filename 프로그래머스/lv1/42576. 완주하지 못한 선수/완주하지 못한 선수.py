def solution(participant, completion):
    answer = ''

    # 두 리스트를 sorting 한다.
    participant.sort()
    completion.sort()
    
    # completion list의 length 만큼 돌면서, participant에 존재 하지 안흔ㄴ 한명을 찾는다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i] 
    
    # 전부 돌아서 없을 경우에 마지막 주자가 완주하지 못한 것이다.
    return participant[len(participant) - 1]
