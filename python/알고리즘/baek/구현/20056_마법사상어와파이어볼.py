dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]  


N, M, K = map(int, input().split())  
arr = [[[] for _ in range(N)] for _ in range(N)]  
fireball = []  



for _ in range(M):  
    r, c, m, s, d = map(int, input().split())  
    fireball.append((r-1, c-1, m,s,d))  

for _ in range(K):  
    while fireball:  
        cr, cc, cm, cs, cd = fireball.pop()  
        nr = (cr + cs * dr[cd]) % N  
        nc = (cc + cs * dc[cd]) % N  
        arr[nr][nc].append([cm, cs, cd])  

    for r in range(N):  
        for c in range(N):  
            if len(arr[r][c]) >= 2:  
                val_m, val_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(arr[r][c])  
                while arr[r][c]:  
                    m, s, d = arr[r][c].pop()  
                    val_m += m  
                    val_s += s  
                    if d % 2:  
                        cnt_odd += 1  
                    else:  
                        cnt_even += 1  
                if cnt_odd == cnt or cnt_even == cnt:  
                    nd = [0, 2, 4, 6]  
                else:  
                    nd = [1, 3, 5, 7]  

                if val_m // 5:  
                    for i in nd:  
                        fireball.append([r, c, val_m//5, val_s//cnt, i])  

            elif len(arr[r][c]) == 1:  
                fireball.append([r, c] + arr[r][c].pop())  

print(sum(i[2] for i in fireball))