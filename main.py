import random
import turtle
from turtle import Turtle,Screen
from random import randint

turtle.colormode(255)
tim=Turtle()
tim.shape("arrow")
tim.width(15)
tim.speed(10)


def shape(sides):
    angles=[0,90,180,270]
    for _ in range(sides):
        tim.pencolor(randint(0, 255),
                     randint(0, 255),
                     randint(0, 255))
        tim.forward(30)
        tim.setheading(random.choice(angles))


shape(200)

screen=Screen()
screen.exitonclick()
