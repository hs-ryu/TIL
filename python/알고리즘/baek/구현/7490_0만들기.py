# 한줄 출력하기 ->  end="" 사용하기
# 

T = int(input())

def search(level, st):
    if level == n-1:
        sum_value = eval("".join(st))
        if sum_value == 0:
            for i in range(len(st)):
                if st[i] == "":
                    print(" ", end="")
                elif i == len(st) - 1:
                    print(st[i])
                else:
                    print(st[i], end="")

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


for _ in range(T):
    n = int(input())
    arr = [str(i) for i in range(1,n+1)]
    search(0, arr)
    print("")



# print(eval('4+5+'))