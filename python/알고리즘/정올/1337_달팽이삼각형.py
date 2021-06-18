n = int(input())

r = -1
c = -1
k = 0
arr = [[''] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if i%3==0:
            r += 1
            c += 1
        elif i % 3 == 1:
            c -= 1
        elif i % 3 == 2:
            r -= 1
        arr[r][c] = k % 10
        k += 1
for i in range(n):
    print(*arr[i])