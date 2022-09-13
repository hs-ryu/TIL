n = int(input())
steel = sorted(list(map(int, input().split())))
ans = 0
s = sum(steel)
for i in range(n):
    s -= steel[i]
    ans += steel[i] * s
print(ans)