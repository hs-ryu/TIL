import sys
sys.stdin = open('5249_input.txt')


def find_daepyo(x):
    while daepyo[x] != x:
        x = daepyo[x]
    return x


# kruskal로 풀기
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    ganseons = [list(map(int, input().split())) for _ in range(E)]
    # 가중치를 기준으로 오름차순 정렬
    ganseons.sort(key=lambda x : x[2])
    daepyo = list(range(V+1))

    cnt = 0
    i = 0
    result = 0
    while cnt < V:
        temp = ganseons[i]
        # 같지 않으면 싸이클 아니니까 
        if find_daepyo(temp[0]) != find_daepyo(temp[1]):
            result += temp[2]
            daepyo[find_daepyo(temp[0])] = find_daepyo(temp[1])
            cnt += 1
            i += 1
        else:
            i += 1
    print('#%d %d' %(t, result))