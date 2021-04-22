import sys
sys.stdin = open('5251_input.txt')

# 다익스트라로 풀어보기

def dijkstra(s):
    distance = [11] * (N + 1)
    visited = [0] * (N+1)
    visited[s] = 1
    for node in AL[s]:
        distance[node[0]] = node[1]
    
    i = 0
    while i < N-1:
        min_v = 11
        min_idx = 0
        for j in range(N+1):
            if visited[j] == 1:
                continue
            if distance[j] < min_v:
                min_v = distance[j]
                min_idx = j

        visited[min_idx] = 1
        for node in AL[min_idx]:
            distance[node[0]] = min(distance[node[0]], distance[min_idx] + node[1])
            
        i += 1
    return distance[N]

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        AL[s].append([e, w])
    result = dijkstra(0)
    print('#%d %d' %(t, result))


