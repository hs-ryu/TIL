n, a, d = map(int,input().split())
songs = list(map(int,input().split()))
flag = 0
now = a
result = 0
for i in range(n):
    if songs[i] == a and flag == 0:
        flag = 1
        now += d
        result += 1
    if flag:
        if songs[i] == now:
            result += 1
            now += d
print(result)