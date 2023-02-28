# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#
# Author: Leah Methratta
# Date Created: 2022 02 22
# Date Revised: 2022 02 22
# Purpose: Image Viewer App


from tkinter import *
from PIL import ImageTk, Image
from tkinter.constants import DISABLED, NORMAL

root = Tk()
root.title("Image Viewer App")

my_img0 = ImageTk.PhotoImage(Image.open("images/formulation.png"))
my_img1 = ImageTk.PhotoImage(Image.open("images/img1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))



image_list = [my_img0, my_img1, my_img2, my_img3, my_img4]
last_index = len(image_list) - 1
#image_list = iter(image_list[1:5])

i = 0
val = i

my_label = Label(image = image_list[i])
my_label.grid(row = 0, column = 0, columnspan = 3)

# bd is for border
# relief is to make the label have a "sunken" effect
# anchor allows for the label to be anchored to a direction 
    # for example, let's anchor to the right, or East
status = Label(root, text = "Image " + str(val + 1) + " of " + str(len(image_list)), 
               bd = 1, relief = SUNKEN, anchor = E)
# sticky allows for the label to stretch in any direction 
    # W+E means stretch from left to right, or west to east
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)



def forward():
    
    global my_label
    global button_forward                                              
    global button_back
    global status

 
    global val
    #val +=1
    
    if val >= last_index:
        button_forward = Button(root, text = ">>", state = DISABLED)    
    else:                     
        # To get rid of previous image, and replace it with next one..
        my_label.grid_forget()
        #my_label = Label(image = next(image_list))
        val += 1
        my_label = Label(image = image_list[val])
        my_label.grid(row = 0, column = 0, columnspan = 3)
        status = Label(root, text = "Image " + str(val + 1) + " of " + str(len(image_list)), 
                       bd = 1, relief = SUNKEN, anchor = E)
        status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)


       

def back():
      
    global my_label
    global button_forward                                              
    global button_back

    global val
    
    if val <= 0:
        button_back = Button(root, text = "<<", state = DISABLED )    
    else:                     
        # To get rid of previous image, and replace it with next one..
        my_label.grid_forget()
        #my_label = Label(image = next(image_list))
        val -= 1
        my_label = Label(image = image_list[val])
        my_label.grid(row = 0, column = 0, columnspan = 3)
        status = Label(root, text = "Image " + str(val + 1) + " of " + str(len(image_list)), 
                       bd = 1, relief = SUNKEN, anchor = E)
        status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

button_back = Button(root, text = "<<", command = back)
button_forward = Button(root, text = ">>", command = forward)
button_exit = Button(root, text = "CLOSE", command = root.destroy)

                     


button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
# Adding pady allows for enough space between rows
button_forward.grid(row = 1, column = 2, pady = 10)


root.mainloop()

