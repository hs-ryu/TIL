s = input()


ducks = []
for i in range(len(s)):
    if s[i] == "q":
        ducks.append(s[i])
    else:
        for j in range(len(ducks)):
            if s[i] == "u":
                if ducks[j][-1] == "q":
                    ducks[j] += s[i]
            elif s[i] == "a":
                if ducks[j][-1] == "u":
                    ducks[j] += s[i]
            elif s[i] == "c":
                if ducks[j][-1] == "a":
                    ducks[j] += s[i]
            elif s[i] == "k":
                if ducks[j][-1] == "c":
                    ducks[j] += s[i]

result = 0
for i in range(len(ducks)):
    if ducks[i] == "quack":
        result += 1
print(result)