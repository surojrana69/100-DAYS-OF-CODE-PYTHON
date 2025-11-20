#Miles to Km project using Tkinter

from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20,pady=20)

#INPUT FIELD
input= Entry(width=10)
input.place(x=200,y=0)

#Labels

label=Label(text="Label",font=("Arial",10,""))
label.config(text="Miles")
label.place(x=260,y=0)

label2=Label(text="Label",font=("Arial",10,""))
label2.config(text="is equal to ")
label2.place(x=100,y=20)

label3=Label(text="Label",font=("Arial",10))
label3.config(text="Km")
label3.place(x=300,y=20)

result_label=Label(text=0,font=("Arial",10))
result_label.place(x=200,y=25)

# BUTTON Function
def button_clicked():
    miles= float(input.get())
    km=miles * 1.60934
    result_label.config(text=f"{km}")


#BUTTON 1
button = Button(text="Calculate", command=button_clicked)
button.place(x=200,y=50)



window.mainloop()