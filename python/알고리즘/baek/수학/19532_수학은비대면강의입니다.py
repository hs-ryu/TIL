a,b,c,d,e,f = map(int,input().split())

flag = 0
for i in range(-999,1000):
    for j in range(-999,1000):
        if (a * i) + (b * j) ==c and (d*i) + (e*j) == f:
            x,y = i,j
            flag = 1
            break
    if flag:
        break
print(x,y)