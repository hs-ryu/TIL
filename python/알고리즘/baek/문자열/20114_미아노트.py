n,h,w = map(int,input().split())
afters = [input() for _ in range(h)]

result = ["?"] * n
for i in range(len(afters)):
    st = afters[i]
    for j in range(0,len(st),w):
        k = j // w
        if result[k] != "?":
            continue
        
        m = 0
        while j + m < j + w:
            temp_st = st[j+m]
            if temp_st == "?":
                m += 1
                continue
            else:
                if result[k] == "?":
                    result[k] = temp_st
                break
            
print("".join(result))