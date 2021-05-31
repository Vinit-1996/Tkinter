from tkinter import *
import tkinter
root=tkinter.Tk()
root.title("Window")
root.geometry("300x300")
frame=Frame(root)
frame.pack()

leftframe=Frame(root)
leftframe.pack(side=LEFT)

Rightframe=Frame(root)
Rightframe.pack(side=RIGHT)

btn1=Button(frame,text="Submit",fg="red",activebackground='red')
btn1.pack(side=LEFT)

btn2=Button(frame,text="Remove",fg="green",activebackground='green')
btn2.pack(side=RIGHT)

btn3=Button(frame,text="ADD",fg="black",activebackground='yellow')
btn3.pack(side=LEFT)

root.mainloop()