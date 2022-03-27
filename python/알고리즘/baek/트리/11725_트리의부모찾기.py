# pypy만 통과...


n = int(input())

tree = [[] for _ in range(n+1)]

# 결과 출력을 위한 배열
result = [0] * (n+1)
result[1] = -1

for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q = []
# 처음 1의 자식들 확인하기
for i in range(len(tree[1])):
    q.append(tree[1][i])
    result[tree[1][i]] = 1


while q:
    temp = q.pop(0)

    for i in range(len(tree[temp])):
        x = tree[temp][i]
        if result[x]:
            continue
        result[x] = temp
        q.append(x)
# print(result)

# print(check)

for i in range(2,n+1):
    print(result[i])