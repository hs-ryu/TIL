def solution(n):
    def hanoi(s, t, e, answer, n):
        # print(answer)
        if n == 1:
            answer.append([s, e])
            return
        hanoi(s, e, t, answer, n - 1)
        answer.append([s, e])
        hanoi(t, s, e, answer, n - 1)
        return answer
    ans = hanoi(1, 2, 3, [], n)
    return ans