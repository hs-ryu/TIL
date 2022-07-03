n = int(input())
m = int(input())
lights = list(map(int,input().split()))

h = lights[0]
for i in range(m):
    if i == m - 1:
        temp = n - lights[-1]
    else:
        w = lights[i+1] - lights[i]
        if w % 2:
            temp = w // 2 + 1
        else:
            temp = w // 2
    h = max(h,temp)
print(h)