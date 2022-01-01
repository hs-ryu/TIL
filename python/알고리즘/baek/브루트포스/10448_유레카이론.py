t = int(input())

T = [0] * 46

for i in range(1,46):
    T[i] = i*(i+1) // 2
# print(T)
for _ in range(t):
    k = int(input())
    result = 0
    flag = 0
    for i in range(1,46):
        if T[i] >= k:
            break
        for j in range(1,46):
            if T[j] >= k - T[i]:
                break
            for l in range(1,46):
                if T[l] > k - T[i] - T[j]:
                    break
                elif T[l] + T[i] + T[j] == k:
                    result = 1
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break
    print(result)


