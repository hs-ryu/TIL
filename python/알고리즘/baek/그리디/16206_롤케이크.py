n, m = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort(key=lambda x: (x%10,x))
result = 0
for cake in cakes:
    cnt = cake//10
    if not cake%10:
        if cnt-1 <= m:
            result += cnt
            m -= cnt -1
        else:
            result += m
            m -= m
    else:
        if cnt <= m:
            result += cnt
            m -= cnt
        else:
            result += m
            m -= m
print(result)