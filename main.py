import tkinter
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


label_A = customtkinter.CTkLabel(frame_1, text = 'A', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 1, padx = 2)
label_B = customtkinter.CTkLabel(frame_1, text = 'B', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 2, padx = 2)
label_C = customtkinter.CTkLabel(frame_1, text = 'C', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 3, padx = 2)
label_D = customtkinter.CTkLabel(frame_1, text = 'D', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 4, padx = 2)
label_E = customtkinter.CTkLabel(frame_1, text = 'E', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 5, padx = 2)
label_F = customtkinter.CTkLabel(frame_1, text = 'F', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 6, padx = 2)
label_G = customtkinter.CTkLabel(frame_1, text = 'G', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 7, padx = 2)
label_H = customtkinter.CTkLabel(frame_1, text = 'H', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 8, padx = 2)
label_I = customtkinter.CTkLabel(frame_1, text = 'I', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 9, padx = 2)
label_J = customtkinter.CTkLabel(frame_1, text = 'J', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 10, padx = 2)
label_K = customtkinter.CTkLabel(frame_1, text = 'K', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 11, padx = 2)
label_L = customtkinter.CTkLabel(frame_1, text = 'L', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 12, padx = 2)
label_M = customtkinter.CTkLabel(frame_1, text = 'M', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 13, padx = 2)
label_N = customtkinter.CTkLabel(frame_1, text = 'N', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 14, padx = 2)
label_O = customtkinter.CTkLabel(frame_1, text = 'O', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 15, padx = 2)
label_P = customtkinter.CTkLabel(frame_1, text = 'P', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 16, padx = 2)
label_Q = customtkinter.CTkLabel(frame_1, text = 'Q', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 17, padx = 2)
label_R = customtkinter.CTkLabel(frame_1, text = 'R', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 18, padx = 2)
label_S = customtkinter.CTkLabel(frame_1, text = 'S', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 19, padx = 2)
label_T = customtkinter.CTkLabel(frame_1, text = 'T', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 20, padx = 2)
label_U = customtkinter.CTkLabel(frame_1, text = 'U', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 21, padx = 2)
label_V = customtkinter.CTkLabel(frame_1, text = 'V', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 22, padx = 2)
label_W = customtkinter.CTkLabel(frame_1, text = 'W', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 23, padx = 2)
label_X = customtkinter.CTkLabel(frame_1, text = 'X', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 24, padx = 2)
label_Y = customtkinter.CTkLabel(frame_1, text = 'Y', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 25, padx = 2)
label_Z = customtkinter.CTkLabel(frame_1, text = 'Z', fg_color= "red", font = ("Arial", 25)).grid(row = 2, column = 26, padx = 2)

timer_label = customtkinter.CTkLabel(frame_1, text = "0", font = ("Arial", 25))
timer_label.pack(pady = 100)
complete_Label = customtkinter.CTkLabel(frame_1, text = "", font = ("Arial", 25))
complete_Label.pack()
#----------Methods-------------
time = 0
valid = True
sentence = "the quick brown fox jumps over the lazy dog".replace(" ", "")
def generateSentence():
    global sentence
    pass


def checkEntry(entry):
    global sentence
    global valid
    if(entry.replace(" ", "") == sentence):
        print("yes")
        time = 0
        valid = False
        complete_Label.configure(text = "Complete!")
    else:
        print("No")

def Timer():
    global valid
    if(valid):
        global time
        time = time + 1
        timer_label.configure(text = str(time))
        timer_label.after(1000, Timer)


entry_Box = tkinter.Entry(frame_2, width = 100, )
entry_Box.pack()
start_Button = customtkinter.CTkButton(frame_2, command= lambda: Timer(), width = 70, text = "Start")
start_Button.pack()
finish_Button = customtkinter.CTkButton(frame_2, command = lambda: checkEntry(entry_Box.get()), width = 70, text = "Finish")
finish_Button.pack()



#entry = entry_Box.get()
#checkEntry(entry)
app.mainloop()
