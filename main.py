
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
rand={}
list_french={}

try:
    pd = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    new_pd=pandas.read_csv("data/french_words.csv")
    list_french=new_pd.to_dict(orient="records")
else:
    list_french = pd.to_dict(orient="records")


def clickme():
    global rand,wintimer
    window.after_cancel(wintimer)
    rand = random.choice(list_french)
    canvas.itemconfig(French,text=rand["French"],fill="black")
    canvas.itemconfig(Tittle,text="French",fill="black")
    canvas.itemconfig(changeimg, image=images)
    wintimer=window.after(3000, func=counter)

def known():
    list_french.remove(rand)
    known_words=pandas.DataFrame(list_french)
    known_words.to_csv("data/words_to_learn.csv",index=False)
    clickme()
    
def counter():

    canvas.itemconfig(French, text=rand["English"],fill="white")
    canvas.itemconfig(Tittle, text="English",fill="white")
    canvas.itemconfig(changeimg,image=images2)


window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
wintimer=window.after(3000, func=counter)

canvas=Canvas(width=800,height=526,highlightthickness=0)
images=PhotoImage(file="images/card_front.png")
images2=PhotoImage(file="images/card_back.png")
changeimg=canvas.create_image(400,263,image=images)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
Tittle=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
French=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

unknownimage=PhotoImage(file="images/wrong.png")
unknownButton=Button(image=unknownimage,padx=50,command=clickme)
unknownButton.grid(row=1,column=0)

knownButtonImage=PhotoImage(file="images/right.png")
knownButton=Button(image=knownButtonImage,command=known)
knownButton.grid(row=1,column=1)

clickme()


window.mainloop()
