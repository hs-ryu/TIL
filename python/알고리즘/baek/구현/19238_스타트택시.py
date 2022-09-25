dr = [-1,1,0,0]
dc = [0,0,-1,1]

def action(sr,sc):
    visitied = [[0] * n for _ in range(n)]
    visitied[sr][sc] = 1
    q = [[sr,sc]]
    global oil

    flag = True
    start_points = 0,0
    
    while q:
        cr,cc = q.pop()
        for i in range(4):
            nr,nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visitied[nr][nc] == 0 and jido[nr][nc] != "1":
                if flag:
                    visitied[nr][nc] = visitied[cr][cc] + 1
                    if jido[nr][nc] in customer_end.keys():
                        flag = False
                    q.append([nr,nc])



n,m,oil = map(int,input().split())

jido = [input().split() for _ in range(n)]
# print(jido)

sr,sc = map(int,input().split())

customer = []
for i in range(m):
    fr,fc,lr,lc = map(int,input().split())
    customer.append([fr-1,fc-1,lr-1,lc-1])

customer_end = dict()
for i in range(len(customer)):
    fr,fc,lr,lc = customer[i]
    jido[fr][fc] = "s" + str(i+1)
    jido[lr][lc] = "e" + str(i+1)
    customer_end["s" + str(i+1)] = [lr,lc]


