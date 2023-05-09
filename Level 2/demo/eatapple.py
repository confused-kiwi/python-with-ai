import turtle
import random
import time

#  make the apple & screen

win = turtle.Screen()
win.setup(width=600, height=600)

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("green")
apple.penup()
apple.goto(0, 0)

win.listen()

if head.distance(apple) <15:
    #  make it so the snake can eat the apple
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)

turtle.done()
