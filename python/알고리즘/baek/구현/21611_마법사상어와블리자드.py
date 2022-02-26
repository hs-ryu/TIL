# 1. 구슬위에 블리자드
# 2. 블리자드 시전된 칸 구슬 파괴
# 3. 구슬 이동
# 4-1. 구슬 폭파
# 4-2. 구슬 이동
# 4번 반복
# 더이상 폭발할 구슬 없으면 구슬 변화
# 5-1. 그룹짓기
# 5-2. 한 그룹의 구슬 갯수, 그룹을 이루는 구슬 번호 뽑아서 1번칸부터 순서대로 넣기. 구슬이 칸의 수보다 많으면 남는 구슬 사라짐.
# 답 : 1 x 폭발한 1번 구슬의 개수 + 2 x 폭발한 2번 구슬의 개수 + 3 x 폭발한 3번 구슬의 개수

# 상하좌우
from pprint import pprint
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 구슬 옮기기 함수. 굳!
def move_marble():
    # 달팽이모양 순서대로 배치해주기 위해 order 배열의 길이 변수 선언
    length_order = n * n - 1

    # 0을 뺀 놈들을 담을 배열
    new_marble_list = []
    # 반복문 돌면서 0인거 빼고 넣어줌
    for i in range(length_order):
        # order는 달팽이 모양으로 순서를 넣어놓은 배열임.
        cr,cc = order[i]
        if area[cr][cc]:
            new_marble_list.append(area[cr][cc])
    
    # 다시 반복문 돌면서, 하나하나 넣어줌. 길이 봐서 남는 부분은 0으로 채워줌.
    for i in range(length_order):
        cr,cc = order[i]
        if i < len(new_marble_list):
            area[cr][cc] = new_marble_list[i]
        else:
            area[cr][cc] = 0


# 구슬 폭발시키기 함수. 베리굳
def explode_marble():
    global flag
    global result
    # 폭발하는 숫자들의 개수 배열
    cnt = [0, 0, 0, 0]

    length_order = n * n - 1
    # 4개 이상인 놈들 찾기. group_list에는 연속한 숫자들의 위치가 들어감.
    group_list = []
    for i in range(length_order-1):
        r, c = order[i]
        nr, nc = order[i+1]
        # 지금 보는 놈이랑 다음에 보는 놈이랑 같은 숫자다? 위치 추가해줌.
        if area[r][c] == area[nr][nc]:
            group_list.append([r, c])
        # 다르다? 그럼 연속된 부분이 끝난거니까 길이 체크해서 폭파시키자.
        else:
            # 그룹의 마지막 부분을 넣어주기 위함.
            if group_list:
                pr,pc = group_list[-1]
                if area[pr][pc] == area[r][c]:
                    group_list.append([r,c])

            # 한 그룹의 길이가 4 이상일때. 폭파 개수 증가시켜주고 그 위치들 0으로 만들어주기.
            if len(group_list) >= 4:
                # print(group_list)
                while group_list:
                    er, ec = group_list.pop(0)
                    cnt[area[er][ec]] += 1
                    area[er][ec] = 0
            # 그룹 초기화
            group_list = []
        
        
        
    # 순서상 제일 마지막 부분은 폭파가 안될수도 있으므로 한번 더 체크해서 없애기 ㄱㄱ
    if len(group_list) >= 4:
        while group_list:
            er, ec = group_list.pop(0)
            area[er][ec] = 0

    # 하나도 폭발 안하면 더이상 폭발할게 없는거니까 그만~
    if cnt[1] == 0 and cnt[2] == 0 and cnt[3] == 0:
        # 얘를 체크해서 더이상 폭파시킬게 없으면 다음 단계 진행.
        flag = 1
    # print(cnt)
    # 답 증가시켜주기
    result += cnt[1] + (cnt[2] * 2) + (cnt[3] * 3)

# 폭파 단계가 끝나고 연속된 애들 그룹지어서 개수랑 숫자로 다시 배열 만드는 작업.
def change_marble():
    length_order = n * n - 1
    # 그룹에 속한 애들 수와 몇번으로 이뤄져있는지 넣어줄 배열
    new_marble_list = []

    # 새로운 구슬 배열 뽑아내기
    # total : 그룹안에 속한 애들 수
    # num : 그룹을 이루고 있는 숫자
    total, num = 1,0
    # pprint(area)
    for i in range(length_order-1):
        r, c = order[i]
        nr, nc = order[i+1]
        # 0을 만나면 어차피 뒤에 더 볼 필요 없으니까 그만
        if not area[r][c]:
            break
        
        # 그룹을 이루고 있는 숫자 할당
        num = area[r][c]
        # 그룹안에 속한 애들 개수 세기
        if area[r][c] == area[nr][nc]:
            total += 1
        # 그룹이 끝나면 추가해주기.
        else:
            new_marble_list.append(total)
            new_marble_list.append(num)
            total = 1
    # print(new_marble_list)
    # 실제 배열에 바꿔주기
    for i in range(length_order):
        r, c = order[i]
        if i < len(new_marble_list):
            area[r][c] = new_marble_list[i]
        else:
            area[r][c] = 0
            

n, m = map(int, input().split())

# 최초 구슬들이 있는 공간
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))


# 달팽이 모양 순서를 위한 배열
order = []
k = n * n
step = 1
y = 0
x = -1
size = n
while True:
    for _ in range(size):
        k -= 1
        x += step
        order.append([y, x])
    size -= 1
    if size < 1:
        break
    for _ in range(size):
        k -= 1
        y += step
        order.append([y, x])
    step = -step
# 마지막껀 센터니까 필요없다잉
order.pop(-1)
# 보기 쉽게 반대로 정렬
order.reverse()


# 시작하자...
result = 0
for _ in range(m):
    # 먼저 블리자드로 방향에 맞게 처리해주기. 굳!
    # 상어의 위치
    sr, sc = n//2, n//2
    d, s = map(int, input().split())
    # k는 한단계씩 없애주기위함.
    k = 0
    while k < s:
        br, bc = sr + dr[d-1], sc + dc[d-1]
        area[br][bc] = 0
        sr, sc = br, bc
        k += 1
    # pprint(area)
    # 구슬 이동
    move_marble()
    # pprint(area)

    # 구슬 폭파. 하나도 폭발 안하면 브레이크
    while True:
        flag = 0
        # 폭발 ㄱㄱ
        # pprint(area)
        explode_marble()
        # pprint(area)
        if flag:
            break
        # 폭발 끝났으면 무브무브
        move_marble()
        # pprint(area)
    # 폭발 끝나면 이제 바꾸기
    # pprint(area)
    change_marble()
    # pprint(area)
print(result)