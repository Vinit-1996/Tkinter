import tkinter as tk
def slogan():
     print(" hello Welocome")

root=tk.Tk()
button=tk.Button(root,text='Quit',fg='red',command=quit)
button.pack(side=tk.LEFT)
slogan1=tk.Button(root,text="Hi",command='slogan')
slogan1.pack(side=tk.LEFT)
root.mainloop()