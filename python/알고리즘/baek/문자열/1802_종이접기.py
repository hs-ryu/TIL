# in-in-out -> 1번, 1번으로 접는 경우
# out-in-in -> 1번, 2번으로 접는 경우
# in-out-out -> 2번, 1번으로 접는 경우
# out-out-in -> 2번, 2번으로 접는 경우
# 가운데를 기준으로 양 쪽이 다르다.

t = int(input())

for _ in range(t):
    st = input()
    # print(st)
    if len(st) == 1:
        print('YES')
    # 최소 단위 : 3개
    # 3개 -> 가운데를 기준으로 양쪽이 다르면 ok
    # 7개 -> 가운데를 기준으로 3개, 3개 잘라서 각각 확인
    # 15개 -> 가운데를 기준으로 7개, 7개 자르고, 각 7개를 3개, 3개로 잘라서 확인.
    else:
        k = [st]
        while len(k[0]) > 3:
            new_k = []
            for i in range(len(k)):
                m = len(k[i]) // 2
                part1 = ""
                part2 = ""
                part1 = k[i][:m]
                part2 = k[i][m+1:]
                new_k.append(part1)
                new_k.append(part2)
            
            k = new_k[:]
                
        # print(k)
        # 접을수 있는지 없는지 체크하는 플래그. 접을수 있다면 0 없으면 1
        flag = 0
        for i in range(len(k)):
            # 가운데를 기준으로 양쪽이 같으면 접을 수 없다.
            if k[i][0] == k[i][2]:
                flag = 1
                break
        if flag:
            print("NO")
        else:
            print("YES")