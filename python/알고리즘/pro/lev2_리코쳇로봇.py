# fail. visited 처리를 어떻게 해주지?
def solution(board):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    def go(r,c,cnt):
        # 도착 했으면 그만 해도 되징
        if board[r][c] == "G":
            nonlocal answer
            if cnt < answer:
                answer = cnt
            return
        
        # 상,하,좌,우 순으로 쭉쭉 보내보기
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            moving_flag = False
            while 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != D:
                moving_flag = True
                nr += dr[i]
                nc += dc[i]
            if moving_flag:
                go(nr-dr[i],nc-dc[i],cnt+1)
        # 도착 안했으면 계속 돌려야지
        
    answer = 0
    sr,sc = 0,0
    flag = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                sr,sc = i,j
                flag = 1
                break
        if flag:
            break
    go(sr,sc,0)
    
    
    return answer