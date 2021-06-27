import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while 1:
        try:
            count +=  1
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            
            if scoville[0] >= K:
                return count
        except:
            return -1
