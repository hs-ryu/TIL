n = int(input())
arr = []
for _ in range(n):
    name, point = input().split()
    arr.append([name, int(point)])
arr.sort(key=lambda x:(-x[1],x[0]))
for i in range(n):
    print(*arr[i])