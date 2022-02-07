n = int(input())

passwords = []

for _ in range(n):
    password = input()
    passwords.append(password)


for i in range(n):
    check = list(passwords[i])
    length = len(check)
    check.reverse()
    check = "".join(check)
    if check in passwords:
        result = check
        break

print(length, result[length//2])