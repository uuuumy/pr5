h=int(input())
if h%10==1 and h!=11:
    print(h,'попугай')
if (h%10==2 and h!=12) or (h%10==3 and h!=13) or (h%10==4 and h!=14):
    print(h,'попугая')
if h%10==5 or h%10==6 or h%10==7 or h%10==8 or h%10==9 or h%10==0:
    print(h, 'попугаев')

