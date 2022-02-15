#A+B비교
#10 20 40 (10+20) + (30+40) / (10+40) + (50+30)
import heapq
import sys
# input = sys.stdin.readline()

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
while(len(heap)!=1):

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    heapq.heappush(heap, (a+b))
    result += (a+b)
print(result)
    
