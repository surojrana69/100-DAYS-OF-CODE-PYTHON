# from turtle import Turtle, Screen
# import  random
#
# tom=Turtle()
# tom.shape("turtle")
# tom.color("Limegreen")

# for _ in range(10):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()

#for square
# for _ in range(4):
#     tom.forward(100)
#     tom.left(90)


#for pentagon
# for _ in range(5):
#     tom.forward(100)
#     tom.left(72)

# colors=["green","blue","pink","cyan","red"]
# def draw_shape(number_sides):
#     for _ in range(number_sides): #put number of sides of polygons
#         angle = 360/number_sides   #number of sides
#         tom.forward(100)
#         tom.left(angle)
#
# for shape_side in range(3,11):
#     tom.color(random.choice(colors))
#     draw_shape(shape_side)

#RANDOM WALK PROGRAM
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)  # Correct place to set color mode

tom = Turtle()
tom.shape("turtle")




def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r, g, b)
    return color

tom.speed(100)
def spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        tom.color(random_colors())
        tom.circle(100)
        tom.setheading(tom.heading()+10)
        tom.circle(100)
spirograph(5)




screen =Screen()

screen.exitonclick()

# import turtle as toy
# tom=toy.Turtle()
#
# import heroes
# print(heroes.gen())