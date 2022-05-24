def solution(dirs):
    answer = 0
    arr = [[[] for _ in range(11)] for _ in range(11)]
    r,c = 5,5
    for i in range(len(dirs)):
        nr = r
        nc = c
        if dirs[i] == "U":
            nr -= 1
        elif dirs[i] == "D":
            nr += 1
        elif dirs[i] == "R":
            nc += 1
        else:
            nc -= 1
        if 0 <= nr < 11 and 0 <= nc < 11:
            if dirs[i] == "U":
                if "U" not in arr[r][c] and "D" not in arr[nr][nc]:
                    arr[r][c].append(dirs[i])
                    answer += 1
            elif dirs[i] == "D":
                if "D" not in arr[r][c] and "U" not in arr[nr][nc]:
                    arr[r][c].append(dirs[i])
                    answer += 1 
                    
            elif dirs[i] == "L":
                if "L" not in arr[r][c] and "R" not in arr[nr][nc]:
                    arr[r][c].append(dirs[i])
                    answer += 1
            else:
                if "R" not in arr[r][c] and "L" not in arr[nr][nc]:
                    arr[r][c].append(dirs[i])
                    answer += 1
            r = nr
            c = nc
    return answer