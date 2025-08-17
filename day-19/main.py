from turtle import  Turtle,Screen

tom = Turtle()
screen=Screen()

# def move_forwards():
#     tom.forward(10)
# def rotate_left():
#     tom.left(90)
# def move_backwards():
#     tom.backward(10)
# def rotate_right():
#     tom.right(90)
# screen.onkey(key="a", fun=rotate_left)              #YOU CAN ALSO DO THIS # screen.onkey(rotate_left,"space")
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=rotate_right)


def move_forwards():
    tom.forward(10)
def rotate_left():
    new_heading=tom.heading() + 20
    tom.setheading(new_heading)
def move_backwards():
    tom.backward(10)
def rotate_right():
    new_heading=tom.heading() - 20
    tom.setheading(new_heading)
def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(clear_screen, "c")






screen.listen()




screen.exitonclick()
