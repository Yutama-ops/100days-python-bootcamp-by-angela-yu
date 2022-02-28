from tkinter import *


# Button
def Calculate():
    miles = float(input.get())
    miles *= 1.609
    result["text"] = miles


# window
window = Tk()
window.title("Mile to km converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.get()
input.grid(column=1, row=0)

# miles label
miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2, row=0)

# is_equal_to label
is_equal_to = Label(text="Is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0, row=1)

# result label
result = Label(text="0", font=("Arial", 12, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="Newest Text")
result.grid(column=1, row=1)

# km label
km = Label(text="I Am a Label", font=("Arial", 12, "bold"))
km.grid(column=2, row=1)

# button
button = Button(text="Calculate")
button.config(command=Calculate)
button.grid(column=1, row=2)





window.mainloop()
