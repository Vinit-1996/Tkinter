
'''-------------CheckBoxes-------------'''
from tkinter import *
root=Tk()
var1=IntVar()
Checkbutton(root,text="Male",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(root,text="Female",variable=var2).grid(row=1,sticky=W)


'''----------------Radio Button----------------------------------'''
radiovalue=IntVar()
radio1=Radiobutton(root,text='January',variable=radiovalue,value=1)
radio2=Radiobutton(root,text='February',variable=radiovalue,value=2)
radio3=Radiobutton(root,text='March',variable=radiovalue,value=3)
radio4=Radiobutton(root,text='April',variable=radiovalue,value=4)

radio1.grid(column=0,row=6)
radio2.grid(column=0,row=7)
radio3.grid(column=1,row=6)
radio4.grid(column=1,row=7)
root.mainloop()