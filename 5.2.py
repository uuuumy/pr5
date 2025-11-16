import turtle as t
x,y=map(int,input('Координаты центра окружности: ').split())
r=int(input('Радиус: '))
a,b=map(int,input('Координаты точки: ').split())
d=((a-x)**2+(b-y)**2)**0.5
q=0
if d<r:
    q='точка внутри окружности'
elif d>r:
    q='точка вне окружности'
else:
    q='точка на окружности'
t.penup()
t.goto(x,y-r)
t.pendown()
t.circle(r)
t.penup()
t.goto(a,b)
t.dot(5)
t.hideturtle()
t.write(q)
t.done()

