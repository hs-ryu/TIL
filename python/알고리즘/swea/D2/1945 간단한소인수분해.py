T = int(input())
for t in range(1, T+1):
    N = int(input())
    k = [2,3,5,7,11]
    result = [0] * len(k)
    for i in range(len(k)):
        while True:
            if N % k[i] != 0:
                break
            N /= k[i]
            result[i] += 1
    result_str_list = list(map(str, result))
    result_str = ' '.join(result_str_list)
    print('#%d %d' % (t, result_str))