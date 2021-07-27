n,k = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)
cnt = 0
jungbok = 1
if arr[0][0] == k:
    print(1)
else:
    for i in range(1,n):
        if arr[i][0] == k:
            if jungbok != 1:
                cnt += jungbok
            else:
                cnt += 1
            break
        if arr[i-1][1:4] != arr[i][1:4]:
            cnt += jungbok
            jungbok = 1
        else:
            jungbok += 1

print(cnt)