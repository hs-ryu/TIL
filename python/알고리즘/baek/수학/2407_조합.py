# 조합 계산 알고리즘
def check(x,arr):
    if x == n:
        if len(arr) == m:
            ans[0] += 1
        return
    arr.append(k[x])
    check(x+1, arr)
    arr.pop(-1)
    check(x+1, arr)

n,m = map(int,input().split())
k = [i for i in range(n)]
ans = [0]
check(0,[])
print(ans[0])

# 답을 위한 풀이
n,m = map(int,input().split())
ans = 1
for i in range(n,n-m,-1):
    ans *= i
# print(ans)
for j in range(1,m+1):
    ans //= j
print(ans)