n = int(input())

string_list = []
for _ in range(n):
    string_list.append(input())
string_list = list(set(string_list))
string_list.sort()
string_list.sort(key=lambda x:len(x))
for i in range(len(string_list)):
    print(string_list[i])