from tkinter import *
from pandas import *
import random


BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    french_words = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = read_csv("data/french_words.csv")
finally:
    fw = french_words.to_dict(orient='records')



def i_know():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(fw)
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text=language, fill="white")
    canvas.itemconfig(card_word, text=current_word["French"], fill="white")
    flip_timer = window.after(3000, func=i_dont_know)

def i_know_right():
    fw.remove(current_word)
    print(len(fw))
    i_know()
    data = pandas.DataFrame(fw)
    data.to_csv("words_to_learn.csv", index=False)


def i_dont_know():
    global current_word
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word["English"], fill="black")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=i_dont_know)

language = "French"
word = "Word"

canvas = Canvas(height=526, width=800)
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
card_image = canvas.create_image(400, 263, image=card_back)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text=language, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=word, font=("Arial", 60, "bold"))
canvas.grid(row=0, columnspan=2)


image_right = PhotoImage(file='images/right.png')
button_right = Button(image=image_right, highlightthickness=0, command=i_know_right)
button_right.grid(row=1, column=1)
image_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=image_wrong, highlightthickness=0, command=i_know)
button_wrong.grid(row=1, column=0)

en = i_know()




window.mainloop()


