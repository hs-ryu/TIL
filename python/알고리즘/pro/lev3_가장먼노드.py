# 테스트 7,8,9 시간초과.

def solution(n, edge):
    def BFS():
        visited = [0] * (n+1)
        visited[1] = 1
        q = [1]
        while q:
            temp = q.pop(0)
            cnt = visited[temp] + 1
            for e in edge:
                if e[0] == temp and visited[e[1]] == 0:
                    q.append(e[1])
                    visited[e[1]] = cnt
                elif e[1] == temp and visited[e[0]] == 0:
                    q.append(e[0])
                    visited[e[0]] = cnt
        max_v = max(visited)
        return visited.count(max_v)
    
    edge.sort(key=lambda x:x[0])
    answer = BFS()
    return answer