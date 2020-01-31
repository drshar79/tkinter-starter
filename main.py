# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import*
from tkinter.ttk import Progressbar
from tkinter import Menu
import time
window = Tk()
window.title("Sample Text") 
window.geometry('700x400') 
lbl = Label(window, text="Welcome", font=("Times New Roman", 50))
lbl.grid(column=0, row=0)
txt=Entry(window, width=10,)
txt.grid(column=4, row=0)
txt.focus()
combo=Combobox(window)
combo['values']=(1,2,3,4,5, "Text")
combo.current(1)
combo.grid(column=3, row=0)
chk=Checkbutton(window, text='Choose')
chk.grid(column=0, row=1)
bar=Progressbar(window, length=200)
bar['value']=70
bar.grid(column=1, row=1)
menu=Menu(window)
new_item=Menu(menu)
menu.add_command(label="File")
new_item.add_command(label="New File")
new_item.add_command(label="Optional file")
menu.add_cascade(label="File2", menu=new_item)
window.config(menu=menu)
spin=Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=2)
score = 0

def addToScore():
  global score
  score += 1
  lbl['text'] = score
# Add a label with the text "Hello"
lbl = Label(window, text=score, font=("Arial Bold", 50))
lbl.grid(column=0, row=5)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 0 , row = 1)
window.mainloop()     # Keep the window open
def countdown(n):
    while n>0:
        print(n)
        n=n-1
    if n==0:
        print("Time's up!")
        countdown(50)
def clicked():
    lbl.configure(text="Button was clicked!!", font=("Arial Bold", 20))
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()