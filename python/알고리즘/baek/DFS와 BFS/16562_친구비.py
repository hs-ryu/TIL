
def BFS(people):
    q = [people]
    while q:
        temp = q.pop(0)
        for i in range(len(relation[temp])):
            if not friended[relation[temp][i]]:
                q.append(relation[temp][i])
                friended[relation[temp][i]] = 1

n,m,k = map(int,input().split())
# 돈계산 쉽게 하려고 만든 딕셔너리 {1번:20원}
money_list = dict()
# 입력받은 금액
price = list(map(int,input().split()))
a = []
for i in range(n):
    # 최소값을 출력해야하니까 입력받은 금액을 낮은 금액부터 보기 위해 [사람,금액] 순으로 배열 다시 만들어줌
    a.append([i+1,price[i]])
    # 딕셔너리에도 추가해주기
    money_list[i+1] = price[i]
# 정렬. 금액 기준 오름차순
a.sort(key=lambda x:x[1])

# 친구 관계
relation = [[] for _ in range(n+1)]
for i in range(m):
    v,w = map(int,input().split())
    relation[v].append(w)
    relation[w].append(v)

# print(relation)
# 현재 친구인지 아닌지 체크하는 배열
friended = [0 for _ in range(n+1)]
total_money = 0

# 돈 초과하면 더 탐색할 필요 없으니 flag 만들어줌
flag = 0
for i in range(n):
    # 현재 친구가 아닌 경우만 확인. 정렬 해놧으니까 순서대로 보면됨
    if not friended[a[i][0]]:
        # 친구 체크 해줌.
        friended[a[i][0]] = 1
        # 돈 추가
        total_money += money_list[a[i][0]]
        # print(a[i][0])
        # print(friended)
        # BFS 돌면서 그놈의 친구(친구의 친구의 친구의 친구... 까지 다)관계 싹다 체크
        BFS(a[i][0])
    # 낸 돈이 k보다 크면 그만
    if total_money > k:
        flag = 1
        break

print(total_money if not flag else "Oh no")