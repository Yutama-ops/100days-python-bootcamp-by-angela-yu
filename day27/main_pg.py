from tkinter import *


# Button
def button_click():
    input.get()
    my_label["text"] = input.get()


# window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Newest Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me")
button.config(command=button_click)
# button.pack()
# button.place(x=10, y=10)
button.grid(column=1, row=1)

# new button
new_button = Button(text="Click Me")
new_button.config(command=button_click)
# new_button.pack()
# new_button.place(x=10, y=10)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.get()
# input.pack()
# input.place(x=100, y=100)
input.grid(column=3, row=3)



window.mainloop()
