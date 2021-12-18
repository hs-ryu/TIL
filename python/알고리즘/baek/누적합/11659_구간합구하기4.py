# n,m = map(int, input().split())
# nums = [0]+list(map(int,input().split()))

# for _ in range(m):
#     s,e = map(int,input().split())
#     print(sum(nums[s:e+1]))

# 이거 안쓰면 시간초과
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = [0]+list(map(int,input().split()))

nujeock = [0] * (n+1)
for i in range(1, n+1):
    nujeock[i] = nums[i] + nujeock[i-1]

for _ in range(m):
    s,e = map(int,input().split())
    print(nujeock[e] - nujeock[s-1])