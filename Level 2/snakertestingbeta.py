#  Snake Game | Peyton, Xuliang, Luciana
#  import

import turtle
import random
import time

def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def go_right():
  if head.direction != "left":
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
win.bgcolor("blue")
win.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cadet blue")
head.penup()
head.goto(0, 100)
head.direction = "stop"

high_score = 0

body = [head]


apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("firebrick")
apple.shapesize(0.50, 0.50)
apple.penup()
apple.goto(0, 0)

#  keyboard binding :DD

def hide_body(body):
# change snake and body parts to red after collision
  head.color("red")
  for part in body:
    part.color("red")
  time.sleep(1)
  head.color("blue")
  for part in body:
    part.color("blue")

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

#Pen for Score Board and Score Board itself
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def update_score(score,high_score_local):
  # update score
  pen.clear()
  pen.write("score: {} High Score: {}".format(score, high_score_local), align="center", font=("Courier", 24, "normal"))

def snakegame():
  global high_score
  update_score(0,high_score)
  score = 0
  delay = 0.155
  stop = False
  win.bgcolor("blue")
  body.clear()
  head.goto(0, 100)
  head.color("cadet blue")
  head.direction = "stop"
  for part in body:
    part.color("cadet blue")
  apple.goto(0, 0)
  while not stop:
    win.update()
    move()
    time.sleep(delay)
    win.listen
    if head.distance(apple) < 15:
        print(len(body))
      #  make it so the snake can eat the apple
        x = random.randint(-220, 220)
        y = random.randint(-220, 220)
        apple.goto(x, y)
        # make the snake grow
        part = turtle.Turtle()
        part.speed(0)
        part.shape("square")
        part.color("cadet blue")
        part.penup()
        body.append(part)
        # Increase the score
        score = score+10
        if score > high_score:
          high_score = score
        update_score(score,high_score)
        # Move the last part to where the head is
    if len(body) > 0:
        last_part = body.pop()
        body.insert(0,last_part)
        x = head.xcor()
        y = head.ycor()
        # move the last part right after the head
        last_part.goto(x, y)
        last_part.showturtle()
        
        # Check for body collision
    for index in range(len(body)-1,1,-1):
      if body[index].distance(head) < 20:
        hide_body(body)
        head.color("red")
        for part in body:
          part.color("red")
        score = 0
        update_score(score,high_score)
        stop = True
        break
    # Check for border collision 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
      hide_body(body)
      score = 0
      update_score(score,high_score)
      stop = True
      break


while True:
  snakegame()


