# 부루투포스
n,m = map(int,input().split())
arr = [[]]

for _ in range(n):
    a = [0] + list(map(int,input().split()))
    arr.append(a)

k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())
    result = 0
    for a in range(i,x+1):
        for b in range(j,y+1):
            result += arr[a][b]
    print(result)

