from tkinter import *
import pandas
import random


try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")


to_learn = data.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


def next_card():
    global current_word
    current_word = random.choice(to_learn)
    canvers.itemconfig(card_title, text="French", fill="black")
    canvers.itemconfig(card_word, text=current_word["French"], fill="black")
    canvers.itemconfig(card_background, image=canvers_front_img)
    window.after(4000, func=flip_card)


def flip_card():
    canvers.itemconfig(card_title, text="English", fill="white")
    canvers.itemconfig(card_word, text=current_word["English"], fill="white")
    canvers.itemconfig(card_background, image=canvers_back_img)

def known_word():
    to_learn.remove(current_word)
    next_card()
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

window = Tk()
window.title("Capstone project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvers = Canvas(width=800, height=526)
canvers_front_img = PhotoImage(file="card_front.png")
canvers_back_img = PhotoImage(file="card_back.png")

card_background = canvers.create_image(400, 263, image=canvers_front_img)
canvers.grid(row=0, column=0, columnspan=2)
canvers.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvers.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvers.create_text(400, 265, text="Word", font=("Ariel", 40, "bold"))

cross_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
tick_img = PhotoImage(file="right.png")
tick_button = Button(image=tick_img, highlightthickness=0, command=known_word)
tick_button.grid(row=1, column=1)
next_card()
window.mainloop()
