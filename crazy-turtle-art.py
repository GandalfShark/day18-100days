"""
very silly program that creates computer generated 'art'.
code inspired by day 18 - 100 days of code by Dr.Angela Yu
"""

import random
import turtle as t
tom = t.Turtle()
screen = t.Screen()
screen.bgcolor('black')

# change the color to rgb mode
t.colormode(255)

# setting up tom the turtle
tom.shape('turtle')
tom.color('blue')
tom.pu()
tom.goto(-100, 100)
tom.pd()
tom.speed(40)
tom.pensize(4)

# some sides for shapes for tom to draw
list_of_sides = [3, 4, 6, 8, 10, 12]


def random_color():
    # Randint stops at the last value. We don't need 256 like you would think
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = (r, g, b)
    return color_code

def shape_time():
    for number in list_of_sides:
        moves = 0
        sides = number
        while sides != moves:
            angle = 360/sides
            tom.forward(100)
            tom.right(angle)
            moves += 1
        tom.color(random_color())
    # have tom draw all the shapes


def pick_a_direction_and_color():
    tom.setheading(random.choice([0, 90, 180, 270]))
    tom.color(random_color())
    # choose a color and direction at random


def random_walk(steps):
    for _ in range(steps):
        tom.forward(12)
        pick_a_direction_and_color()


def spiral_graph(number_of_circles):
    for _ in range(number_of_circles):
        tom.circle(100)
        tom.color(random_color())
        tom.left(360/number_of_circles)


for _ in range(5):
    spiral_graph(random.choice([5,10,15,20,25]))
    random_walk(random.choice([16,32,64,128]))
    shape_time()
    # watch tom the amazing turtle create art right before your eyes!

screen.exitonclick()