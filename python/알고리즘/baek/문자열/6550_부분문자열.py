while True:
    try:
        s,t = input().split()
        check = len(s)
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                check -= 1
            j += 1
            if check == 0:
                break
        print('No' if check else 'Yes')
    except:
        break