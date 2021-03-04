'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

def DFS(x):
    visit = []
    stack = []
    visited = [0 for _ in range(N+1)]
    stack.append(x)
    visited[x] = 1

    while stack:
        y = stack.pop()
        visit.append(y)
        for i in AL[y]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
    return visit


def BFS(x):
    visit = []
    Queue = []
    visited = [0 for _ in range(N+1)]
    Queue.append(x)
    visited[x] = 1

    while Queue:
        y = Queue.pop(0)
        visit.append(y)
        for i in AL[y]:
            if not visited[i]:
                Queue.append(i)
                visited[i] = 1
    return visit


N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
AL = [[] for _ in range(N+1)]
for i,j in arr:
    AL[i].append(j)
    AL[j].append(i)
i = 0
while i < len(AL):
    AL[i].sort()
    i += 1
BFS_result = BFS(V)
i = 0
while i < len(AL):
    AL[i].sort(reverse=True)
    i += 1
DFS_result = DFS(V)
print(*DFS_result)
print(*BFS_result)
