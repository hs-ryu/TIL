# 86% 에서 틀림..

def search_most_distance(start_node):
    q = graphs[start_node][:]
    while q:
        s,e,dist = q.pop(0)
        if visited[e] == 0:
            node_dist[e] = node_dist[s] + dist
            visited[e] = 1
            q.extend(graphs[e][:])

    return

n = int(input())
graphs = [[] for _ in range(n+1)]

for i in range(n-1):
    n1,n2,c = map(int,input().split())
    graphs[n1].append([n1,n2,c])
    graphs[n2].append([n2,n1,c])
# print(graphs)

# 1. 1번부터 제일 멀리 있는놈 찾기.(루트노드 1번)
# 2. 그놈부터 제일 멀리있는놈 찾기.
# 3. 두놈 사이의 길이 구하기.

node_dist = [0] * (n+1)
visited = [0] * (n+1)
# 1번 노드는 볼 필요 없으니까.
visited[1] = 1
search_most_distance(1)
# print(node_dist)
# 여기까진 굳

# 1번노드에서 제일 먼 놈 -> 그 놈과 가장 먼놈 찾기.
max_v = max(node_dist)
start_nodes = []
for i in range(n+1):
    if node_dist[i] == max_v:
        start_nodes.append(i)


result = 0
for i in range(len(start_nodes)):
    node_dist = [0] * (n+1)
    visited = [0] * (n+1)
    start_node = start_nodes[i]
    search_most_distance(start_node)
    if max(node_dist) > result:
        result = max(node_dist)
print(result)