def solution(m, n, board):
    def search(r,c):
        if board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
            check[r][c], check[r][c+1], check[r+1][c], check[r+1][c+1] = 1,1,1,1
    
    def removing():
        nonlocal answer
        nonlocal x
        for r in range(m):
            for c in range(n):
                if check[r][c]:
                    x = 1
                    board[r][c] = "0"
                    answer += 1
    
    def moving():
        for c in range(n):
            l = 0
            for r in range(m-1,-1,-1):
                if board[r][c] == "0":
                    l += 1
                else:
                    if l:
                        board[r+l][c] = board[r][c]
                        board[r][c] = "0"
        
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        x = 0
        check = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != "0":
                    search(i,j)
        removing()
        if x == 0:
            break
        moving()
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))