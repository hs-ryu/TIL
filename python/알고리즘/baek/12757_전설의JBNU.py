
# 시발 못풀겠다
n,m,k = map(int,input().split())

jbnu = dict()
keys = []
for i in range(n):
    key, value = map(int,input().split())
    jbnu[key] = value
    keys.append(key)
keys.sort()
print(jbnu)

for i in range(m):
    data = list(map(int,input().split()))
    if data[0] == 1:
        jbnu[data[1]] = data[2]
        keys.insert(0,data[1])
        keys.sort()

    elif data[0] == 2:
        if data[1] in jbnu:
            jbnu[data[1]] = data[2]
        else:
            idx = keys.index(data[1])
            if idx < len(keys)-1 and idx > 0:
                a = keys[idx-1]
                b = keys[idx+1]
                ma = keys[idx] - a
                mb = b - keys[idx]
                if ma <= k and mb <= k:
                    if ma == mb:
                        continue
                    else:
                        if ma > mb:
                            jbnu[a] = data[2]
                        else:
                            jbnu[b] = data[2]
                elif ma <= k:
                    jbnu[a] = data[2]
                elif mb <= k:
                    jbnu[b] = data[2]
            else:
                if idx < len(keys)-1:
                    a = keys[idx+1]
                    ma = a - keys[idx]
                    if ma <= k:
                        jbnu[a] = data[2]
                if idx > 0:
                    a = keys[idx-1]
                    ma = keys[idx] - a
                    if ma <= k:
                        jbnu[a] = data[2]
    elif data[0] == 3:
        if data[1] in jbnu:
            print(jbnu[data[1]])
        else:
            idx = keys.index(data[1])
            if idx < len(keys)-1 and idx > 0:
                a = keys[idx-1]
                b = keys[idx+1]
                ma = keys[idx] - a
                mb = b - keys[idx]
                if ma <= k and mb <= k:
                    if ma == mb:
                        print("?")
                    else:
                        if ma > mb:
                            print(jbnu[a])
                        else:
                            print(jbnu[b])
                elif ma <= k:
                    print(jbnu[a])
                elif mb <= k:
                    print(jbnu[b])
                else:
                    print(-1)
            else:
                if idx < len(keys)-1:
                    a = keys[idx+1]
                    ma = a - keys[idx]
                    if ma <= k:
                        print(jbnu[a])
                if idx > 0:
                    a = keys[idx-1]
                    ma = keys[idx] - a
                    if ma <= k:
                        print(jbnu[a])
