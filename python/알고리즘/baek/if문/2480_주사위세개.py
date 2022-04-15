a,b,c = map(int,input().split())

list_num = [a,b,c]
set_num = list(set([a,b,c]))

if len(set_num) == 1:
    result = 10000 + (set_num[0] * 1000)
elif len(set_num) == 2:
    for i in range(len(set_num)):
        if list_num.count(set_num[i]) == 2:
            result = 1000 + (set_num[i] * 100)
            break
else:
    result = max(list_num) * 100

print(result)