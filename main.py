import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# packed = center of the program
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text= "New Text")
# my_lable.pack(side="left"/"right"/"bottom")
# my_label.pack(expand=True)

# Advanced Python Arguments:
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
# my_function(c=1, a=3, b=2)
# to call this function via putting agruments in. we can just setup defualt value for a,b,c.
# then when call this function ,we can just simply do: my_function(), then it will run with the default value.
# if, you want to change one of values, lets say b, then just do: my_function((b=5).
# (it means that from tkinter import everything)
# from tkinter import *
# with this one, we can save some typing via getting rid of the module mention("tkinter") before the name of the class.
# for example: my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold")) CAN BE WRITTEN :
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))


button = Button(text= "Click me")
def button_clicked():
    my_label.config("i got clicked")

button = Button(text="click me", command=button_clicked())
button.pack()





window.mainloop()
