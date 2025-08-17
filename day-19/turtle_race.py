
from turtle import Turtle, Screen
import random

is_race_on = False
screen=Screen()
screen.setup(700,500)
user_choice=screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
color=["red","orange","yellow","green","blue","purple"]
y_positions=[-150,-100,-50,0,50,100]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    ycoordinate=y_positions[turtle_index]
    new_turtle.goto(x=-330, y=ycoordinate)
    all_turtle.append(new_turtle)

if user_choice:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>330:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_choice:
                print(f"You turtle {winning_color} has won the race. Congrates!")
                print("""
       ***************       
     *                 *     
   *     0       0     *     
  *                     *    
 *        \\     /       *    
 *         \\___/        *    
  *                     *    
   *   \\___________/   *     
     *                 *     
       ***************       
""")
            else:
                print(f"The turtle {winning_color} has loss the race. Try Again!")
                print("""
                       ***************       
                     *                 *     
                   *     0       0     *     
                  *                     *    
                 *         _____        *    
                 *        /     \\       *    
                  *                     *    
                   *   /_________\\   *     
                     *                 *     
                       ***************       
                """)


        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()