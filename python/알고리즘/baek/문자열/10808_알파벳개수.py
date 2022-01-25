st = input()
dic = {chr(i) : 0 for i in range(97, 123)}
for s in st:
    dic[s] += 1
print(*dic.values())