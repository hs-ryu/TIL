n = int(input())



friends = [[] for _ in range(n+1)]
while True:
    n1,n2 = map(int,input().split())
    if n1 == -1 and n2 == -1:
        break
    friends[n1].append(n2)
    friends[n2].append(n1)
print(friends)