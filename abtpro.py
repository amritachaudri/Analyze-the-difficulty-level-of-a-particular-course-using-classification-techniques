from tkinter import *
from PIL import ImageTk
import os
root= Tk()
l2=Label(root,text="Step By Step Approach")
l2.pack()
canvas =Canvas(width =300 , height = 200, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = 'img/step1.gif')
canvas.create_image(550,60, image = image, anchor = NW)
l1=Label(root,text="1. Importing the data set:The data set containing the information about the students is imported.\n 2. Data pre-processing:In this step we are trying to perform feature scaling on the given data set.First \nwe perform mapping on feature 'Grade'. Then we perform label encoding on the given data set as it\n convert is the categorical data into numerical data. Then with the help of ” imputer ”we remove null\nvalues present in the data set as we cannot remove the column of the row containing the\n null values the strategy used for removing the null values is mean\n3. Visualisation:In this step we plot graph between different features of the data set such as grade, course \nattendance, different evaluations, and with the help of heat map check the relationship different features \nof the data set.\n4. Splitting the data set:With the help of train test split, we split the data set into parts that is training and\n testing.\n5. Training the model:We choose some models for the comparative study. The models chosen are SVM, \nlinear regression,k nearest neighbours, naive Bayes.\n6. Hyper parameter tuning:With the use of pipeline we perform hyper parameter tuning on linear regression\n classification model.\n7. Confusion matrix:With Help of confusion matrix on SVM we try to visualise the classified data\n8 Checking the accuracy:Check the accuracy of the above models by R2 score as the models are classification\n models\n9. Checking the difficulty level of the course:The Result mean grade of all the students available in the data set,\nif the mean is between 0 to 30 percentage the course is referred as difficult else if the range between 40 to 70 \npercent then the course is referred as medium else if the percentage is above 70 the course is referred as easy.")
l1.pack()

def exit_window():
    root.destroy()
exit_image =ImageTk.PhotoImage(file = 'img/exit_image.gif')
b1=Button(root,image=exit_image,command = exit_window)
b1.pack()

root.mainloop()
