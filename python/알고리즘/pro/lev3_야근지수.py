import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    # 힙은 작은수부터 정렬되니까, -1을 곱해 큰수가 앞에 오도록한다.
    works = [-w for w in works]
    # 힙으로 만들어주기.
    heapq.heapify(works)
    while n > 0:
        max_val = heapq.heappop(works)
#       1 더해주고 (-1 곱했으니까) 다시 힙에 넣어주기.
        heapq.heappush(works, max_val+1)
        n -= 1

    for w in works:
        answer += w ** 2
    return answer