from datetime import date
from tkinter import *


window = Tk()
window.title("opdracht 2")
window['bg']="black"


f = open("C:\\Users\\kenov\\OneDrive\\Bureaublad\\code\\events.txt")
text = f.read()
lines = text.split("\n")

today = date.today()
today = today.strftime("%d/%m/%y")
days = today.split("/")

txt = Text(window,bg="black",foreground="orange",font=('Arial',18,'bold','underline'), bd = 0, height=2, width= 50)
txt.insert(END, "My countdowncalendar" + "\n")
txt1 = Text(window,bg="black",foreground="cyan",font=('Arial',18,'bold','underline'), bd = 0, height=3, width=50)

for index in range(len(lines)-1):

    eventDay = lines[index].split(",")
    eventdata = eventDay[1].split("/")

    d0 = date(int(days[2]), int(days[1]), int(days[0]))
    d1 = date(int(eventdata[2]), int(eventdata[1]), int(eventdata[0]))
    delta = d1 - d0

    txt1.insert(END, "It is ")
    txt1.insert(END, delta.days)
    txt1.insert(END, " days up until ")
    txt1.insert(END, eventDay[0] + "\n")

txt.pack()
txt1.pack()

window.mainloop()
