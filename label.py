'''import  tkinter as tk
root=tk.Tk()
a=tk.Label(root,text="Hello World")
a.pack()
root.mainloop()'''

from tkinter import *
root=Tk()
var=StringVar()
label=Label(root,textvariable=var,relief=RAISED)
var.set("Hey I am Python Coder")
label.pack()
root.mainloop()