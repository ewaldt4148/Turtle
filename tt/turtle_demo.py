#turtle mess aroundS
from turtle import *

colormode(255)
#turtle 1
Turtle1 = Turtle()
Turtle1.shape("turtle")
Turtle1.pen(fillcolor=(100, 0, 0), pencolor=(255, 0, 0), )



Turtle1.onclick(goto)
def stop():
    global running
    running = False
    
def main():
    global running
    clearscreen()
    bgcolor("PapayaWhip")
    tracer(False)
    shape("square")
    f =   0.9
    phi = 18
    s = 5
    c = .5
    # create compound shape
    sh = Shape("compound")
    for i in range(10):
        shapesize(s)
        p =get_shapepoly()
        s *= f
        c *= f
        tilt(-phi)
        sh.addcomponent(p, (c, 0.25, 1-c), "black")
    register_shape("multitri", sh)
    # create dancers
    shapesize(1)
    shape("multitri")
    pu()
    setpos(0, -200)
    dancers = []
    for i in range(180):
        fd(7)
        tilt(-4)
        lt(2)
        update()
        if i % 12 == 0:
            dancers.append(clone())
    home()
    # dance
    running = True
    onkeypress(stop)
    listen()
    cs = 1
    while running:
        ta = -4
        for dancer in dancers:
            dancer.fd(7)
            dancer.lt(2)
            dancer.tilt(ta)
            ta = -4 if ta > 0 else 2
        if cs < 180:
            right(4)
            shapesize(cs)
            cs *= 1.005
        update()
    return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()
