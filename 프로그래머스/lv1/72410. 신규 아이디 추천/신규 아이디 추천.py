
def solution(new_id):
    answer =''
    # 1. 모든 대문자를 대응되는 소문자로 치환한다.
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, -, _, . 를 제외한 모든 문자를 제거한다.
    for c in new_id:
        if c.isalnum() or c in "-_.":
            answer += c
            
    # 3. .가 두번 이상일 경우 . 로 치환한다. while
    while ".." in answer:
        answer = answer.replace("..", ".")
    
    # 4. .가 처음이나 끝에 위치한다면, 제거한다.  if
    if answer[0:1] == '.':
        answer = answer[1:]
        
    if answer[-1:0] == '.':
        answer = answer[:-1]
    # 5. 빈 문자열이면 a 로 치환한다. if
    if answer == '':
        answer = 'a'
    
    # 6. 길이가 16자 이상이면, 첫 15개 문자를 제외한 나머지 문자들을 제거한다. 만약 제거후 마침표가 끝에 위치한다면, . 를 제거한다. slice
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7. 길이가 2자이하라면, 길이가 3이 될때까지 반복해서 끝에 붙인다. while
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer