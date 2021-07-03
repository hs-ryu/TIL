card_shape = []
card_num = []
for _ in range(5):
    card = input().split()
    card_shape.append(card[0])
    card_num.append(int(card[1]))
card_num.sort()
num_set = list(set(card_num))
result = 0
if len(set(card_shape)) == 1 and card_num[0]+1 == card_num[1] and card_num[1]+1 == card_num[2] and card_num[2]+1 == card_num[3] and card_num[3]+1 == card_num[4]:
    result = card_num[4] + 900
elif len(num_set) == 2:
    if card_num.count(num_set[0]) == 4:
        result = num_set[0] + 800
    elif card_num.count(num_set[1]) == 4:
        result = num_set[1] + 800
    # 3번조건
    else:
        if card_num.count(num_set[0]) == 3:
            result = num_set[0] * 10 + num_set[1] + 700
        elif card_num.count(num_set[1]) == 3:
            result = num_set[1] * 10 + num_set[0] + 700
# 4번 조건
elif len(set(card_shape)) == 1:
    result = card_num[4] + 600
# 5번 조건
elif card_num[0]+1 == card_num[1] and card_num[1]+1 == card_num[2] and card_num[2]+1 == card_num[3] and card_num[3]+1 == card_num[4]:
    result = card_num[4] + 500
# 6번 조건 고쳐야할까
elif len(num_set) == 3:
    if card_num.count(num_set[0]) == 3:
        result = num_set[0] + 400
    elif card_num.count(num_set[1]) == 3:
        result = num_set[1] + 400
    elif card_num.count(num_set[2]) == 3:
        result = num_set[2] + 400
# 7번 조건
    else:
        if card_num.count(num_set[0]) == 2 and card_num.count(num_set[1]) == 2:
            if num_set[0] > num_set[1]:
                result = num_set[0] * 10 + num_set[1] + 300
            elif num_set[1] > num_set[0]:
                result = num_set[1] * 10 + num_set[0] + 300
        elif card_num.count(num_set[0]) == 2 and card_num.count(num_set[2]) == 2:
            if num_set[0] > num_set[2]:
                result = num_set[0] * 10 + num_set[2] + 300
            elif num_set[2] > num_set[0]:
                result = num_set[2] * 10 + num_set[0] + 300
        elif card_num.count(num_set[1]) == 2 and card_num.count(num_set[2]) == 2:
            if num_set[1] > num_set[2]:
                result = num_set[1] * 10 + num_set[2] + 300
            elif num_set[2] > num_set[1]:
                result = num_set[2] * 10 + num_set[1] + 300
# 8번 조건
elif len(num_set) == 4:
    if card_num.count(num_set[0]) == 2:
        result = num_set[0] + 200
    elif card_num.count(num_set[1]) == 2:
        result = num_set[1] + 200
    elif card_num.count(num_set[2]) == 2:
        result = num_set[2] + 200
    elif card_num.count(num_set[3]) == 2:
        result = num_set[3] + 200
# 9번 조건
if result == 0:
    result = card_num[4] + 100
print(result)