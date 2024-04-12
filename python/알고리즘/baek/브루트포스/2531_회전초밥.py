N,d,k,c = map(int, input().split())

sushis = [int(input()) for _ in range(N)]

# 초밥 하나씩 시작해서 먹어보기
result = 0
for i in range(N):
    check = [0] * 3001
    cnt = 0
    for j in range(i, i+k, 1):
        if j >= N:
            j -= N
        sushi = sushis[j]

        if check[sushi]:
            continue
        check[sushi] = 1
        cnt += 1
    if check[c] == 0:
        cnt += 1
    
    result = max(result, cnt)
print(result)
