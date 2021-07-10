iron_and_laser = input()
laser = '()'
iron = 0
total = 0
i = 0
while i < len(iron_and_laser) - 1:
    if iron_and_laser[i:i+2] != laser:
        if iron_and_laser[i] == '(':
            iron += 1
            total += 1
        else:
            iron -= 1
    else:
        total += iron
        i += 1
    i += 1
print(total)