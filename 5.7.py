N,K,M= map(int, input().split())
if K>N:
    print('вы ввели станцию Артема>общего количества станций')
if M>N:
    print('cтанция назначения>общего количества станций')
if K==M:
    print(0)
else:
    if K<M:
        f=M-K
    else:
        f=N-K+M
    if K>M:
        b=K-M
    else:
        b=K+N-M
    print(min(f,b)-1)