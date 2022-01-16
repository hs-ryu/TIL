
# 당연히 시간초과
# n,m = map(int,input().split())
# h = [0]+list(map(int,input().split()))

# for _ in range(m):
#     a,b,k = map(int,input().split())
#     for i in range(a,b+1):
#         h[i] += k

# print(*h[1:])

from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
h = [0] + list(map(int,input().split()))

arr = [0] * (n+2)
for _ in range(m):
    a,b,k = map(int,input().split())
    arr[a] += k
    arr[b+1] -= k
# arr = [0,-3,-3,-3,-3,-3,0,0,0,0,0]
# arr = [0,-3,-3,-3,-3,-3,5,5,5,5,5]
# arr = [0,-3,-1,-1,-1,-1,7,7,5,5,5]

# arr = [0,-3,0,0,0,0,3,0,0,0,0,0]
# arr = [0,-3,0,0,0,0,8,0,0,0,0,-5]
# arr = [0,-3,2,0,0,0,8,0,-2,0,0,-5]

# arr = [0,-3,-1,-1,-1,-1,7,7,5,5,5,-5]
print(arr)
for i in range(1,n+1):
    arr[i] = arr[i-1] + arr[i]
print(arr)
for i in range(1,n+1):
    h[i] += arr[i]
print(*h[1:])
