a = int(input())
b = int(input())
c = int(input())

d = a * b * c

result_dict = {i : 0 for i in range(10)}

for num in str(d):
    result_dict[int(num)] += 1

for i in result_dict.values():
    print(i)