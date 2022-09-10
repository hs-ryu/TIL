r,c,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(3)]

# 0,0을 기준으로 맞춰주기
r -= 1
c -= 1

result = 0
# 여기 조건은 < 100으로 주면 74% 에서 틀림.
while result <= 100:
    r_cnt = 3
    c_cnt = 3
    if r < len(a) and c < len(a[0]) and a[r][c] == k:
        break
    new_a = []
    # 행이 열보다 큰 경우. 열 계산 및 정렬
    if len(a) >= len(a[0]):
        # 행 하나하나 계산
        for i in range(len(a)):
            temp_r = a[i][:]
            cnt_dict = dict()
            for j in range(len(temp_r)):
                if temp_r[j] == 0:
                    continue
                if temp_r[j] in cnt_dict:
                    cnt_dict[temp_r[j]] += 1
                else:
                    cnt_dict[temp_r[j]] = 1
            # cnt_dict에는 숫자 : 개수 순으로 들어가 있음.
            temp_list = list(cnt_dict.items())
            # 정렬. 개수 오름차순 + 숫자 크기 오름차순
            temp_list.sort(key=lambda x: (x[1],x[0]))
            # 정렬된 리스트로 리스트 새로 생성.
            new_r = []
            for keyValue in temp_list:
                new_r.extend(keyValue)
            if len(new_r) > r_cnt:
                r_cnt = len(new_r)
            new_a.append(new_r)
        for i in range(len(new_a)):
            temp_r = new_a[i][:]
            temp_r_length = len(temp_r)
            while temp_r_length < r_cnt:
                temp_r.append(0)
                temp_r_length += 1
            new_a[i] = temp_r[:]
    # 열이 행 보다 큰경우. 행 계산 및 정렬
    else:
        columes = list(zip(*a))
        for i in range(len(columes)):
            temp_c = columes[i]
            cnt_dict = dict()
            for j in range(len(temp_c)):
                if temp_c[j] == 0:
                    continue
                if temp_c[j] in cnt_dict:
                    cnt_dict[temp_c[j]] += 1
                else:
                    cnt_dict[temp_c[j]] = 1
            temp_list = list(cnt_dict.items())
            temp_list.sort(key=lambda x: (x[1],x[0]))
            new_c = []
            for keyValue in temp_list:
                new_c.extend(keyValue)
            if len(new_c) > c_cnt:
                c_cnt = len(new_c)
            new_a.append(new_c)
        for i in range(len(new_a)):
            temp_c = new_a[i][:]
            temp_c_length = len(temp_c)
            while temp_c_length < c_cnt:
                temp_c.append(0)
                temp_c_length += 1
            new_a[i] = temp_c[:]
        new_a = list(zip(*new_a))
    result += 1
    a = [arr[:] for arr in new_a]
print(-1 if result == 101 else result)

# x = [[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]]
# y = list(zip(*x))
# print(y)
# print(list(zip(*y)))
