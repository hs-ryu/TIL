from itertools import combinations

def solution(orders, course):
    answer = []
    # 정렬하기
    new_orders = []
    for i in range(len(orders)):
        temp = list(orders[i])
        temp.sort()
        new_orders.append("".join(temp))
    orders = new_orders[:]
    
    # 조합
    x = 0 
    cnt_dict = dict()
    while x < len(course):
        nowCourse = course[x]
        comb_set = set()
        for i in range(len(orders)):
            if len(orders[i]) < nowCourse:
                continue
            comb = combinations(orders[i], nowCourse)
            for temp in comb:
                temp_st = "".join(temp)
                if temp_st in comb_set:
                    if temp_st in cnt_dict:
                        cnt_dict[temp_st] += 1
                    else:
                        cnt_dict[temp_st] = 2
                else:
                    comb_set.add(temp_st)
        x += 1
    # print(cnt_dict)
    
    for i in range(len(course)):
        nowCourse = course[i]
        max_len = 1
        max_string = ''
        nowOrders = []
        for s,k in cnt_dict.items():
            if len(s) == nowCourse:
                nowOrders.append([s,k])
        nowOrders.sort(key=lambda x:x[1], reverse=True)
        if len(nowOrders) == 1:
            if nowOrders[0][1] >= 2:
                answer.append(nowOrders[0][0])
        
        else:
            for j in range(len(nowOrders)-1):
                if nowOrders[j][1] >= 2:
                    if nowOrders[j][0] not in answer:
                        answer.append(nowOrders[j][0])
                    if nowOrders[j][1] == nowOrders[j+1][1]:
                        answer.append(nowOrders[j+1][0])
                    else:
                        break
        
    
    
    answer.sort()
    return answer