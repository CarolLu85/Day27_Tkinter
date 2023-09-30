from tkinter import *


def button_clicked():
    km = str(float(user_input.get()) * 1.609)
    result.config(text= km)
#   reslut.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=60, pady=20)

unit_m = Label(text="Miles", font=("Arial", 12, "bold"))
unit_m.grid(column=5, row=1)
unit_m.config(padx=10, pady=10)


user_input = Entry(width=10)
user_input.grid(column=4, row=1)
# user_input.config(text="0")


equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.grid(column=0, row=2)
unit_m.config(padx=30, pady=30)

result = Label(text="0", font=("Arial", 12, "bold"))
result.grid(column=4, row=2)


unit_k = Label(text="Km", font=("Arial", 12, "bold"))
unit_k.grid(column=5, row=2)


button = Button(text="Calculate", font=("Arial", 12, "bold"), command=button_clicked)
button.grid(column=4, row=3)







window.mainloop()