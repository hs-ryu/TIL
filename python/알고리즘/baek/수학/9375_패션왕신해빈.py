t = int(input())
for _ in range(t):
    n = int(input())
    cloths = dict()
    result = 1
    for i in range(n):
        detail, kind = input().split()
        if kind in cloths:
            cloths[kind].add(detail)
        else:
            cloths[kind] = set([detail])
    
    for key in cloths.keys():
        result *= (len(cloths[key]) + 1)
    print(result-1)

