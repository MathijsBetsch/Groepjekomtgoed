from asyncio.windows_events import NULL
from textwrap import fill
from tkinter import *
from turtle import color

window = Tk()
window.title("opdracht 1")
window.minsize(width=500, height=400)
cv = Canvas(width=500,height=300)


# Create label
l = Label(window, text = "What has to be assembled")
l.config(font =("Courier", 28))


# Create an Exit button.
b1 = Button(window, text = "Exit",
            command = window.destroy)

def create_circle(x, y, r, color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return cv.create_oval(x0, y0, x1, y1, fill = color)

def Create_Sqaure(x, y, s, color):
    x0 = x-s 
    y0 = y-s
    x1 = x+s
    y1 = y+s
    return cv.create_rectangle(x0, y0, x1, y1, fill= color)

create_circle(100, 70, 50, "red")
create_circle(230, 70, 50, "yellow")
create_circle(360, 70, 50, "pink")

Create_Sqaure(100, 200, 50, "yellow")
Create_Sqaure(230, 200, 50, "green")
Create_Sqaure(360, 200, 50, "red")

l.pack()
cv.pack()
b1.pack()

cv.mainloop()
