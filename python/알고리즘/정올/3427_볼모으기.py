n = int(input())
balls = list(input())

check = 0
cnt = 0
min_cnt = 987654321
if balls[0] == 'R':
    for i in range(1,n):
        if balls[i] == 'R':
            if check == 1:
                cnt += 1
        if balls[i] == 'B':
            check = 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

    for i in range(n):
        if balls[i] == 'B':
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

if balls[0] == 'B':
    for i in range(1,n):
        if balls[i] == 'B':
            if check == 1:
                cnt += 1
        if balls[i] == 'R':
            check = 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

    for i in range(n):
        if balls[i] == 'R':
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

if balls[n-1] == 'R':
    for i in range(n-2,-1,-1):
        if balls[i] == 'R':
            if check == 1:
                cnt += 1
        if balls[i] == 'B':
            check = 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

    for i in range(n-2,-1,-1):
        if balls[i] == 'B':
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

if balls[n-1] == 'B':
    for i in range(n-2,-1,-1):
        if balls[i] == 'B':
            if check == 1:
                cnt += 1
        if balls[i] == 'R':
            check = 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

    for i in range(n-2,-1,-1):
        if balls[i] == 'R':
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    check = 0
    cnt = 0

print(min_cnt)