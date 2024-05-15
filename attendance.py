import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import PIL.Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
from customtkinter import *
import customtkinter

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "C:\\Users\\PARKASH\\Desktop\\CTK\Attendance-Management-system-using-face-recognition-master\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\PARKASH\\Desktop\\CTK\Attendance-Management-system-using-face-recognition-master\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\PARKASH\\Desktop\\CTK\Attendance-Management-system-using-face-recognition-master\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\PARKASH\\Desktop\\CTK\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\PARKASH\\Desktop\\CTK\Attendance-Management-system-using-face-recognition-master\\Attendance"


app = CTk()
app.title("Face recognizer")
app.geometry("1000x740")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
app.configure(background="black")


canvas = tk.Canvas(app, width=790, height=1400, bd=0, highlightthickness=0, relief='ridge', background='black')
canvas.place(x=1,y= 1)

img= ImageTk.PhotoImage(Image.open("UI_Image/bg.png"))
canvas.create_image(1,1,anchor=NW,image=img)

# to destroy screen
def del_sc1():
    sc1.destroy()

# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

brd = tk.Label(app,
        fg="White",
        bg="#42aaf5",
        width=35,
        relief=RIDGE,
        bd=10,
        font=("arial", 35)
        )
brd.place(x=790, y=1)

titl = tk.Label(
    app, text="Attendance Management", bg="#42aaf5", fg="white", font=("Helvetica", 30,'bold'),
)
titl.place(x=1040, y=12)

ri = Image.open("UI_Image/register.png")
new_size = (350, 350)  
ri = ri.resize(new_size, Image.Resampling.LANCZOS)
r = ImageTk.PhotoImage(ri)
label1 = Label(app, image=r)
label1.image = r 
label1 = tk.Label(border = 0, text = 'Submit', fg = 'black', image= r,bg = '#282424') 
label1.place(x=850, y=130)

ai = Image.open("UI_Image/attendance.png")
new_size = (350, 350)   
ai = ai.resize(new_size, Image.Resampling.LANCZOS)
a = ImageTk.PhotoImage(ai)
label2 = Label(app, image=a)
label2.image = a
label2 = tk.Label(border = 0, text = 'Submit', fg = 'black', image= a,bg = '#282424') 
label2.place(x=1350, y=130)

vi = Image.open("UI_Image/verifyy.png")
new_size = (350, 350)   
vi = vi.resize(new_size, Image.Resampling.LANCZOS)
v = ImageTk.PhotoImage(vi)
label3 = Label(app, image=v)
label3.image = v
label3 = tk.Label(border = 0, text = 'Submit', fg = 'black', image= v,bg = '#282424') 
label3.place(x=850, y=630)


li = Image.open("UI_Image/info.png")
new_size = (350, 350)   
li = li.resize(new_size, Image.Resampling.LANCZOS)
l = ImageTk.PhotoImage(li)
label4 = Label(app, image=l)
label4.image = l
label4 = tk.Label(border = 0, text = 'Submit', fg = 'black', image= l,bg = '#282424') 
label4.place(x=1350, y=630)

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="yellow",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=370)

r = CTkButton(master=app,
    fg_color="#42aaf5",
    height = 32,
    width= 90,
    font=("Helvetica", 19,'bold'),
    hover_color="#27638f",
    corner_radius= 50,
    text="Register a new student",
    command=TakeImageUI
)
r.place(x=470, y=290)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = CTkButton(master=app,
    text="Take Attendance",
    command=automatic_attedance,
    fg_color="#42aaf5",
    height = 32,
    width= 100,
    font=("Helvetica", 18,'bold'),
    hover_color="#27638f",
    corner_radius= 50,
)
r.place(x=780, y=290)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = CTkButton(master=app,
    text="View Attendance",
    command=view_attendance,
    fg_color="#42aaf5",
    height = 32,
    width= 100,
    font=("Helvetica", 18,'bold'),
    hover_color="#27638f",
    corner_radius= 50,
)
r.place(x=500, y=580)

r = CTkButton(master=app,
    text="View Student Info",
    command=view_attendance,
    fg_color="#42aaf5",
    height = 32,
    width= 100,
    font=("Helvetica", 18,'bold'),
    hover_color="#27638f",
    corner_radius= 50,
)
r.place(x=780, y=580)

r = CTkButton(master=app,
    text="EXIT",
    command=quit,
    fg_color="#42aaf5",
    height = 30,
    width= 100,
    font=("Helvetica", 18,'bold'),
    hover_color="#27638f",
    corner_radius= 15,
)
r.place(x=680, y=690)


app.resizable(False, False)
app.mainloop()
