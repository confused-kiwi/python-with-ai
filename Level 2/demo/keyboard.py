#  Snake Game
# Luciana

import turtle
import random
import time

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
win.title("Snake Game: Luciana")
win.setup(width=600, height=600)
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0, 100)
head.direction = "stop"

#  keyboard binding :DD

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

delay = 0.1
while True:
    win.update()
    move()
    time.sleep(delay)
