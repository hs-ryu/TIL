ml,mr,tl,tr = input().split()

if ml != mr and tl != tr:
    print("?")
elif ml == mr and tl != tr:
    if ml == "S" and (tl == "R" or tr == "R"):
        print("TK")
    elif ml == "P" and (tl == "S" or tr == "S"):
        print("TK")
    elif ml == "R" and (tl == "P" or tr == "P"):
        print("TK")
    else:
        print("?")
elif ml != mr and tl == tr:
    if tl == "S" and (ml == "R" or mr == "R"):
        print("TK")
    elif tl == "P" and (ml == "S" or mr == "S"):
        print("TK")
    elif tl == "R" and (ml == "P" or mr == "P"):
        print("TK")
    else:
        print("?")
else:
    print("?")