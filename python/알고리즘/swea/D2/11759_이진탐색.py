import sys
sys.stdin = open('5176_input.txt')

T = int(input())


def inorder(node):
    global temp
    if node <= N:
        inorder(node*2)
        tree[node] = temp
        temp += 1
        inorder(node*2 + 1)

# 노드 : 1
# inorder(2)
# inorder(4)
# tree[4] = 1
# tree[2] = 2
# inorder(5)
# tree[5] = 3
# tree[1] = 4
# inorder(3)
# inorder(6)
# tree[6] = 5
# tree[3] = 6 


for t in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    temp = 1
    inorder(1)





























# 승호 풀이
def inorder(node):
    if node <= N:
        # 왼쪽
        inorder(node*2)
        global cnt
        tree[node] = cnt
        cnt += 1
        # 오른쪽
        inorder(node*2+1)

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)
    print('#%d %d %d' % (t, tree[1], tree[N//2]))