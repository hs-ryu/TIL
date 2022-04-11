m = ["a", "i", "y", "e", "o", "u"]
j = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]
st = input()
result = ""
for i in range(len(st)):
    temp = st[i]
    if temp.islower():
        if temp in m:
            idx = m.index(temp)
            idx += 3
            if idx > 5:
                idx -= 6
            result += m[idx]
        else:
            idx = j.index(temp)
            idx += 10
            if idx > 19:
                idx -= 20
            result += j[idx]
    elif temp.isupper():
        n_temp = temp.lower()
        if n_temp in m:
            idx = m.index(n_temp)
            idx += 3
            if idx > 5:
                idx -= 6
            result += m[idx].upper()
        else:
            idx = j.index(n_temp)
            idx += 10
            if idx > 19:
                idx -= 20
            result += j[idx].upper()
    else:
        result += temp
print(result)
