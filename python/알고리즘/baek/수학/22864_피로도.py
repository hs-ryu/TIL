a,b,c,m = map(int,input().split())

result = 0
piro = 0
i = 1
while i < 25:
    if piro + a <= m:
        piro += a
        result += b
    else:
        piro -= c
        if piro < 0:
            piro = 0
    i += 1
if piro > m:
    result = 0
print(result)