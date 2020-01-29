# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window
window.title("Sample Text")
# Add a label with the text "Hello"
lbl = Label(window, text="Welcome", font=("Times New Roman Bold", 20))

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
window.geometry('350x200')
btn=Button(window, text="Click Me!", bg="Yellow", fg="Blue")
btn.grid(column=1, row=0)
def clicked():
    lbl.configure(text="Button was clicked!!")
btn=Button(window, text="Click Me!", command=clicked)  
window.mainloop()     # Keep the window open
