from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Label

my_label=Label(text="I am a Label",font=("Arial",25,"italic"))
my_label.config(text="Label")
# my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
my_label.config(padx=10,pady=10)

#BUTTON Function
# def button_clicked():
#     new_text=input.get()
#     my_label.config(text=new_text)

#BUTTON 1
button = Button(text="New Button")
button.grid(column=2,row=0)

#BUTTON 2
button = Button(text="Button")
button.grid(column=1,row=1)

#ENTRY

input= Entry(width=10)
print(input.get())
input.grid(column=3,row=40)





window.mainloop()