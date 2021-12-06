
# dp
# 풀이 참고함..



n = int(input())
# 포도주가 놓여있는 배열
# i-3 연산을 위해 3부터 n+3까지
arr = [0] * (n+3)
# 포도주를 처묵하는 dp 배열
wines = [0] * (n+3)
for i in range(3, n+3):
    arr[i] = int(input())
    
answer = 0

# 6, 10, 13, 9, 8, 1
# 6 -> 10 -> 9 -> 1  : 33 (최대)
# 선택 -> 연속 3잔 안됨.

# arr = 0, 0, 0, 6, 10, 13, 9, 8, 1
# wines = 0, 0, 0, 0, 0, 0, 0, 0, 0
# i = 3
# 0 + 0 + 6    -     0 + 6
# wines[3] = 6
# i = 4
# 0 + 6 + 10     -    0 + 10
# wines[4] = 16
# i = 5
# 0 + 10 + 13    -     6 + 13
# wines[5] = 23
# i = 6
# 6 + 13 + 9    -     16 + 9
# wines[6] = 27
# i = 7
# 16 + 9 + 8     -      23 + 8
# wines[7] = 33   <- 최대
# i = 8
# 23 + 8 + 1    -    27 + 1
# wines[8] = 32


for i in range(3, n+3):
    
    # i를 기준으로 비교. 
    # i-3번째까지 마신것에서, 하나 띄고 i-1번째와 i번째를 마시는 경우 (안마심, 마심, 마심)
    # 또는 i-3번째 까지 마신것에서, i-2번째도 마시고, 하나 띄고 i번째 마시는 경우 (마심, 안마심, 마심) 
    if (wines[i-3] + arr[i-1] + arr[i] > wines[i-2] + arr[i]):
        wines[i] = wines[i-3] + arr[i-1] + arr[i]
    else:
        wines[i] = wines[i-2] + arr[i]
    
    # 최대여야하므로
    if wines[i-1] > wines[i]:
        wines[i] = wines[i-1]

print(wines[n+2])