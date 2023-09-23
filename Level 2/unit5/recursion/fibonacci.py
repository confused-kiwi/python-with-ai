import turtle

def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

my_screen = turtle.Screen()
my_screen.title("Python with AI Level 2")

for i in range(1, 15):
    f = fibonacci(i)
    print(f,end=",")
    radius = f
    turtle.circle(radius, 90)

turtle.done()