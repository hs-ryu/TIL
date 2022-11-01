
n,k = map(int,input().split())
dp = [0] * (n*2)

section = list(map(int,input().split()))
check = False

for i in range(n):
    k -= section[i]
    if k < 0:
        print(i+1)
        check = True
        break

if check != True:
    for i in range(n-1,-1,-1):
        k -= section[i]
        if k < 0:
            print(i+1)
            break

