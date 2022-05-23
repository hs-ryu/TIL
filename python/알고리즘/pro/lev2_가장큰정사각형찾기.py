def solution(board):
    answer = 1
    
    r_len = len(board)
    c_len = len(board[0])
    
    min_len = min(r_len, c_len)
    for i in range(r_len):
        for j in range(c_len):
            for k in range(2, min_len):
                if i + k >= r_len or j + k >= c_len:
                    break
                x = i
                num_set = set()
                while x < i+k:
                    print(x)
                    num_set.add(board[x][j:j+k].count(1))
                    x += 1
                print(num_set)

    return answer