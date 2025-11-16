p=input('PIN-код: ')
if len(p)==4:
    if p[0]!=p[1] and p[0]!=p[2] and p[0]!=p[3] and p[1]!=p[2] and p[1]!=p[3] and p[2]!=p[3]:
        if int(p)>2050 or int(p)<1900:
            print('OK')
        else:
            print('ERROR)
    else:
        print('ERROR')
else:
    print('ERROR')