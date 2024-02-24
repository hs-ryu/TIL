n,m = map(int,input().split())
books = list(map(int, input().split()))

minus = []
plus = []
for item in books:
    if item < 0:
        minus.append(item)
    elif item > 0:
        plus.append(item)

distance = []
minus.sort()
for i in range(len(minus)//m):
    distance.append(abs(minus[m*i]))
if len(minus) % m > 0:
    distance.append(abs(minus[(len(minus)//m)*m]))

plus.sort(reverse = True)
for i in range(len(plus)//m):
    distance.append(plus[m*i]) 
if len(plus) % m > 0:
    distance.append(plus[(len(plus)//m)*m])    
    
distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)   