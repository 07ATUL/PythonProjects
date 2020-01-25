from tkinter import *
window=Tk()
window.title("Atul Gui")
window.geometry("350x200")
me=Label(window,text="Hello World",font=("Arial Bold",50))
me.grid(column=0,row=0)
txt=Entry(window,width=10)
txt.grid(column=0,row=1)
def clicked():
    res="Welcome to " + txt.get()
   # me.configure(text="This was Clicked")
    me.configure(text=res)
btn=Button(window,text="Click Me",bg="red",fg="white",command=clicked)
btn.grid(column=1,row=0)

window.mainloop()