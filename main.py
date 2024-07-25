import tkinter
from tkinter import *
import customtkinter
import keyboard
from tkinter import BOTH

#----------UI setup------------
app = customtkinter.CTk()
app.geometry("1500x700")
app.title("Typing test")
app.resizable(0,0)
app.config(bg="steel blue")


frame_1 = customtkinter.CTkFrame(app, fg_color="red")
frame_1.pack(fill = BOTH, expand = True)

frame_2 = customtkinter.CTkFrame(app, fg_color="blue")
frame_2.pack(fill = BOTH, expand = True)
frame_2.propagate(0)
frame_1.propagate(0)


Into_Label = customtkinter.CTkLabel(frame_1, text = 'Welcome! Press start and see how fast you can type the phrase:', fg_color= "red", font = ("Arial", 25))
Into_Label.pack()
Into_Label2 = customtkinter.CTkLabel(frame_1, text = 'The quick brown fox jumps over the lazy dog', fg_color= "red", font = ("Arial", 25))
Into_Label2.pack(pady = 50)

timer_label = customtkinter.CTkLabel(frame_1, text = "0", font = ("Arial", 25))
timer_label.pack(pady = 10, padx = 10)
complete_Label = customtkinter.CTkLabel(frame_1, text = "", font = ("Arial", 25))
complete_Label.pack()

entry_Box = tkinter.Entry(frame_2, width = 100, font = ("Arial", 25))
entry_Box.pack(padx = 100)
start_Button = customtkinter.CTkButton(frame_2, command= lambda: startPressed(), width = 130, text = "Start"  ,font = ("Arial", 25))
start_Button.pack()
finish_Button = customtkinter.CTkButton(frame_2, command = lambda: checkEntry(entry_Box.get()), width = 130,  text = "Finish",  font = ("Arial", 25))
finish_Button.pack()

#----------Methods-------------
time = 0
valid = True
sentence = "the quick brown fox jumps over the lazy dog".replace(" ", "")
def generateSentence():
    global sentence
    pass

def FinishButton():
    finish_Button.pack()
    start_Button.pack_forget()

def StartButton():
    start_Button.pack()
    finish_Button.pack_forget()

def startPressed():
    global valid
    global time
    valid = True
    complete_Label.configure(text = "")
    time = 0
    Timer()
def checkEntry(entry):
    global sentence
    global valid
    if(entry.replace(" ", "") == sentence):
        print("yes")
        time = 0
        valid = False
        entry_Box.delete(0, END)
        complete_Label.configure(text = "Complete!")
        StartButton()
    else:
        FinishButton()
        print("No")


def Timer():
    global time
    global valid
    if(valid):
        FinishButton()
        time = time + 1
        timer_label.configure(text = str(time))
        timer_label.after(1000, Timer)

StartButton()
app.mainloop()
