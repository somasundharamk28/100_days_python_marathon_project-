from tkinter import *
import pandas as pd
import random
import time
word = {}
to_learn = {}

BACKGROUNDCOLOUR = "#B1DDC6"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")



def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill ="black")
    canvas.itemconfig(card_word, text=word["French"],fill = "black")
    canvas.itemconfig(card_front, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text = word["English"], fill ="white")
    canvas.itemconfig(card_front,image=card_back_image)
def is_known():
    to_learn.remove(word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn",index = False)
    new_word()


window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUNDCOLOUR)
flip_timer = window.after(3000, func=flip_card)




canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400,263,image = card_back_image)
card_front = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",40,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
canvas.configure(bg=BACKGROUNDCOLOUR,highlightthickness=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.config(pady=50, padx=50)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.config(pady=50, padx=50)
right_button.grid(row=1, column=1)

new_word()

window.mainloop()