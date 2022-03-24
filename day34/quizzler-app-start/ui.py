import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Some Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady= 50)

        self.label = Label(text="Score: 0", font=("Arial", 20, "italic"), highlightthickness=0, bg=THEME_COLOR, fg="#FFFFFF")
        self.label.grid(column=1, row=0)

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#FFFFFF")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    # there code on top and on the botom serve the same purpose
    def is_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.window.after(1000, self.get_next_question)





