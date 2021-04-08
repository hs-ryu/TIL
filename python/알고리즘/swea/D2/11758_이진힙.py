import sys
sys.stdin = open("sample_input.txt")

def insert(node, idx):
    tree[idx] = node
    while tree[idx//2] > node and idx != 1:
        tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
        idx //= 2


T = int(input())
for t in range(1, T+1):
    N = int(input())
    node_list = list(map(int,input().split()))
    tree = [0] * (N+1)
    for i in range(N):
        insert(node_list[i], i+1)
    answer = 0
    while N != 1:
        answer += tree[N//2]
        N //= 2
    print("#%d %d" %(t, answer))


























# # 승현 풀이
# def insert(node, idx):
#     tree[idx] = node
#     while tree[idx//2] > node and idx != 1:
#         tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
#         idx //= 2
#     return
# for t in range(1, int(input())+1):
#     N = int(input())
#     node_list = list(map(int, input().split()))
#     tree = [0]*(N+1)
#     for i in range(N):
#         insert(node_list[i], i+1)
#     ans = 0
#     while N != 1:
#         ans += tree[N//2]
#         N //= 2
#     print("#%d %d" %(t, ans))






# 트리 안쓰고 풀어보기 대ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ실패
# def find_node(x, hab):
#     global total
#     if x == N-1:
#         total = hab
#         return 0
#     if x >= N:
#         return 0
#     find_node(2*x+1, hab + integer[x])
#     find_node(2*x+2, hab + integer[x])
#
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     integer = list(map(int, input().split()))
#
#     i = 0
#     while i < N:
#         if 2*i+1 < N and integer[i] > integer[2*i+1]:
#             integer[i], integer[2 * i + 1] = integer[2 * i + 1], integer[i]
#             i = 0
#         elif 2*i+2 < N and integer[i] > integer[2*i+2]:
#             integer[i], integer[2 * i + 2] = integer[2 * i + 2], integer[i]
#             i = 0
#         i += 1
#
#     total = 0
#     find_node(0,0)
#     print('#%d %d' %(t,total))