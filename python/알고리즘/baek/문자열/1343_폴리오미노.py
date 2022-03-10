s = list(input().split('.'))
result = ""
for i in range(len(s)):
    check = s[i]
    flag = 0
    if len(check) % 2:
        flag = 1
        break

    temp = ""
    i = len(check)
    while i >= 2:
        if i >= 4:
            temp += 'AAAA'
            i -= 4
        else:
            temp += 'BB'
            i -= 2
    result += temp
    result += '.'

if flag:
    print(-1)
else:
    print(result[:-1])