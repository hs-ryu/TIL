h = int(input())
m = int(input())
l = int(input())
coke = int(input())
sidar = int(input())

hamberger = [h,m,l]
beverage = [coke,sidar]

result = min(hamberger) + min(beverage) - 50
print(result)