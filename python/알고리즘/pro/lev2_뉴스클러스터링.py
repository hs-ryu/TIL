def solution(str1, str2):
    st1 = dict()
    st2 = dict()
    alpha = set([chr(i) for i in range(97,123)])
    st_set = set()
    
    for i in range(len(str1)-1):
        temp1 = str1[i].lower()
        temp2 = str1[i+1].lower()
        if temp1 in alpha and temp2 in alpha:
            x = temp1 + temp2
            st_set.add(x)
            if x in st1:
                st1[x] += 1
            else:
                st1[x] = 1

    for i in range(len(str2)-1):
        temp1 = str2[i].lower()
        temp2 = str2[i+1].lower()
        if temp1 in alpha and temp2 in alpha:
            x = temp1 + temp2
            st_set.add(x)
            if x in st2:
                st2[x] += 1
            else:
                st2[x] = 1
    
    minv = 0
    maxv = 0 
    
    for s in st_set:
        if s in st1 and s in st2:
            minv += min(st1[s], st2[s])
            maxv += max(st1[s], st2[s])
        else:
            if s in st1:
                maxv += st1[s]
            elif s in st2:
                maxv += st2[s]

    if minv == 0 and maxv == 0:
        result = float(1)
    else:
        result = minv / maxv
    result = result * 65536
    answer = str(result).split(".")
    answer = int(answer[0])
    return answer