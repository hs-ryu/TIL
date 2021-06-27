'''
# 이렇게 짜면 비효율적
def prime(num):
    if num < 2:
        return False
    root = num ** 0.5
    for i in range(2,int(root)+1):
        if num % i == 0:
            return False
    return True

m,n = map(int,input().split())

result = 0
for i in range(m,n+1):
    if prime(i):
        result += 1
print(result)
'''
arr = [0] * 2000005

def eratos(n):
    # 소수가 아닌 애들은 배열에서 1로 처리.
    arr[0] = arr[1] = 1
    root = n ** 0.5
    for i in range(2, int(root) + 1):
        if arr[i] == 0:
            for j in range(int(root), n+1, i):
                arr[j] = 1

s,e = map(int, input().split())
cnt = 0
eratos(e)
for i in range(s+1,e+1):
    if arr[i] == 0:
        cnt += 1
print(cnt)

