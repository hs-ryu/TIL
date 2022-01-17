from sys import stdin
input = stdin.readline

def BFS():
    queue = []
    for i in range(1, n + 1):
        # 선수과목 없는 놈들부터 정리
        if degree[i] == 0:
            queue.append(i)
            result[i] = 1
    while queue:
        temp = queue.pop(0)
        for i in relation[temp]:
            degree[i] -= 1
            result[i] = max(result[temp] + 1, result[i])
            if degree[i] == 0:
                queue.append(i)

n, m = map(int, input().split())
degree = [0 for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]
relation = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 선수과목 집어넣기
    relation[a].append(b)
    # 선수과목 수 증가
    degree[b] += 1
BFS()
print(*result[1:])
