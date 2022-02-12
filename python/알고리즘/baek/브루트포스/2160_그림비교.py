n = int(input())

picture = [[] for _ in range(n)]
for i in range(n):
    for _ in range(5):
        picture[i].append(list(input()))

result = []
for i in range(n-1):
    m = i+1
    while m < n:
        hab = 0
        for j in range(5):
            for k in range(7):
                if picture[i][j][k] == picture[m][j][k]:
                    hab += 1
        result.append([i+1,m+1,hab])
        m += 1
result.sort(key=lambda x:x[2])
print(result[-1][0],result[-1][1])