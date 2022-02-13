
# def find_daepyo(x):
#     while daepyo[x] != x:
#         x = daepyo[x]
#     return x

# def union(x,y):
#     daepyo[find_daepyo(y)] = find_daepyo(x)

# n,m = map(int,input().split())

# case = 1
# while n != 0 and m != 0:
#     daepyo = list(range(n+1))
#     for _ in range(m):
#         x,y = map(int,input().split())
#         union(x,y)
    
#     result = 0
#     for i in range(1,n+1):
#         if daepyo[i] == i:
#             result += 1
#     if result > 1:
#         print("Case %d: A forest of %d trees." % (case, result))
#     elif result == 1:
#         print("Case %d: There is one tree." % case)
#     else:
#         print("Case %d: No trees" % case)

#     n,m = map(int,input().split())
#     case += 1

def check(num):
    visited[num] = True
    stack = [num]

    while stack:
        node = stack.pop(0)

        for next_node in tree[node]:
            if tree[node][next_node] == 1:
                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)
                    tree[node][next_node] = 0
                    tree[next_node][node] = 0
                else:
                    return False
    return True
            


tc = 1
while True:
    N,M = map(int,input().split())
    if N+M == 0:
        break
    parent_cnt = [0]*(N+1)
    tree = [{} for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        tree[x][y] = 1
        tree[y][x] = 1
    cnt = 0
    visited = [False]*(N+1)
    for num in range(1,N+1):
        if not visited[num]:
            if check(num):
                cnt += 1
    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')


    tc += 1