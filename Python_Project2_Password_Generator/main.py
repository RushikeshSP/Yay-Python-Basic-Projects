# To build this project we will use the basic concept of python and libraries – Tkinter, pyperclip, random, string.
from tkinter import *
import tkinter.messagebox as tmsg
import pyperclip
import random
import string


# Created root instance of a class Tk
root = Tk()
password = StringVar()

'''
# Function to Generate Password Without using String Library
def Generate_Password():
    global password
    password = ""  

    seq = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','"','#','$','%','&','()','*','+',',','-','.','/',':,';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']  

    for i in range(int(length.get())):
        password = password+random.choice(seq)

    display.delete("1.0","end")
    display.insert(END, password)
    print(f"Password of length {length.get()} is Generted.")
'''

# Function to Generate Password using String Library
def Generate_Password():
    global password
    password = ""  

    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for i in range((int(length.get()))-4):
        password = password+ random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

    display.delete("1.0","end")
    display.insert(END, password)
    # print(f"Password of length {length.get()} is Generted.")

# Function to Copy Password using Pyperclip Library
def Copy_Password():
    pyperclip.copy(f"{password}")
    pyperclip.paste()           
    # print(f"Password {password} is copied.")  
    tmsg.showinfo("Copy Password",f"You have successfully Copied Password.")  # Function to display ShowInfo box.

# Set the width x height geometry of tk window
root.geometry("400x400")
root.resizable(0,0) 

# Set the Title of window
root.title("YAY - PASSWORD GENERATOR")   

# created the Canvas to set the Background of window
C = Canvas(root, width=1, height=1)
photo = PhotoImage(file = "photo2.png")
background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# Set the main title
MainTitle = Label(root, text = "PASSWORD GENERATOR", font= "arial 20 bold", bg="sky blue")
MainTitle.pack(pady=10)

# Set the sub title
SubTitle = Label(root, text = "PASSWORD LENGTH", borderwidth=1, relief=SUNKEN, font= "arial 14 bold")
SubTitle.pack(pady=10)

# Set the bottom title
BottomTitle = Label(root, text = "RUSHIKESH SANJAY POKHARKAR", font= "arial 11 bold", bg="gold")
BottomTitle.pack(side=BOTTOM, fill=BOTH)

# Created the Spinbox for taking input.
length = Spinbox(root, from_ = 8, to_ = 12, width = 20, bg="silver")
length.pack()
# myslider = Scale(root, from_=8, to=12, orient = HORIZONTAL)
# myslider.pack()

# Button to Generate Password
b1 = Button(root, text = "GENERATE PASSWORD", font = "arial 12 bold", command=Generate_Password)
b1.pack(pady=20)

# Text box to display Generated Password.
display =  Text(root, width= 20, height=1, borderwidth=4, relief= SUNKEN, bg="silver")
display.pack(pady=10)

# Button to Copy Password
b2 = Button(root, text = "COPY TO CLIPBOARD", font = "arial 12 bold", command=Copy_Password)
b2.pack(pady=15)


root.mainloop()
