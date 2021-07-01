T = int(input())
for t in range(T):
    n = int(input())
    clothes = [input().split() for _ in range(n)]
    cloth_dic = {}
    for cloth in clothes:
        if cloth[1] in cloth_dic:
            cloth_dic[cloth[1]] += 1
        else:
            cloth_dic[cloth[1]] = 2
    result = 1
    for kind in cloth_dic.values():
        result *= kind
    result -= 1
    print(result)