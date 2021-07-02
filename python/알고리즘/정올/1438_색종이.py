n = int(input())
white_paper = [[0] * 101 for _ in range(101)]
paper = [list(map(int,input().split())) for _ in range(n)]

for i in range(len(paper)):
    for j in range(10):
        x_start = paper[i][0]
        y_start = paper[i][1]
        white_paper[x_start+j][y_start:y_start+10] = [1] * 10

cnt = 0
for i in range(101):
    cnt += white_paper[i].count(1)
print(cnt)