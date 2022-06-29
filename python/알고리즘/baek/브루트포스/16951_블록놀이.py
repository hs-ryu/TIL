n,k = map(int,input().split())
blocks = list(map(int,input().split()))
result = n
for i in range(n):
    cnt = 0
    for j in range(n):
        temp = k * (j-i) + blocks[i]
        if temp < 1:
            cnt = n
            break
        if temp != blocks[j]:
            cnt += 1
    result = min(result, cnt)
print(result)
