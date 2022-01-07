from sys import stdin
input = stdin.readline

d,n,m = map(int,input().split())
islands = [0] * n
for i in range(n):
    islands[i] = int(input().split())
# islands = [0] + islands
islands.sort()
# s,e = 

s,e = 1, islands[-1] - islands[0]
while s <= e:
    k = (s + e) // 2
    
    cnt = 1
    stone = islands[0]
    for i in range(1, n):
        if k <= islands[i] - stone:
            cnt += 1
            stone = islands[i]
    if cnt >= d:
        answer = k
        s = k + 1
    else:
        e = k - 1
print(answer)