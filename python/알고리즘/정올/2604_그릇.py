plates = input()
result = 10
for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:
        result += 5
    else:
        result += 10
print(result)