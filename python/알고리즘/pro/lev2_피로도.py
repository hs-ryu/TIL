# DFS 재귀
def solution(k, dungeons):
    # x = 남은 피로도
    def search(x,cnt):
        # print(x,cnt)
        nonlocal answer
        if cnt > answer:
            answer = cnt
        for i in range(l):
            if visited[i] == 0 and x >= dungeons[i][0]:
                visited[i] = 1
                search(x-dungeons[i][1], cnt + 1)
                visited[i] = 0
    l = len(dungeons)
    answer = 0
    visited = [0] * l
    search(k, 0)
    return answer