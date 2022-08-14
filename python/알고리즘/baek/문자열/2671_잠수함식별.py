def check():
    i = 0
    s = len(st)

    while i < s:
        if st[i] == "0":
            if i + 1 >= s:
                return
            if st[i+1] != "1":
                return
            i += 2
        else:
            if i + 3 >= s:
                return
            if st[i+1] != "0" and st[i+2] == "0":
                return
            while i < s and st[i] == "0":
                i += 1
            if i >= s:
                return
            i += 1
            while i < s and st[i] == "1":
                if i + 2 < s and st[i+1] == "0" and st[i+2] == "0":
                    break
                i += 1
    flag = 1

st = input()
flag = 0
check()
if flag:
    print("SUBMARINE")
else:
    print("NOISE")