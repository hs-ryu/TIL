from sys import stdin
input = stdin.readline
n = int(input())

points = [list(map(int,input().split())) for _ in range(n)]
result = 0
for i in range(n-2):
    x1,y1 = points[i]
    for j in range(i+1,n-1):
        x2,y2 = points[j]
        for k in range(j+1,n):
            x3,y3 = points[k]
            l1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
            l2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2)
            l3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2)
            m = sorted([l1,l2,l3])
            if m[0] + m[1] == m[2]:
                result += 1
print(result)