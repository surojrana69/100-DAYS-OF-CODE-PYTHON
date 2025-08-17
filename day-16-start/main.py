# import another_module
# print(another_module.name)

# '''way of creating a object'''
# # import turtle
# # tom=turtle.Turtle()
#
# from turtle import Turtle, Screen
# tom=Turtle()
# print(tom) #printing an object
# tom.shape("turtle")
# tom.color("darkblue")
# tom.forward(300)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table=PrettyTable()
table.add_column ("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric", "Water","Fire"])
table.align="c"
print(table)

