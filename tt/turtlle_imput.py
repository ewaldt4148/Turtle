from turtle import *
import random
def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    angle = 180 - (360 / points)

    color(line, fill)
    begin_fill()
    for i in range(points):
        fd(200)
        left(angle)
    end_fill()

bgcolor("black")
speed(50)

def rand_pos():
    return random.randrange(-500, 500, 10)



while True:
    
    draw_star(rand_pos(), rand_pos(), 36, "blue", "maroon")  
    draw_star(rand_pos(), rand_pos(), 36, "pink", "cadet blue")
