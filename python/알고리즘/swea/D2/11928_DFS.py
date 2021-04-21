
# 반복문
def DFS(s):
    stack = [s]
    while stack:
        x = stack.pop()
        if visited[x] == 0:
            visited[x] = 1
            result.append(x)
            AL[x].sort(reverse=True)
            for i in AL[x]:
                if visited[i] == 0:
                    stack.append(i)


T = int(input())
for t in range(1, T+1):
    V, E = map(int ,input().split())
    AL = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    visited = [0] * (V+1)
    result = []
    DFS(1)
    print('#%d %s' %(t, ' '.join(map(str, result))))



# 재귀
'''

def DFS(s):
    for i in AL[s]:
        if visited[i] == 0:
            result.append(i)
            visited[i] = 1
            DFS(i)

T = int(input())
for t in range(1, T+1):
    V, E = map(int ,input().split())
    AL = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    visited = [0] * (V+1)
    visited[1] = 1
    result = [1]
    DFS(1)
    print('#%d %s' %(t, ' '.join(map(str, result))))

'''