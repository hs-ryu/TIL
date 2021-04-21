import sys
sys.stdin = open('input2.txt')


def Find_set(x):
    if daepyo[x] == x:
        return x
    return Find_set(daepyo[x])


# KRUSKAL로 풀어보기
T = int(input())
for t in range(1, T+1):
    # 섬의 개수
    N = int(input())
    AL = [[] for _ in range(N+1)]
    x_list = list(map(int ,input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    L = []
    for i in range(N-1):
        for j in range(i+1, N):
            # 무방향이니까 그냥 하나에만 넣어서 체크하자. 어차피 대표자 체크 할거니까
            L.append([i, j, (x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j]) ** 2])
    L.sort(key=lambda x : x[2])
    
    # 대표자 체크 배열(싸이클 체크)
    daepyo = list(range(N))
    # 최소 길이가 들어갈 배열
    tax = [0] * N
    i = 0
    cnt = 0
    # N-1개 고를거임.
    while cnt < N-1:
        # 젤 앞에서 부터 하나씩 들고와서 체크
        current = L[i]
        # 대표자가 같지 않으면? 싸이클 아니니까 추가!
        if Find_set(current[0]) != Find_set(current[1]):
            tax[cnt] = current[2] * E
            # start 지점과 end 지점의 대표자를 맞춰줌 (start 지점으로)
            daepyo[Find_set(current[0])] = Find_set(current[1])
            # 고른 개수 1개 추가
            cnt += 1
            i += 1
        # 같다면? 싸이클 생긴거니까 패스
        else: 
            i += 1
    print('#%d %d' %(t, round(sum(tax))))
        
