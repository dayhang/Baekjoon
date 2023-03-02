import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap1 = []
# 1번 힙
heap2 = []
# 2번 힙
mid = []
# 중위값

for i in range(n):
    x = int(input())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, (-x,x))
    else:
        heapq.heappush(heap2, (x,x))
        
    if heap2 and heap1[0][1] > heap2[0][0]:
        min = heapq.heappop(heap2)[0]
        max = heapq.heappop(heap1)[1]
        heapq.heappush(heap1, (-min,min))
        heapq.heappush(heap2, (max, max))
    
    mid.append(heap1[0][1])
    
for num in mid:
    print(num)
          