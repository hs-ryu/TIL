def check(cnt):
    if cnt >= len(a):
        x = int("".join(sel))
        if x < int(b):
            if x != int(a):
                if result[0] < x:
                    result[0] = x
        return
    
    for i in range(len(a)):
        if visited[i] == 0:
            if cnt == 0 and a[i] == '0':
                continue
            visited[i] = 1
            sel[cnt] = a[i]
            check(cnt+1)
            visited[i] = 0

a,b = input().split()
visited = [0] * len(a)
sel = [""] * len(a)
result = [-1]
check(0)
print(result[0])