while True:
    try:
        x = input()
        n,m = map(int,x.split())
        sn,sm = str(n),str(m)

        cnt = 0
        for i in range(n,m+1):
            si = str(i)
            
            for j in si:
                if si.count(j) > 1:
                    break
            else:
                cnt += 1
        print(cnt)
    except EOFError:
        break
