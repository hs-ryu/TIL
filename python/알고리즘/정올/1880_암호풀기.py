decoding = input()
incoding = input()

dict = {chr(97+i) : decoding[i] for i in range(26)}
dict[' '] = ' '

result_str = ''
for i in range(len(incoding)):
    if incoding[i].isupper():
        result_str += dict[incoding[i].lower()].upper()
    else:
        result_str += dict[incoding[i]]
print(result_str)