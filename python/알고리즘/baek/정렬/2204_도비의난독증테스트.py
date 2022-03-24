n = int(input())

while n:
    st = []
    for i in range(n):
        st.append(input())
    st.sort(key=lambda x:x.upper())
    print(st[0])
    n = int(input())