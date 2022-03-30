bingo = [list(map(int,input().split())) for _ in range(5)]



t = 0

visited = [[0] * 5 for _ in range(5)]

bin_flag = 0
for i in range(5):
    nums = list(map(int,input().split()))

    for j in range(5):
        t += 1
        num = nums[j]
        flag = 0
        for m in range(5):
            for n in range(5):
                if bingo[m][n] == num:
                    visited[m][n] = 1
                    flag = 1
                    break
            if flag:
                break
        bin = 0
        
        # 가로 체크
        for m in range(5):
            cnt = 0
            for n in range(5):
                if visited[m][n]:
                    cnt += 1
            if cnt == 5:
                bin += 1
        
        # 세로 체크
        for m in range(5):
            cnt = 0
            for n in range(5):
                if visited[n][m]:
                    cnt += 1
            if cnt == 5:
                bin += 1

        if visited[0][4] + visited[1][3] + visited[2][2] + visited[3][1] + visited[4][0] == 5:
            bin += 1
        if visited[0][0] + visited[1][1] + visited[2][2] + visited[3][3] + visited[4][4] == 5:
            bin += 1
        
        if bin >= 3:
            bin_flag = 1
            break
    if bin_flag:
        break
print(t)

                


