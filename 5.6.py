p=int(input())
v=int(input())
t=int(input())
if p==v==t:
    print(3)
elif p==v or p==t or v==t:
    print(2)
else:
    print(1)