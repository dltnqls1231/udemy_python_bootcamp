# from tkinter import *
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# #Label
#
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text2")
# # my_label.place(x=0,y=0)
# my_label.grid(column=2, row=2)
# # Button
#
# def button_clicked():
#     my_label["text"]=input.get()
#
# button = Button(text="button click me", command=button_clicked)
# button.grid(column=4, row=4)
#
# # Entry
#
# input = Entry(width=10)
# input.grid(column=3, row=0)
# input.get()
#
#
#
# window.mainloop()

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=30)
window.config(padx=30, pady=20)

entry = Entry(width=10)
entry.insert(0, "0")
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="Km")
label3.grid(column=2, row=1)

kilo = Label(text="0")
kilo.grid(column=1, row=1)

def calculate():
    mile = float(entry.get())
    kilometer = round(mile * 1.60934, 2)
    kilo["text"] = str(kilometer)

calc = Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)






window.mainloop()