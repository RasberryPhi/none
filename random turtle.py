import random as random
import turtle


wn = turtle.Screen()
wn.title("Maze")
wn.setup(0.7, 0.85)
# set the position by using setpos()
turtle.up()
turtle.setpos(-300,300)
turtle.down()
  
# forward turtle by 100
for __init__ in range(4):
    turtle.forward(600)
    turtle.right(90)

for k in range(1,24):
    turtle.up()
    turtle.setpos(-300,-300+25*k)
    turtle.down()
    turtle.forward(600)
turtle.right(90)
for m in range(1,24):
    turtle.up()
    turtle.setpos(300-m*25,300)
    turtle.down()
    turtle.forward(600)
    
    
def maze():
    turtle.color("white")
    turtle.up()
    turtle.setpos(-300,300)
    turtle.down()
    turtle.forward(25)
    turtle.up()
    turtle.setpos(275,-300)
    turtle.down()
    turtle.forward(25)
    

turtle.up()
turtle.setpos(0,0)
turtle.down()
L=[]
for __init__ in range(400):
    b=round(random.random())
    L.append(b)
turtle.color("white")
print(L)

for i in range(400):
    if L[i]==0:
        turtle.right(90)
        turtle.forward(25)
    if L[i]==1:
        turtle.left(90)
        turtle.forward(25)
        





    

    
    

