from copy import deepcopy

def check(k):
    new_friends = deepcopy(friends)
    q = new_friends[k][:]
    while q:
        temp,length = q.pop(0)
        if visited[temp] == 0:
            visited[temp] = length
            for j in range(len(new_friends[temp])):
                new_friends[temp][j][1] = length+1
                q.append(new_friends[temp][j])
n = int(input())

friends = [[] for _ in range(n+1)]
while True:
    n1,n2 = map(int,input().split())
    if n1 == -1 and n2 == -1:
        break
    friends[n1].append([n2,1])
    friends[n2].append([n1,1])
print(friends)

total_cnt = 0
max_v = n
results = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    check(i)
    print(visited)
    temp_cnt = 0
    temp_v = 0
    for j in range(1,n+1):
        if visited[j]:
            temp_cnt += 1
            if temp_v < visited[j]:
                temp_v = visited[j]  
    if total_cnt <= temp_cnt:
        total_cnt = temp_cnt
        if temp_v == max_v:
            results.append(i)
        elif temp_v < max_v:
            results = [i]
print(results)