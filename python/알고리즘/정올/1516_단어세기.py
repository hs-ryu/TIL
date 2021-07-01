
while True:
    string = input().split()
    dic = dict()
    if string[0] == 'END':
        break
    for st in string:
        if st in dic:
            dic[st] += 1
        else:
            dic[st] = 1
    result = sorted(dic.items())
    for res in result:
        print(f'{res[0]} : {res[1]}')