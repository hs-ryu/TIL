n = int(input())

for _ in range(n):
    a,b = input().split()
    a_dict = dict()
    b_dict = dict()

    for i in range(len(a)):
        if a[i] in a_dict:
            a_dict[a[i]] += 1
        else:
            a_dict[a[i]] = 1
    
    for i in range(len(b)):
        if b[i] in b_dict:
            b_dict[b[i]] += 1
        else:
            b_dict[b[i]] = 1
    flag = 0
    for key in a_dict.keys():
        if key not in b_dict:
            flag = 1
            break
        else:
            if b_dict[key] != a_dict[key]:
                flag = 1
                break
    if flag == 0:
        print("{0} & {1} are anagrams.".format(a,b))
    else:
        print("{0} & {1} are NOT anagrams.".format(a,b))


