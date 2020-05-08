from tkinter import *
from math import *

font = ("Helvetica", 15, "bold")
calc = Tk()
lbl = Label(calc, text="Calculator 2.0", font=font, width=15)#, bg="black", fg="white")
lbl.grid(row=0, column=0, columnspan=4)
entry = Entry(calc, width=12, font=("Helvetica", 20, "bold"))
entry.grid(row=1, column=0, columnspan=4)
btn_list = ["7", "8", "9", "C", "4", "5", "6", "+","1", "2", "3", "-", "*", "0", "/", "="]

def run(x):
    txt = str(entry.get())
    entry.delete(0, END)
    if x == '=':
        res = eval(txt)
        entry.insert(0, res)
    elif x == 'C':
        entry.insert(0, txt[:-1])
    else:
        txt += x
        entry.insert(0, txt)
    
for i in range(16):
    btn = Button(calc, text=btn_list[i], font=font, command=lambda x=btn_list[i]: run(x), width=3)#, bg="black", fg="white")
    btn.grid(row=i//4 + 2, column=i%4)
