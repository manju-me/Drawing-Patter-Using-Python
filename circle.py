import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("red")
turtle.speed(2)
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()