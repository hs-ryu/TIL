from collections import deque

N,Q = map(int,input().split())

graph = [deque() for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append([q,r])
    graph[q].append([p,r])


# [[], [[2,3]], [[1,3], [3,2], [4,4]], [[2,2]], [[2,4]]]
# 경로는 반드시 "1개" 존재함

for i in range(Q):
    answer = 0
    k,v = map(int,input().split())
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    # v 동영상을 볼 때 USADO가 k 이상인 애들은 몇개인가?
    queue = deque()

    for t,y in graph[v]:
        visited[t] = 1
        queue.append([t,y])

    while queue:
        node, value = queue.popleft()

        if value >= k:
            answer += 1
            for d,b in graph[node]:
                if visited[d] == 0:
                    queue.append([d,min(b,value)])
                    visited[d] = 1


    print(answer)
                




