# 금액 범위 설정
# 범위 2로 나눠서 목표값 정하기.
# 목표값으로 출금 몇번 하는지 체크

# 출금횟수가 m보다 크면 low 증가
# 출금횟수가 m보다 작거나 같으면 high 증가


n,m = map(int,input().split())

moneys = []
for i in range(n):
    moneys.append(int(input()))

l = 0
r = 100001
result = 100001

while l <= r:
    mid = (l+r)//2

    money = 0
    num = 0

    # cnt = 출금 횟수
    cnt = 0
    for i in range(len(moneys)):
        if mid < moneys[i]:
            cnt = m+1
            break
        if money >= moneys[i]:
            money -= moneys[i]
        else:
            money = mid - moneys[i]
            num += 1
    else:
        cnt = num
    
    if cnt > m:
        l = mid + 1
    elif cnt <= m:
        result = min(result,mid)
        r = mid -1
print(result)




    