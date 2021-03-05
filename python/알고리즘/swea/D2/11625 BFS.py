'''
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 너비우선탐색 하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

출력 결과의 예는 다음과 같다.
1-2-3-4-5-7-6
'''

import sys
sys.stdin = open('input1.txt')

def BFS(s):
    # visited 넣고. 큐에 넣기
    Queue = []
    visited = [0 for _ in range(N+1)]
    result = []
    visited[s] = 1
    Queue.append(s)
    while Queue:
        x = Queue.pop(0)
        result.append(x)
        for i in AL[x]:
            if not visited[i]:
                visited[i] = 1
                Queue.append(i)
    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    AL = [[] for _ in range(N+1)]
    for i, j in arr:
        AL[i].append(j)
        AL[j].append(i)
    res = BFS(1)
    ans = ' '.join(list(map(str, res)))
    print('#%d %s' %(t, ans))
