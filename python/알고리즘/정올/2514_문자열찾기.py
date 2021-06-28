string = input()
KOI = 0
IOI = 0
for i in range(len(string)-2):
    if string[i] == 'K':
        if string[i+1] == 'O' and string[i+2] == 'I':
            KOI += 1
    if string[i] == 'I':
        if string[i+1] == 'O' and string[i+2] == 'I':
            IOI += 1
print(KOI)
print(IOI)