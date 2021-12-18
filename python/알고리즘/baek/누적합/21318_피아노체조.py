import sys
input = sys.stdin.readline

n = int(input())
difficulty = [0] + list(map(int, input().split()))
q = int(input())

miss = [0] * (n+1)
for i in range(1, n+1):
    if (difficulty[i-1] > difficulty[i]):
        miss[i] = miss[i-1]+1
    else:
        miss[i] = miss[i-1]
# print(miss)
for _ in range(q):
    x, y = map(int,input().split())
    print(miss[y]-miss[x])