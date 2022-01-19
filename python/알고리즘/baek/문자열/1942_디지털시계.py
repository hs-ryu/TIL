
for _ in range(3):
    st, et = input().split()
    sthour,stminute,stsecond = map(int,st.split(':'))
    ethour,etminute,etsecond = map(int,et.split(':'))

    result = 0
    nowtime = int(str(sthour).zfill(2)+str(stminute).zfill(2)+str(stsecond).zfill(2))
    endtime = int(str(ethour).zfill(2)+str(etminute).zfill(2)+str(etsecond).zfill(2))
    if not nowtime % 3:
        result += 1
    while True:
        # print(nowtime)
        if nowtime == endtime:
            break
        stsecond += 1
        if stsecond >= 60:
            stsecond -= 60
            stminute += 1
        if stminute >= 60:
            stminute -= 60
            sthour += 1
        if sthour >= 24:
            sthour -= 24
        nowtime = int(str(sthour).zfill(2)+str(stminute).zfill(2)+str(stsecond).zfill(2))
        if not nowtime % 3:
            result += 1
    print(result)