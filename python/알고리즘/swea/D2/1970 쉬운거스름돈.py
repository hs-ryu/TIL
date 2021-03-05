

T = int(input())
for t in range(1,T+1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result_list = [0] * len(money_list)
    for i in range(len(money_list)):
        result_list[i] = N // money_list[i]
        N %= money_list[i]
    print('#%d'%t)
    # print(*result_list)
    str_list = list(map(str, result_list))
    answer = ' '.join(str_list)
    print(answer)