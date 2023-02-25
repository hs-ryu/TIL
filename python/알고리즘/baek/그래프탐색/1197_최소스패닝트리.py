# 크러스컬
def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
    return graph[x]

v,e = map(int,input().split())

graph = [0] + [i+1 for i in range(v)]
info = []

for i in range(e):
    info.append(list(map(int,input().split())))
    
info.sort(key=lambda x:x[2])

result = 0
for s,e,c in info:
    a = find(s)
    b = find(e)
    if a != b:
        if a > b:
            graph[a] = b
        else:
            graph[b] = a
        result += c
print(result)