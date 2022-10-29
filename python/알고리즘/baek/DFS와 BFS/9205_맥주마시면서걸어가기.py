def search():
    q = [place[0]]
    visited = [place[0]]
    while q:
        cx,cy = q.pop(0)
        if cx == place[-1][0] and cy == place[-1][1]:
            return "happy"
        for nx,ny in place:
            if [nx,ny] not in visited:
                if abs(nx-cx) + abs(ny-cy) <= 1000:
                    q.append([nx, ny])
                    visited.append([nx, ny]) 
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    # home = list(map(int,input().split()))
    place = [list(map(int,input().split())) for _ in range(n+2)]
    # rock = list(map(int,input().split()))
    result = search()
    print(result)







