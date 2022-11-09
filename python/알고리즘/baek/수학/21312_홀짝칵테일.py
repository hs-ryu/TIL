a,b,c = map(int,input().split())

x = [a,b,c]

y = 1
k = 1
odd = False
for i in range(len(x)):
    if x[i] % 2:
        y *= x[i]
        odd = True
    else:
        k *= x[i]

if odd:
    print(y)
else:
    print(k)
