n = int(input())
persons = [list(map(int,input().split())) for _ in range(n)]

max_value = 0

persons.sort(key=lambda x:(x[0]))
# print(persons)

result = 0 

for i in range(n):
    x = 0 

    # 이익이 안남으면 안파는거니까, 배송비 비교해서, 이익 남으면 x 값 추가해주기.
    # 예제 2번
    # 13원 -> 1번한텐 팔아도 되지만, 2,3번 팔아도 배송비 때매 이익 안남음 = 8원 이득
    # 22원 -> 2번한테 팔아도 되지만, 1은 안살거고, 3번은 배송비 때매 안됨. = 7원 이득
    # 35원 -> 3번한테 팔아도 되지만, 1,2번은 안살거임 = 5원 이득
    # 13원이 최대
    for j in range(i,n):
        if persons[i][0] - persons[j][1] > 0:
            x += persons[i][0] - persons[j][1]
    # 파는 금액 결정.
    if x > max_value:
        max_value = x
        result = persons[i][0]
    i += 1
print(result)
