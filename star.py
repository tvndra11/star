import turtle
import math

dots = int(input('how many points: '))
distance = int(input('how many far: '))
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
skk = turtle.Turtle()
skk.back(1000/dots/2)
skk.speed(3)
root = math.sqrt(2)
length = 1000/dots
turn = 360/dots


for i in range(dots):
    skk.forward(length)
    skk.left(turn)
if dots % 2 == 1:
    skk.left(turn*(distance/2))
for i in range(dots):
        
        #skk.forward(math.sqrt((length*length)+(length*length)-(2*length*length*math.cos(math.radians(180-turn)))))
        #skk.left(turn*2)
    length1 = length
    length2 = length
    for j in range(distance):
        length2 = math.sqrt((length1*length2)+(length1*length2)-(2*length1*length2*math.cos(math.radians(180-turn))))
    skk.forward(length2)
    skk.left(turn*(distance+1))
    print(length2)
        
        
    
    
     
turtle.done()
