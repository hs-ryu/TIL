x,y,p1,p2 = map(int,input().split())

result = -1
flag = 0
for i in range(101):
    p = (i * x) + p1
    for j in range(101):
        q = (j * y) + p2
        if q == p:
            result = p
            flag = 1
            break
    if flag:
        break
print(result)