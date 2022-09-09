r,c,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(3)]

# 0,0을 기준으로 맞춰주기
r -= 1
c -= 1

while True:
    if a[r][c] == k:
        break
    # 행이 열보다 큰 경우
    if len(a) >= len(a[0]):
        pass
        

    # 열이 행 보다 큰경우
    else:
        pass
    
    a = []

