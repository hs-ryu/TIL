# 11%에서 틀림.

def search(level, arr):
    # 체크 ㄱ
    if level == n:
        global result

        # 찾는 문자 있는지 체크하는 배열
        visited = [0] * (len(t))
        # 현재 배열의 총 토탈 프라이스.
        total_price = 0
        for i in range(len(arr)):
            price, pos = arr[i]
            total_price += int(price)
            # 찾는 문자열을 하나하나 확인한다.
            for k in range(len(t)):
                # 있으면 visited 체크
                if t[k] in pos:
                    visited[k] = 1
        # visited -> [1,1,0] 뭐 이런식. 없는건 0 그대로 일거임.
        if sum(visited) == len(t):
            result = min(result,total_price)    
        return
    
    arr.append(books[level][:])
    search(level+1, arr)
    arr.pop(-1)
    search(level+1, arr)

t = input()
n = int(input())
books = [input().split() for _ in range(n)]
books.sort(key=lambda x:x[0])


# 가능한 놈들 체크해벌이기.
for i in range(n):
    c,w = books[i]
    c = int(c)
    possible = set()
    for j in range(len(w)):
        if w[j] in t:
            possible.add(w[j])
    books[i][1] = possible

# books를 프린트 해보면 -> [['35000', {'T', 'A'}], ['40000', {'N', 'T', 'A'}], ['43000', {'N', 'T'}], ['47000', {'T', 'A'}]]

# 최솟값 찾아야하니까, result 크게 초기화.
result = 100001 * 50
search(0,[])
if result == 100001 * 50:
    result = -1

print(result)