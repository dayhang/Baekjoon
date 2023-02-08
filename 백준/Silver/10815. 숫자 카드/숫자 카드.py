import sys
n = int(sys.stdin.readline())
n_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_cards = list(map(int, sys.stdin.readline().split()))

_dict = {}  
for i in range(n):
    _dict[n_cards[i]] = 0  

for j in range(m):
    if m_cards[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')