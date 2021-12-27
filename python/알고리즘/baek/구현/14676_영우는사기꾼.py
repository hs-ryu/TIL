# python 시간초과
# pypy 89% 시간초과

from sys import stdin
input = stdin.readline


n,m,k = map(int,input().split())
# 건물 관계
structures = [[] for _ in range(n+1)]
for _ in range(m):
    # y를 짓기 위해선 x가 지어져야함.
    x,y = map(int,input().split())
    structures[y].append(x)
# print(structures)

# 현재 건물 목록
built = dict()
result = "King-God-Emperor"
for _ in range(k):
    action, building = map(int, input().split())
    flag = 0
    # 짓는다
    if action == 1:
        # 선행 건물이 있는 경우 체크 이새끼 때매 시간초과 나는듯
        for i in range(len(structures[building])):
            check = structures[building][i]
            # 선행건물이 안지어졌으면 못짓는다.
            if check not in built:
                result = "Lier!"
                flag = 1
                break
        # break 안걸리면. 선행 건물들 잘 지어진 경우임.
        else:
            if building in built:
                built[building] += 1
            else:
                built[building] = 1
        # 못짓는 경우일때 반복문 그만 돌기
        if flag == 1:
            break
    # 허문다
    else:
        # 지어져있는 빌딩일때
        if building in built:
            if built[building]:
                built[building] -= 1
                if built[building] == 0:
                    built.pop(building)
            # 0이면 없는거임.
            else:
                result = "Lier!"
                break
        # 없을때는 못 허문다.
        else:
            result = "Lier!"
            break
# print(built)
print(result)




from sys import stdin
input = stdin.readline

n,m,k = map(int,input().split())
# 건물 관계
structures = [[] for _ in range(n+1)]
# 지을 수 있는지 체크하는 배열. 각 건물당 몇개의 선행 건물이 필요한 지 count 해서 들어감.
available = [0] * (n+1)
# 건물 올리기
built = [0] * (n+1)

for _ in range(m):
    # y를 짓기 위해선 x가 지어져야함.
    x,y = map(int,input().split())
    structures[x].append(y)
    # 필요 건물 수 1개 증가
    available[y] += 1

result = "King-God-Emperor"
for _ in range(k):
    action, building = map(int, input().split())
    # 건물 올리기
    if action == 1:
        # 필요한 건물이 다 안지어졌는데 지으려고 하면 불가능
        if available[building] > 0:
            result = "Lier!"
            break
        else:
            # 건물 짓는다!
            built[building] += 1
            # 처음 짓는 건물의 경우에만 필요한 건물 개수들을 빼준다.
            # 중복해서 지어진 건물은 뒤에 건물에 영향을 미치지 않는다.
            if built[building] == 1:
                for i in structures[building]:
                    available[i] -= 1
    # 건물 철거
    else:
        # 건물이 없는데 철거하려고 하면 불가능
        if built[building] == 0:
            result = "Lier!"
            break
        
        # 건물 철거시킴
        built[building] -= 1

        # 해당 건물의 개수가 0개라면, 뒤에 지어지는 건물 중 해당 건물이 필요한 건물들에 대해 필요 건물 개수 증가 시켜준다.
        if built[building] == 0:
            for i in structures[building]:
                available[i] += 1
        
print(result)





