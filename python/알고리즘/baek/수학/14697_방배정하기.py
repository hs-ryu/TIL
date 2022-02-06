a,b,c,n = map(int,input().split())

flag = 0
# a,b,c의 최솟값이 1이니까. n의 최댓값 300에 맞추기 위해선 100까지 곱해봐야함.
for i in range(101):
    A = i * a
    if A > n:
        break
    for j in range(101):
        B = j * b
        if A + B > n:
            break
        for k in range(101):
            C = k * c
            if A + B + C > n:
                break
            if A + B + C == n:
                flag = 1
                result = 1
                break
        if flag:
            break
    if flag:
        break
if not flag:
    result = 0
print(result)
            
