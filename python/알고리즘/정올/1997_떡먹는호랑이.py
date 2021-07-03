def check():
    for i in range(1,int(k/2)):
        for j in range(i,k):
            if k == (i*a[d-1] + j*b[d-1]):
                result = [i,j]
            elif k < (i*a[d-1] + j*b[d-1]):
                break
    return result

d, k = map(int,input().split())
a,b = [0] * d,[0] * d
a[0],a[1] = 1,0
b[0],b[1] = 0,1
for i in range(2,d):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]
result = check()
print(result[0])
print(result[1])