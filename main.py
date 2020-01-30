# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import*
from tkinter.ttk import Progressbar
window = Tk()
window.title("Sample Text") 
window.geometry('700x400') 
lbl = Label(window, text="Welcome", font=("Times New Roman", 50))
lbl.grid(column=0, row=0)
txt=Entry(window, width=10,)
txt.grid(column=0, row=0)
txt.focus()
combo=Combobox(window)
combo['values']=(1,2,3,4,5, "Text")
combo.current(1)
combo.grid(column=3, row=0)
chk=Checkbutton(window, text='Choose')
chk.grid(column=0, row=1)
bar=Progressbar(window, length=200)
bar['value']=70
txt.grid(column=1, row=1)
def clicked():
    lbl.configure(text="Button was clicked!!", font=("Arial Bold", 20))
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()