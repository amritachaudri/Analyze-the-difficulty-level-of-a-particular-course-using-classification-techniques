# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:19:29 2020

@author: Harprem Singh
"""
from tkinter import *
from PIL import ImageTk
import os
import sys
root= Tk()
l1=Label(root,text="WELCOME TO THE PROJECT WHICH ANALIYZES THE DIFFICULTY LEVEL OF A PARTICULAR COURSE")
l1.pack()
canvas =Canvas(width =300 , height = 200, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image5 = ImageTk.PhotoImage(file = 'img/lpu-about-logo.jpg')
canvas.create_image(600,30, image = image5, anchor = NW)
image = ImageTk.PhotoImage(file = 'img/student.gif')
canvas.create_image(700,290, image = image, anchor = NW)
f1=Frame(canvas,width=50,height=5)
canvas.create_window((2,2),window=f1, anchor = NW)

#code for about the project
def abtpro():
    root.destroy()
    #import abtpro
    os.system('python abtpro.py')
image1=ImageTk.PhotoImage(file = 'img/about project.png')
b1=Button(root, text="About The Project",image=image1,command=abtpro)
b1.pack(side=LEFT,anchor=NW)
#code for visualization
def visaul():
    root.destroy()
    #import visual
    os.system('python visual.py')
image2=ImageTk.PhotoImage(file = 'img/visualization.jpg')
b2=Button(root,text="Visualization",image=image2, command=visaul)
b2.pack(side=LEFT,anchor=SW)
#code exit button
def exit_window():
    root.destroy()
exit_image =ImageTk.PhotoImage(file = 'img/exit_image.gif')
b4=Button(root,text="Exit",image=exit_image,command = exit_window)
b4.pack(side=RIGHT,anchor=NE)

#code for result
def result():
    root.destroy()
    #import result
    os.system('python result.py')
image3=ImageTk.PhotoImage(file = 'img/result.jpg')
b3=Button(root,text="Resuts",image=image3,command=result)
b3.pack(side=RIGHT,anchor=SE)


mainloop()
