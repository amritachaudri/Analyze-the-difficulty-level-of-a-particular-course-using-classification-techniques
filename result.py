from tkinter import *
from PIL import ImageTk
import os
root= Tk()
l2=Label(root,text="The Result Given By the Model is")
l2.pack()
canvas =Canvas(width =300 , height = 200, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = 'img/R1.gif')
image1 = ImageTk.PhotoImage(file = 'img/R2.png')
canvas.create_image(50,60, image = image, anchor = NW)
canvas.create_image(650,60, image = image1, anchor = NW)
def exit_window():
    root.destroy()
exit_image =ImageTk.PhotoImage(file = 'img/exit_image.gif')
b1=Button(root,image=exit_image,command = exit_window)
b1.pack()
root.mainloop()
