def solution(n):
    def check(r):
        if r >= n:
            nonlocal answer
            answer += 1
        
        for c in range(n):
            if v0[c] or v1[r-c+(n-1)] or v2[r+c]:
                continue
            v0[c] = 1
            v1[r-c+(n-1)] = 1
            v2[r+c] = 1
            # print(v1)
            # print(v2)
            check(r+1)
            v0[c] = 0
            v1[r-c+(n-1)] = 0
            v2[r+c] = 0
    
    v0 = [0] * n
    # 좌상 체크
    v1 = [0] * (2 * n - 1)
    # 우상 체크
    v2 = [0] * (2 * n - 1)
    answer = 0
    check(0)

    
    return answer