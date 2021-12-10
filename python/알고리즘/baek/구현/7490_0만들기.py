from copy import deepcopy
# import ast
def search(level, st):

    # 그만
    if level == n-1:
        # print(st)
        string = "".join(st)
        # print(string)
        # x = re.split('+',string)
        # print(x)
        # sum_value = ast.literal_eval("".join(st))
        sum_value = eval(string)
        if sum_value == 0:
            # print(st)
            result = deepcopy(st)
            answers.append(result)

    # 재귀 ㄱㄱ
    else:
        st.insert(level * 2 + 1, '')
        search(level+1, st)
        st.pop(level*2 + 1)

        st.insert(level*2+1, '+')
        search(level+1, st)
        st.pop(level*2 + 1)

        st.insert(level*2 + 1, '-')
        search(level+1, st)
        st.pop(level*2 + 1)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [str(i) for i in range(1, n+1)]
    answers=[]

    search(0, arr)
    # print(answers)
    if len(answers) > 0:
        for i in range(len(answers)):
            answer = ''
            for j in range(len(answers[i])):
                    if answers[i][j] == "":
                        answer += ' '
                    else:
                        answer += answers[i][j]
            print(answer)
    print("")
