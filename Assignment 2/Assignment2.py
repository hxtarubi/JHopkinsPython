import turtle
t=turtle.Pen()
t.pensize(5)
t.color("BurlyWood")

t.forward(50)
t.up()
t.right(90)
t.forward(10)
t.down()
t.circle(50)
#Created left rim of the glasses

t.left(90)
t.up()
t.forward(100)
t.left(45)
t.down()
t.forward(150)
t.right(90)
t.forward(25)
#Created left temple of the glasses

t.up()
t.backward(25)
t.left(90)
t.backward(150)
t.right(45)
t.backward(150)
t.right(270)
t.down()
t.circle(50)
t.left(180)
#Created right rim of the glasses

t.right(90)
t.up()
t.forward(100)
t.right(135)
t.down()
t.forward(150)
t.right(90)
t.forward(25)
#Created right temple of the glasses
