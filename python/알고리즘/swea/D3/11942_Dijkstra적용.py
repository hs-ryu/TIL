import sys
sys.stdin = open('ex04_input.txt')

T = int(input())
for t in range(1, T+1):
    V, E = map(int ,input().split())
    AL = [[] for _ in range(V)]
    for i in range(E):
        s, e, l = input().split()
        AL[ord(s)-97].append([ord(e)-97, int(l)])
    # 거리 정보를 저장할 distance 배열
    distance = [987654321] * V
    # 방문했는지 여부 확인할 visited 배열
    visited = [0] * V
    # a부터 시작한다고 했으니까 0번째 거리를 0으로 초기화
    distance[0] = 0
    # 마찬가지 방문처리
    visited[0] = 1
    # 시작 정점에서 연결된 정점들 사이의 거리를 갱신
    for node in AL[0]:
        distance[node[0]] = node[1]
    
    # distance 배열에서 제일 작은값 찾고, 그 값의 인덱스에 해당하는 정점을 가져옴
    i = 0
    while i < (V-1):
        min_v = 9876543210
        min_idx = 0
        for j in range(V):
            if visited[j] == 1:
                continue
            if distance[j] < min_v:
                min_v = distance[j]
                min_idx = j
        visited[min_idx] = 1
        # 가져온 정점에서 연결된 정점들을 탐색하며
        # 현재 연결된 정점들의 거리 정보와 (가져온 정점 거리정보 + 둘 사이의 거리) 를 비교하여 더 작은값을 distance 배열에 갱신
        for node in AL[min_idx]:
            distance[node[0]] = min(distance[node[0]], distance[min_idx] + node[1])
        i += 1
    print('#%d %s' %(t, ' '.join(map(str, distance))))
        