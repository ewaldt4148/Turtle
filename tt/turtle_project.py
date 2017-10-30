from turtle import *
import time
import math

#basic
colormode(255)
#background stuffs 
bgcolor(255, 239, 213)

time.sleep(10)

title("Darts!")
setup(width=1000, height= 1800, startx=0, starty=0)
#Dart Board
def dart_board():
    penup()
    setposition(-100, -300)
    pendown()
    color(0, 0, 0)
    begin_fill()
    speed(15)
    circle(400)
    end_fill()
    color(255, 250, 250)
    

    
def rings(x, y, r, c):
    penup()
    setposition(x, y)
    pendown()
    color(c)
    begin_fill()
    speed(15)
    circle(r)
    end_fill()

def numbers():
    penup()
    setposition(-100, -300)
    pendown()
    for i in range( 1, 10):
        radians()
        write("1")
        color(255, 250, 250)



#Display

dart_board()

rings(-100, -270, 370, [255, 250, 250])
rings(-100, -200, 300, [250, 0, 0])
rings(-100, -170, 270, [0, 0, 0])
rings(-100, 0, 100 , [34, 139, 34])
rings(-100, 50, 50 , [250, 0, 0])

#numbers
penup()
numbers()

#dart
dart = Turtle()
clicks = 0;

def triangle(x, y):
    global clicks
    
    if (clicks < 3):
        dart.penup()
        dart.setposition(x, y)
        dart.pendown()
        dart.color("white")
        dart.begin_fill()
        dart.radians()
        dart.rt(.5)
        dart.fd(50)
        dart.lt(2)
        dart.fd(100)
        dart.lt(2)
        dart.fd(100)
        dart.rt(-2.5)
        dart.end_fill()
        dart.color(190, 190, 190)
        dart.fd(100)
        dart.bk(100)
        dart.lt(-1.5)
        dart.begin_fill()
        dart.fd(15)
        dart.bk(30)
        dart.lt(-1.5)
        dart.fd(100)
        dart.rt(1.5)
        dart.bk(30)
        dart.lt(1.5)
        dart.bk(100)
        dart.end_fill()
        dart.fd(100)
        dart.rt(1)
        dart.begin_fill()
        dart.color(135, 206, 250)
        dart.fd(20)
        dart.rt(1)
        dart.fd(20)
        dart.lt(1)
        dart.end_fill()

        clicks += 1

pen = Pen()
onscreenclick(triangle)
color(135, 206, 250)
write("Press space bar to exit", font=(10))


onkeypress(bye, "space")
listen()
color("red")

    


