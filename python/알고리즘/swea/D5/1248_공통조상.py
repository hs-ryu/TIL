import sys
sys.stdin = open("input.txt")

def inorder(x):
    global cnt
    if x:
        inorder(tree[x][0])
        cnt += 1
        inorder(tree[x][1])

def preorder(x):
    if x:
        josang[tree[x][0]].extend(josang[x])
        josang[tree[x][0]].append(x)
        josang[tree[x][1]].extend(josang[x])
        josang[tree[x][1]].append(x)
        preorder(tree[x][0])
        preorder(tree[x][1])

T = int(input())
for t in range(1,T+1):
    V, E, node1, node2 = map(int, input().split())
    gansun = list(map(int, input().split()))

    tree = [[0,0] for _ in range(V+1)]
    josang = [[] for _ in range(V+1)]
    for i in range(0, len(gansun)-1 , 2):
        if tree[gansun[i]][0] == 0:
            tree[gansun[i]][0] = gansun[i+1]
        else:
            tree[gansun[i]][1] = gansun[i+1]
    preorder(1)
    max_idx = 0
    max_value = 0
    for i in josang[node1]:
        if i in josang[node2]:
            if max_idx < josang[node2].index(i):
                max_idx = josang[node2].index(i)
    max_value = josang[node2][max_idx]
    cnt = 0
    inorder(max_value)
    print('#%d %d %d' %(t, max_value, cnt))
