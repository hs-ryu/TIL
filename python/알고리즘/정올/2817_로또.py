

# def DFS(level, k, r):
#     if level == len(lotto_num):
#         if len(k) == r:
#             print(*k)
#         return
#     k.append(lotto_num[level])
#     DFS(level+1,k,r)
#     k.pop()
#     DFS(level+1,k,r)
# input_num = list(map(int, input().split()))
# lotto_num = input_num[1:]
# DFS(0,[],6)


def nCr(n, ans, r):
    if n == len(lotto_num):
        if len(ans) == r:
            print(*ans)
        return
    ans.append(lotto_num[n])
    nCr(n+1,ans,r)
    ans.pop()
    nCr(n+1,ans,r)
input_num = list(map(int, input().split()))
lotto_num = input_num[1:]
DFS(0,[],6)
