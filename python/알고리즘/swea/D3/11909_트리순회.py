import sys
sys.stdin = open('ex03_input.txt')



# 각각 다 구현해보기
'''
def preorder(x):
    if x:
        result.append(x)
        preorder(nodes[x][0])
        preorder(nodes[x][1])

def inorder(x):
    if x:
        inorder(nodes[x][0])
        result.append(x)
        inorder(nodes[x][1])

def postorder(x):
    if x:
        postorder(nodes[x][0])
        postorder(nodes[x][1])
        result.append(x)


T = int(input())
for t in range(1, T+1):
    V = int(input())
    nodes = [[0,0] for _ in range(V+1)]
    ganseon = list(map(int, input().split()))
    for i in range(0, len(ganseon)-1, 2):
        if nodes[ganseon[i]][0] == 0:
            nodes[ganseon[i]][0] = ganseon[i+1]
        else:
            nodes[ganseon[i]][1] = ganseon[i+1]
    print('#%d' %t)
    result = []
    preorder(1)
    print('-'.join(map(str,result)))
    result = []
    inorder(1)
    print('-'.join(map(str,result)))
    result = []
    postorder(1)
    print('-'.join(map(str,result)))
'''

def order(x):
    if x:
        result_pre.append(x)
        order(nodes[x][0])
        result_in.append(x)
        order(nodes[x][1])
        result_post.append(x)


# 한번에 모다서
T = int(input())
for t in range(1, T+1):
    V = int(input())
    nodes = [[0,0] for _ in range(V+1)]
    ganseon = list(map(int, input().split()))
    for i in range(0, len(ganseon)-1, 2):
        if nodes[ganseon[i]][0] == 0:
            nodes[ganseon[i]][0] = ganseon[i+1]
        else:
            nodes[ganseon[i]][1] = ganseon[i+1]

    result_pre, result_in, result_post = [],[],[]
    order(1)
    print('#%d' %t)
    print('-'.join(map(str,result_pre)))
    print('-'.join(map(str,result_in)))
    print('-'.join(map(str,result_post)))