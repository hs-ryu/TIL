n,m = map(int,input().split())


s = [input() for _ in range(n)]

set_distance = dict()
min_hd = 50001

result = ""
hd = 0
for i in range(m):
    k_dict = dict()
    for j in range(n):
        temp = s[j]
        if temp[i] in k_dict:
            k_dict[temp[i]] += 1
        else:
            k_dict[temp[i]] = 1
    x = list(k_dict.items())
    x.sort(key=lambda x:x[0])
    x.sort(key=lambda x:-x[1])
    result += x[0][0]
    hd += n - x[0][1]
print(result)
print(hd)