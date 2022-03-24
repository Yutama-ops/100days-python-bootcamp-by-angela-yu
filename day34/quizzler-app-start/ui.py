from tkinter import *

THEME_COLOR = "#375362"

class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady= 50)

        self.label = Label(text="Score: 0", font=("Arial", 20, "italic"), highlightthickness=0, bg=THEME_COLOR, fg="#FFFFFF")
        self.label.grid(column=1, row=0)


        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        true_button = Button(image=self.true_img, highlightthickness=0)
        true_button.grid(column=0, row=2)
        false_button = Button(image=self.false_img, highlightthickness=0)
        false_button.grid(column=1, row=2)

        self.window.mainloop()




