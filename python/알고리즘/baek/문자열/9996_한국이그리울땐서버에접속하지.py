n = int(input())
check = input()
check_list = check.split("*")
# 오른쪽부터 세고, 왼쪽에서도 센다. 근데, 중복돼서 카운트되면 안되네...
for _ in range(n):
    temp = input()
    visited = [0] * len(temp)
    flag = True
    for i in range(len(check_list[0])):
        if check_list[0][i] != temp[i]:
            flag = False
            break
    else:
        visited[:len(check_list[0])] = [1]
    
    for i in range(len(check_list[1])-1, -1, -1):
        if check_list[1][i] != temp[i-len(check_list[1])] or visited[i-len(check_list[1])] == 1:
            flag = False
            break
    if not flag:
        print("NE")
    else: 
        print("DA")