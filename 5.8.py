N=int(input())
gal=N//(17*29)
kn=N-(gal*17*29)
cikl=kn//29
kn1=N-(gal*17*29)-(kn//29)*29
if gal==0 and cikl!=0:
    print(cikl,'сиклей', kn1,'кнатов')
elif cikl==0 and gal!=0 and kn1!=0:
    print(gal,'галлеонов', kn1,'кнатов')
elif kn1==0 and gal!=0 and cikl!=0:
    print(gal,'галлеонов',cikl, 'сиклей')
elif gal==0 and cikl==0 and kn1!=0:
    print(kn1, 'кнатов')
elif cikl==0 and kn1==0 and gal!=0:
    print(gal, 'галлеонов')
elif gal==0 and kn1==0 and cikl!=0:
    print(cikl, 'сиклей')
else:
    print(gal, 'галлеонов', cikl, 'сиклей',kn1,'кнатов')