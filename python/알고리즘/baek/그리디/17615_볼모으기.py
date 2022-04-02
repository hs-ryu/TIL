n = int(input())

st = input()
# 각 색깔 갯수 세기.
R_cnt = st.count("R")
B_cnt = st.count("B")

# print(R_cnt)

# 최대 옮겨야 하는 횟수 : 더 적은 갯수의 볼의 수
result = min(R_cnt, B_cnt)

# 왼쪽으로 옮겨보기 
# 왼쪽부터 연속된 색깔의 개수 세어서 그만큼 해당색의 전체 갯수에서 빼기.
left_color = st[0]
cnt = 0
i = 0
while i < n:
    if st[i] == left_color:
        cnt += 1
    else:
        break
    i += 1
result = min(result, st.count(left_color) - cnt)


# 오른쪽으로 옮겨보기
# 오른쪽부터 연속된 색깔의 개수 세서 그만큼 해당색의 전체 갯수에서 빼기.
right_color = st[-1]
cnt = 0
i = n-1
while i >= 0:
    if st[i] == right_color:
        cnt += 1
    else:
        break
    i -= 1
result = min(result, st.count(right_color) - cnt)

print(result)