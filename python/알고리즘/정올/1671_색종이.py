n = int(input())

white_paper = [[0] * 101 for _ in range(101)]
paper = [list(map(int,input().split())) for _ in range(n)]

for i in range(len(paper)):
    for j in range(10):
        for k in range(10):
            x_start = paper[i][0]
            y_start = paper[i][1]
            white_paper[x_start+j][y_start+k] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if white_paper[i][j] == 1:
            if white_paper[i-1][j] == 0:
                cnt += 1
            if white_paper[i+1][j] == 0:
                cnt += 1
            if white_paper[i][j-1] == 0:
                cnt += 1
            if white_paper[i][j+1] == 0:
                cnt += 1
print(cnt)