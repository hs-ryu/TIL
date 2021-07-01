decoding = input()
incoding = input()

dic = {chr(97+i) : decoding[i] for i in range(26)}
dic[' '] = ' '

result_str = ''
for i in range(len(incoding)):
    if incoding[i].isupper():
        result_str += dic[incoding[i].lower()].upper()
    else:
        result_str += dic[incoding[i]]
print(result_str)