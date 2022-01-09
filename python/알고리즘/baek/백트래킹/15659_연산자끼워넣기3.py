
def search(level,st):
    
    if level == n-1:
        global maxV,minV
        # print(st)
        string = "".join(st)
        calc_value = eval(string)
        if calc_value > maxV:
            maxV = calc_value
        if calc_value < minV:
            minV = calc_value
            
    # 넣었다 뺐다
    else:
        if calc[0]:
            st.insert(level * 2 + 1, '+')
            calc[0] -= 1
            search(level+1, st)
            st.pop(level * 2 + 1)
            calc[0] += 1
        if calc[1]:
            st.insert(level * 2 + 1, '-')
            calc[1] -= 1
            search(level+1, st)
            st.pop(level * 2 + 1)
            calc[1] += 1
        if calc[2]:
            st.insert(level * 2 + 1, '*')
            calc[2] -= 1
            search(level+1, st)
            st.pop(level * 2 + 1)
            calc[2] += 1
        if calc[3]:
            st.insert(level * 2 + 1, '//')
            calc[3] -= 1
            search(level+1, st)
            st.pop(level * 2 + 1)
            calc[3] += 1


n = int(input())
a = list(input().split())
calc = list(map(int,input().split()))

maxV = -1000000001
minV = 1000000001

search(0,a)
print(maxV)
print(minV)