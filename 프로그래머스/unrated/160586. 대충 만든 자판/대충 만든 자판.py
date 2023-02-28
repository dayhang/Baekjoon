def solution(keymap, targets):
    answer = []
    
    for w in targets:
        count = 0
        for c in w:
            check = False
            mc = 101
            for k in keymap:
                if c in k:
                    mc = min(k.index(c)+1, mc)
                    check = True
            
            if not check:
                count = -1
                break
            
            count += mc
        answer.append(count)
            
    return answer