from tkinter import *
from turtle import left, right

state = "Chosing"

window = Tk()
window.title("opdracht 3 - decoder")
window["bg"] = "light gray"

def SET_TITLE_TEXT(text):
    titleText.delete(1.0,END)
    titleText.insert(END, text)
    titleText.tag_add("center", "1.0", "end")   

def CODE(text):
    text = list(text)
    for i in range(0, len(text)-1, 2):
        text[i], text[i+1] = text[i+1], text[i]

    return ''.join(text)

def OK_BUTTON():
    global state
    if e.get() != "":
        if state == "Chosing":
            if e.get().lower() == "code":
                state = "code"
                e.delete(0, END)
                SET_TITLE_TEXT("Type the text you want to code")
            elif e.get().lower() == "decode":
                state = "decode"
                e.delete(0, END)
                SET_TITLE_TEXT("Type the text you want to decode")
        else:
            newText = CODE(e.get())
            e.delete(0,END)
            e.insert(END, newText)

    else:
        SET_TITLE_TEXT("Do you want to code or decode?")
        state = "Chosing"

titleText = Text(window, bg="light gray", border=0, height=1, font=('Arial',18),width=30)
titleText.tag_config("center", justify="center")
SET_TITLE_TEXT("Do you want to code or decode?")

e = Entry(window, width=20, font=(18))
e.focus_set()

b1 = Button(window, text = "OK", width = 10, command = OK_BUTTON)
b2 = Button(window, text = "Cancel", width = 10, command = window.destroy)




titleText.pack()
e.pack()
b1.pack(side=LEFT,padx=100)
b2.pack(side=RIGHT, padx=100)

window.mainloop()