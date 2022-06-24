cc = "Spacerocket007"

import turtle
import time

t = turtle.Turtle()
t.shape("turtle")
t.pensize(2)
t.turtlesize(1)
t.speed(15)
t.fillcolor("black")
window = turtle.Screen()
window.setup(410, 410)
window.bgcolor("lightgrey")
window.title("Tic Tac Turtle!")
FONTSIZE = 14
FONT =("Arial", FONTSIZE, "normal")


on = True
status = True
blue = 0
green = 0
x = 1 
y = 1
"""
0 = no stamp
1 = blue
2 = green
"""
myList = [[0,0,0],
          [0,0,0],
          [0,0,0]]

def draw():
    t.penup()
    t.forward(150)
    t.setheading(90)
    t.pendown()
    t.forward(150)
    t.setheading(180)
    t.forward(100)
    t.setheading(270)
    t.forward(300)
    t.setheading(180)
    t.forward(100)
    t.setheading(90)
    t.forward(300)
    t.setheading(180)
    t.forward(100)
    t.setheading(270)
    t.forward(100)
    t.setheading(0)
    t.forward(300)
    t.setheading(270)
    t.forward(100)
    t.setheading(180)
    t.forward(300)
    t.setheading(270)
    t.forward(100)
    t.setheading(0)
    t.forward(300)
    t.setheading(90)
    t.forward(300)
    t.setheading(180)
    t.forward(300)
    t.setheading(270)
    t.forward(300)
    t.setheading(0)
    t.penup()
    t.forward(150)
    t.setheading(90)
    t.forward(150)

    
def arrowRight():
    global x
    if x >= 2:
        for i in range(0, 2):
            time.sleep(0.1)
            t.fillcolor("red")
            time.sleep(0.1)
            if green == 1:
                t.fillcolor("green")
            else:
                t.fillcolor("blue")
    else:
        t.setheading(0)
        t.forward(100)
        t.setheading(90)
        x +=1

def arrowLeft():
    global x
    if x <= 0:
        for i in range(0, 2):
            time.sleep(0.1)
            t.fillcolor("red")
            time.sleep(0.1)
            if green == 1:
                t.fillcolor("green")
            else:
                t.fillcolor("blue")
    else:
        t.setheading(180)
        t.forward(100)
        t.setheading(90)
        x -=1
    
def arrowUp():
    global y
    if y >= 2:
        for i in range(0, 2):
            time.sleep(0.1)
            t.fillcolor("red")
            time.sleep(0.1)
            if green == 1:
                t.fillcolor("green")
            else:
                t.fillcolor("blue")
    else:
        t.setheading(90)
        t.forward(100)
        y +=1
    
def arrowDown():
    global y
    if y <= 0:
        for i in range(0, 2):
            time.sleep(0.1)
            t.fillcolor("red")
            time.sleep(0.1)
            if green == 1:
                t.fillcolor("green")
            else:
                t.fillcolor("blue")
    else:
        t.setheading(270)
        t.forward(100)
        t.setheading(90)
        y -=1

def stampCheck():
    global status
    global x
    global y
    x = x
    y = y
    if status:
        blueTranslator()
    else:
        greenTranslator()
               
def stamp():
        t.turtlesize(2)
        t.stamp()                

def blueTranslator():
    global x
    global y
    global myList
    global blue
    global green
    global status
# Horizontal top to bottom:
    if x == 0:
        if y == 2:
            if myList[0][0] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[0][0] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 2:
            if myList[0][1] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[0][1] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 2:
        if y == 2:
            if myList[0][2] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[0][2] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
#-------------    
    if x == 0:
        if y == 1:
            if myList[1][0] == 0:
                stamp()
                #print(x,y, "blue")
                bluewinCheck()
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[1][0] = 1
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 1:
            if myList[1][1] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[1][1] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")                
    if x == 2:
        if y == 1:
            if myList[1][2] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[1][2] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
#-------------    
    if x == 0:
        if y == 0:
            if myList[2][0] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[2][0] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 0:
            if myList[2][1] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[2][1] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 2:
        if y == 0:
            if myList[2][2] == 0:
                stamp()
                #print(x,y, "blue")
                t.turtlesize(1)
                t.fillcolor("green")
                green = 1
                blue = 0
                status = False
                myList[2][2] = 1
                bluewinCheck()
                #print(myList, "blue")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
            
def greenTranslator():
    global x
    global y
    global myList
    global green
    global status
# Horizontal top to bottom:
    if x == 0:
        if y == 2:
            if myList[0][0] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[0][0] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 2:
            if myList[0][1] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[0][1] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 2:
        if y == 2:
            if myList[0][2] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[0][2] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
#-------------    
    if x == 0:
        if y == 1:
            if myList[1][0] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[1][0] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 1:
            if myList[1][1] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[1][1] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 2:
        if y == 1:
            if myList[1][2] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[1][2] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
#-------------    
    if x == 0:
        if y == 0:
            if myList[2][0] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[2][0] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 1:
        if y == 0:
            if myList[2][1] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[2][1] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")
    if x == 2:
        if y == 0:
            if myList[2][2] == 0:
                stamp()
                #print(x,y, "green")
                t.turtlesize(1)
                status = True
                t.fillcolor("blue")
                green = 0
                blue = 1
                myList[2][2] = 2
                greenwinCheck()
                #print(myList , "green")
            else:
                print("No")
                for i in range(0, 2):
                    time.sleep(0.1)
                    t.fillcolor("red")
                    time.sleep(0.1)
                    if green == 1:
                        t.fillcolor("green")
                    else:
                        t.fillcolor("blue")

def greenwinCheck():
    global blue
    global green
    global myList
    global on
# All winning combinations represented here:
# Horizontal top to bottom:
    if myList[0][0] == 2:
        if myList[0][1] == 2:
            if myList[0][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
            
    if myList[1][0] == 2:
        if myList[1][1] == 2:
            if myList[1][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
        
    if myList[2][0] == 2:
        if myList[2][1] == 2:
            if myList[2][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
                    
# Vertical left to right:       
    if myList[0][0] == 2:
        if myList [1][0] == 2:
            if myList[0][0] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
            
    if myList[0][1] == 2:
        if myList[1][1] == 2:
            if myList[2][1] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
            
    if myList[0][2] == 2:
        if myList[1][2] == 2:
            if myList[2][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
                    
# Diagonal bottom left to right:
    if myList[2][0] == 2:
        if myList[1][1] == 2:
            if myList[0][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)

# Diagonal top left to right:
    if myList[0][0] == 2:
        if myList[1][1] == 2:
            if myList[2][2] == 2:
                    print("Green Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Green wins!", align="center", font=FONT)
            
def bluewinCheck():
    global blue
    global green
    global myList
    global on
# all winning combinations represented here:
# Horizontal top to bottom:
    if myList[0][0] == 1:
        if myList[0][1] == 1:
            if myList[0][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)
            
    if myList[1][0] == 1:
        if myList[1][1] == 1:
            if myList[1][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)
        
    if myList[2][0] == 1:
        if myList[2][1] == 1:
            if myList[2][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)

# Vertical left to right:       
    if myList[0][0] == 1:
        if myList [1][0] == 1:
            if myList[2][0] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)

    if myList[0][1] == 1:
        if myList[1][1] == 1:
            if myList[2][1] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)

    if myList[0][2] == 1:
        if myList[1][2] == 1:
            if myList[2][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)

# Diagonal bottom left to right:
    if myList[2][0] == 1:
        if myList[1][1] == 1:
            if myList[0][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)
                    
# Diagonal top left to right:
    if myList[0][0] == 1:
        if myList[1][1] == 1:
            if myList[2][2] == 1:
                    print("Blue Wins")
                    on = False
                    t.ht()
                    t.clearstamps()
                    reset()
                    time.sleep(1)
                    t.write("Blue wins!", align="center", font=FONT)
                                    


def reset():
    global x
    global y
    t.goto(0, 0)
    x = 1
    y = 1

 
window.onkey(stampCheck, "p")    
window.onkey(arrowRight, "Right")
window.onkey(arrowLeft, "Left")
window.onkey(arrowUp, "Up")
window.onkey(arrowDown, "Down")
window.onkey(reset, "r")
window.listen()

draw()
time.sleep(0.5)
t.fillcolor("blue")
    
