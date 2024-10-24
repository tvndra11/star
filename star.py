import turtle
import math

dots = int(input('how many points: '))
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
skk = turtle.Turtle()
skk.back(1000/dots/2)
skk.speed(0)
length = 1000/dots
turn = 360/dots

for i in range(dots):
    skk.forward(length)
    skk.left(turn)
if dots % 2 == 1:
    
    for i in range(dots):
        skk.left(turn/2)
        skk.forward(math.sqrt((length*length)+(length*length)-(2*length*length*math.cos(math.radians(180-turn)))))
        skk.left(turn*1.5)
    
    
     
turtle.done()
