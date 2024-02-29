import turtle
import time

# Fa schifo sto cuore

canvas = turtle.Screen()
canvas.bgcolor('black')
pen = turtle.Turtle()
pen.speed(0)
pen.color('red', 'blue')
pen.penup()

def draw_heart(x, y, size):
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.left(45)
    pen.forward(100 * size)
    pen.circle(50 * size, 180)
    pen.right(90)
    pen.circle(50 * size, 180)
    pen.forward(100 * size)
    pen.end_fill()
    pen.setheading(0)
    pen.penup

def heartbeat():
    for i in range(6):
        pen.shapesize(1 + i/10)
        draw_heart(0, 0, 1 + i/10)
        time.sleep(0.1)
        pen.clear

while True: 
    heartbeat()

pen.hideTurtle()

canvas.exitonclick()