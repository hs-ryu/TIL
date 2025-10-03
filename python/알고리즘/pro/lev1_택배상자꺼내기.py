def solution(n, w, num):
    answer = 0
    
    arr = [[0] * w for i in range(n // w + 1)]
    
    x = 1
    r = -1
    c = -1
    done = False
    for i in range(n // w + 1):
        if i % 2:
            for j in range(w-1,-1,-1):
                arr[i][j] = x
                if x == num:
                    c = j
                    r = i
                x += 1
                if x > n:
                    done = True
                    break
        else:
            for j in range(w):
                arr[i][j] = x
                if x == num:
                    c = j
                    r = i
                x += 1
                if x > n:
                    done = True
                    break
                    
        if (done):
            break
    
    
    # print(arr)
    # print(r,c)
    
    for i in range(r, n // w + 1):
        if (arr[i][c] != 0):
            answer += 1
    
    return answer