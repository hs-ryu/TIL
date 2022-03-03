n,k = map(int,input().split())

people = [i for i in range(1,n+1)]

result = []

i = k-1
while people:
    if i >= len(people):
        i = i - len(people)
    else:
        x = people.pop(i)
        result.append(str(x))
        i += k-1
print("<" + ", ".join(result) + ">")