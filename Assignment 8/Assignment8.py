#Jude Yang
#8/4/21

import turtle
import random
colors = ["Lavender", "AliceBlue", "Beige", "Azure", "AntiqueWhite", "LightCyan", "HoneyDew", "LemonChiffon", "PeachPuff", "LightYellow", "MistyRose",  "LavenderBlush", "Ivory"]
turtle.Screen().bgcolor("black")
t = turtle.Pen()
#Turned the background screen black, and set all the colors that I will use.

for x in range(0, 4):
    t.pensize(5)
    n = random.randint(3, 8)
    print("The number is", n)
    print(" ")
    #Repeats the entire code 4 times so that it'll create 4 graphics after each
    #other.

    if int(n) == 3:
        for x in range(0, 26):
            t.forward(x * 10)
            t.left(120)
            t.color(random.choice(colors))
            #If the randomly generated integer is three, a spiral triangle will be
            #drawn.

    elif int(n) == 4:
        for x in range(0, 20):
            for x in range(0, 4):
                t.forward(100)
                t.right(90)
                t.color(random.choice(colors))
            t.right(20)
            #If the randomly generated integer is four, a rotating square is drawn.

    elif int(n) == 5:
        for x in range(0, 35):
                t.forward(x * 5)
                t.left(72)
                t.color(random.choice(colors))
                #If the randomly generated integer is five, a spiral pentagon is
                #drawn.

    elif int(n) == 6:
        for x in range(0, 18):
            for x in range(0, 6):
                t.forward(100)
                t.right(300)
                t.color(random.choice(colors))
            t.right(20)
            #If the randomly generated integer is six, a rotating hexagon is drawn.

    elif int(n) == 7:
        for x in range(0, 35):
            t.forward(x * 4)
            t.right(51.42)
            t.color(random.choice(colors))
            #If the randomly generated integer is seven, a spiral septagon is drawn.

    elif int(n) == 8:
        for x in range(0, 20):
            for x in range(0, 8):
                t.forward(100)
                t.right(45)
                t.color(random.choice(colors))
            t.right(20)
            #If the randomly generated integer is eight, a rotating octagon is drawn.
    t.reset()
    #The code is reset everytime so that the shapes don't overlap.



            
