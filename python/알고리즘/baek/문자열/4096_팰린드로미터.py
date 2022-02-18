n = input()
result = []
while n != '0':

    cnt = 0

    if n == n[::-1]:
        result.append(cnt)
    else:
        tmp = len(n)
        while n != n[::-1]:
            cnt += 1
            t = int(n) + 1
            n = str(t).zfill(tmp)
        result.append(cnt)
    n = input()

for i in range(len(result)):
    print(result[i])