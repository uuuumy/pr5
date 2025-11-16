x,y,z=map(int,input().split())
if (x>y and x<z) or (x>z and x<y):
    print(max(x,y,z),x, min(x,y,z))
elif (y>x and y<z) or (y>z and y<x):
    print(max(x,y,z),y, min(x,y,z))
elif (z>y and z<x) or (z>x and z<y):
    print(max(x,y,z),z, min(x,y,z))