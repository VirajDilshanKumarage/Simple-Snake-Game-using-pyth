import turtle
import time
import random


delay=0.1
#setup
wn=turtle.Screen()
wn.title("snake")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.speed()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
#sneke food
fhead=turtle.Turtle()
fhead.speed()
fhead.shape("circle")
fhead.color("red")
fhead.penup()
fhead.goto(0,100)

segments =[]
 #ke
# fuynction
def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"




def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x= head.xcor()
        head.setx(x -20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
#keyword
wn.listen()
wn.onkeypress(go_up,"w")

wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_down,"s")




#main game loop
while True:
    wn.update()

    if head.distance(fhead)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        fhead.goto(x,y)

        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

    #move
    for i in range(len(segments)-1, 0, -1):
         x=segments[i-1].xcor()
         y=segments[i-1].ycor()
         segments[i].goto(x,y)


    #move segment end
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)



    move()
    time.sleep(delay)

wn.mainloop()

