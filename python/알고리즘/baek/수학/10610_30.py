n = list(input())


if "0" not in n:
    print(-1)
else:
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    # 30의 배수 -> 각 자리수 합이 3
    if s % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        answer = "".join(n)
        print(answer)