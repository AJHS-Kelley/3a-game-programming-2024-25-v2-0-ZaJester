# import object from module turtle
from turtle import*

state= {'turn'}
def spin():
    clear()
    angle = state['turn']/5

    right(angle)

    forward(100)

    dot(120,'crimson')

    back(100)

    "second dot"
    right(120)
    forward(100)
    dot(120,'thistle')
    back(100)
    
    "third dot"
    right(120)
    forward(100)
    dot(120,'sienna')
    back(100)

    right(120)

    update()

def animate():
    if state['turn']>0:
        state['turn']-=1

    spin()
    ontimer(animate, 40)

def flick():
    state['turn']+=60

setup(600, 400, 370, 0)
bgcolor("white")

tracer(False)

width(10)
color("orchid")

onkey(flick,'space')

listen()
animate()
done()
     