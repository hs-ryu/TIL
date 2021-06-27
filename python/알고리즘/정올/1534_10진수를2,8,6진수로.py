decimal,n = map(int,input().split())
form = 'b' if n == 2 else 'o' if n == 8 else 'x'
print(format(decimal,form).upper())