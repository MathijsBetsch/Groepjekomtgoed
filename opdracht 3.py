from tkinter import *

window = Tk()
window.title("opdracht 2 country")
window["bg"] = "light gray"

def READ_FILE():
    f = open("C:\\Users\\kenov\\OneDrive\\Bureaublad\\Code\\data_capital_city.txt", "r")
    file = f.read()
    f.close()
    return file.split("\n")

lines = READ_FILE()

titleText = Text(window, bg="light gray", height=1, border=0)
titleText.tag_config("center", justify="center")
titleText.insert(END, "Type the name of a country: ")
titleText.tag_add("center", "1.0", "end")

e = Entry(window)
e.focus_set()

def FIND_CITY(country):
    for place in lines:
        point = place.split("/")
        if point[0].lower() == country.lower():
            titleText.delete(1.0,END)
            titleText.insert(END, "The capital city of " + point[0] + " is " + point[1])
            titleText.tag_add("center", "1.0", "end")
            e.delete(0, END)
            return
    ASK_FOR_CAPITAL(country)

creatingNew = False


def ASK_FOR_CAPITAL(country):
    e.delete(0, END)
    titleText.delete(1.0,END)
    titleText.insert(END, "No capital found. input the capital of " + country + ":")
    titleText.tag_add("center", "1.0", "end")
    global newCountry
    newCountry = country
    global creatingNew
    creatingNew = True

def ADD_NEW_COUNTRY(capital):
    f = open("C:\\Users\\kenov\\OneDrive\\Bureaublad\\Code\\data_capital_city.txt", "a")
    f.write("\n" + newCountry + "/" + capital)
    f.close()
    global creatingNew
    creatingNew = False
    titleText.delete(1.0,END)
    titleText.insert(END, "Type the name of a country: ")
    titleText.tag_add("center", "1.0", "end")   
    e.delete(0, END)
    global lines
    lines = READ_FILE()



newCountry = ""
def OK_BUT():
    if e.get() != "":
        global creatingNew
        if creatingNew != True:
            FIND_CITY(e.get())
        else:
            ADD_NEW_COUNTRY(e.get())
    else:
        titleText.delete(1.0,END)
        titleText.insert(END, "Type the name of a country: ")
        titleText.tag_add("center", "1.0", "end") 
        creatingNew = False  
        
def CANCEL_BUT():
    window.destroy()

b1 = Button(window, text = "OK", width = 10, command = OK_BUT)
b2 = Button(window, text = "Cancel", width = 10, command = CANCEL_BUT)


titleText.pack()
e.pack()
b1.pack(side=LEFT)
b2.pack(side=RIGHT)

window.mainloop()
