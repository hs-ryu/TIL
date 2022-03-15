from re import L


n, m = map(int,input().split())

folders = dict()
folders["main"] = []
print(folders)
for _ in range(n+m):
    high, low, kind = input().split()
    if high in folders:
        folders[high].append([low,kind])
    else:
        folders[high] = [[low,kind]]
print(folders)

k = int(input())
for _ in range(k):
    fr,to = input().split()
    fr = fr.split('/')
    to = to.split('/')
    for i in range(len(folders[fr[-1]])):
        for j in range(len(folders[to[-1]])):
            if folders[fr[-1]][i][0] == folders[to[-1]][j][0] and folders[fr[-1]][i][1] == folders[to[-1]][j][1]:
                break
        else:
            folders[to[-1]].append([folders[fr[-1]][i][0], folders[fr[-1]][i][1]])
    del folders[fr[-1]]

q = int(input())
for _ in range(q):
    x = list(input().split("/"))
    result_set = {}
    kind, cnt = 0,0
    for i in range(len(folders[x[-1]])):
        a,b = folders[x[-1]][i][0], folders[x-1][i][1]
        if b == "0":
            if a in result_set:
                cnt += 1
            else:
                result_set.add(a)
                cnt += 1
                kind += 1
        else:
            f = [a]
            while f:
                temp_folder = f.pop(0)
                if temp_folder in folders:
                    now_folder = folders[temp_folder]
                    for j in range(len(now_folder)):
                        aa,bb = now_folder[j][0], now_folder[j][1]
                        if bb == "0":
                            if aa in result_set:
                                cnt += 1
                            else:
                                result_set.add(a)
                                cnt += 1
                                kind += 1
                        else:
                            f.append(aa)
    print(kind,cnt)
