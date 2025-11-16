g=int(input())
if g%4!=0:
    print('365')
else:
    if g%100!=0:
        print('366')
    else:
        if g%400!=0:
            print('365')
        else:
            print('366')