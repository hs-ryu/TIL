n = int(input())
info = [[] for _ in range(11)]

result = 0
for _ in range(n):
    cow, location = map(int,input().split())
    if not info[cow]:
        info[cow].append(location)
    else:
        if location == 0:
            if info[cow][0] == 1:
                info[cow][0] = 0
                result += 1
        else:
            if info[cow][0] == 0:
                info[cow][0] = 1
                result += 1
print(result)