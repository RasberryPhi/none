#sierpinski
from turtle import *

def s(a,ai):
    if a >=ai:
        for i in range(3):
            p.forward(a)
            p.left(120)
            s(a/2,ai)
            
wn=Screen()
wn.bgcolor("green")
wn.setup(width=640,height=480)
wn.title("Sierpinski-Dreieck")
p=Turtle()
p.pencolor("black")
p.pensize(2)
m=4
g=400
ai=g/2**m
p.penup()
p.setpos(-250,-180)
p.pendown()
wn.tracer(True)
s(g,ai)
wn.update()
print("Stufe:",m,",Anzahl der Dreiecke:",(3**(m+1)-1)/2)
wn.mainloop()
