n = int(input())

dic = dict()
for _ in range(n):
    i = input()
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
answer = list(dic.items())
answer.sort(key=lambda x:(-x[1],x[0]))
print(answer[0][0])