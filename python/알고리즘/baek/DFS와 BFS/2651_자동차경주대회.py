from collections import deque

L = int(input()) # 한번에 갈 수 있는 거리
N = int(input()) # 정비소 개수
dist = [0] * (N + 2)

d = list(map(int, input().split()))
for i in range(1, N+2):
    dist[i] = dist[i-1] + d[i-1]

t = [0] + list(map(int,input().split())) + [0]

# N = 5
# d = 100, 30, 100, 40, 50 ,60

#         출   1    2    3    4    5    도
# dist = [0, 100, 130, 230, 270, 320, 380]
# t =    [0,  5 ,  10,  4,   11,  7,   0]
visited = [0] * (N+2)
timeCheck = [2**31] * (N+2)
timeCheck[0] = 0

def BFS():
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        for target in range(now+1, N+2):
            # 타겟으로 잡은 정비소를 한번에 가지 못하는 경우, 그 뒤는 더 볼 필요도 없이 못간다.
            if dist[target] - dist[now] > L:
                break
            
            # 정비를 받는게 이득이라면 -> 받게 하자
            if timeCheck[target] > timeCheck[now] + t[target]:
                timeCheck[target] = timeCheck[now] + t[target]
                visited[target] = now
                q.append(target)
result = []
def pri(k, cnt, total):
    if visited[k] == 0:
        print(total)
        print(cnt)
        return
    pri(visited[k], cnt + 1, total + t[visited[k]])
    result.append(visited[k])

# 정비소를 방문하지 않고 한번에 갈 수 있는 경우
if dist[N+1] < L:
    print(0)
    print(0)
# 
else:
    BFS()
    pri(N+1, 0, 0)
    # print(visited)
    # print(timeCheck)
    print(*result)