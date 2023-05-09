#  Snake Game | Peyton, Xuliang, Luciana
#import
import turtle
import random
import time

#direction
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()  #  y cordinates of turtle
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor() #  x cordinates of turtle
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


win = turtle.Screen()
win.title("Snake Game: Group 3")
win.setup(width=600, height=600)
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cadet blue")
head.penup()
head.goto(0, 100)
head.direction = "stop"

body = []

part = turtle.Turtle()
part.speed(0)
part.shape("square")
part.color("cadet blue")
part.penup()
body.append(part)

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("firebrick")
apple.penup()
apple.goto(0, 0)

#  keyboard binding :DD

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

delay = 0.2 #.1 would be too fast
while True:
    win.update()
    move()
    time.sleep(delay)
    win.listen
    if head.distance(apple) < 15:
    #  make it so the snake can eat the apple
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        apple.goto(x, y)
      # make the snake grow
        # Move the last part to where the head is
    if len(body) > 0:
        last_part = body.pop()
        body.insert(0,last_part)
        x = head.xcor()
        y = head.ycor()
        # move the last part right after the head
        last_part.goto(x, y)
        last_part.showturtle()
