n,k = map(int,input().split())
temperatures = list(map(int,input().split()))

totals = [0] * n
totals[0] = temperatures[0]
for i in range(1,n):
    totals[i] = temperatures[i] + totals[i-1]

totals = [0] + totals
results = []
for i in range(k,n+1):
    results.append(totals[i]-totals[i-k])
print(max(results))