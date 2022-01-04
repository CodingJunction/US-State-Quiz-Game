from turtle import Turtle,Screen
import turtle
import pandas

s=Screen()
guess=[]
tolearn=[]
df=pandas.read_csv("50_states.csv")
states=df.state.tolist()
x=df.x.tolist()
y=df.y.tolist()

img="blank_states_img.gif"

s.title("US State Game")
s.addshape(img)

turtle.shape(img)
while len(guess)<50:
    inpu=s.textinput(f"{len(guess)}/50 correct states",'Enter the name of the state:')
    ip=inpu.title()
    if ip=="Exit":
        s.bye()
        break
    if ip in states and ip not in guess:
        guess.append(ip)
        ind=states.index(ip)
        xcor=x[ind]
        ycor=y[ind]
        t=Turtle()
        t.hideturtle()
        t.penup()
        t.goto(xcor,ycor)
        t.pendown()
        t.write(ip)

for i in states:
    if i not in guess:
        tolearn.append(i)

l=pandas.DataFrame(tolearn)
l.to_csv("states_to_learn.csv")
 
def coor(x,y):
    print(x,y)

turtle.onscreenclick(coor)
turtle.mainloop()
#s.exitonclick()