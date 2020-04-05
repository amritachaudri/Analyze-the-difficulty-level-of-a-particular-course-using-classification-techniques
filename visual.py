from tkinter import *
from PIL import ImageTk
import os
root= Tk()
#creating the canvas
l1=Label(root,text="The Graphs and HeatMap of used in the Model are:")
l1.pack()
canvas =Canvas(width =300 , height = 200, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = 'img/mtt.png')
image1 = ImageTk.PhotoImage(file = 'img/heatmap.png')
image2 = ImageTk.PhotoImage(file = 'img/grade.png')
image3 = ImageTk.PhotoImage(file = 'img/course.png')

canvas.create_image(500,30, image = image, anchor = NW)
canvas.create_image(50,30, image = image3, anchor = NW)
canvas.create_image(950,30, image = image2, anchor = NW)
canvas.create_image(500,300, image = image1, anchor = NW)
def exit_window():
    root.destroy()
exit_image =ImageTk.PhotoImage(file = 'img/exit_image.gif')
b1=Button(root,image=exit_image,command = exit_window)
b1.pack()
mainloop()
