"""This project add, subtract, multiply, divide, power and radical, number 1 to number 2 in GUI. Use Tkinter to GUI."""


from tkinter import *


# start main loop.
calculator = Tk()


# colors setting
background_color = "#29332c"
labels_background_color = background_color
labels_color = "#d3ebd9"
entries_backgroung_color = "#000000"
entries_text_color = "#17e856"
buttons_background_color = "#245154" # "#02240b"
buttons_text_color = "#e6ede8"


# window setting
calculator.title("Calc")
calculator.config(bg=background_color)
calculator.minsize(700, 200)
calculator.maxsize(700, 200)
calculator.iconbitmap("icon.ico")


# fonts setting
labels_font = "Times New Roman (Headings CS)"
labels_font_size = 15


# Define functions
def raise_error():
    result_entry.delete(0, END)
    result_entry.insert(0, "ERROR")


def add_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x+y)
    except:
        raise_error()


def subtraction_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x-y)
    except:
        raise_error()


def multiply_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x*y)
    except:
        raise_error()


def divide_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x/y)
    except:
        raise_error()


def power_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x**y)
    except:
        raise_error()


def radical_1_to_2():
    try:
        x = int(number1_entry.get())
        y = int(number2_entry.get())
        result_entry.delete(0, END)
        result_entry.insert(0, x**(y**-1))
    except:
        raise_error()


# Define labels
number1_label = Label(calculator, text="num 1 :", font=(labels_font, labels_font_size), bg=labels_background_color, fg=labels_color, width=10)
number2_label = Label(calculator, text="num 2 :", font=(labels_font, labels_font_size), bg=labels_background_color, fg=labels_color, width=10)
equals_label = Label(calculator, text="Equals : ", font=(labels_font, labels_font_size), bg=labels_background_color, fg=labels_color)
creator_label = Label(calculator, text="code: shsotoudegan@gmail.com", font=(labels_font, labels_font_size), bg=labels_background_color, fg=labels_color)
empt_label_1 = Label(calculator, width=10, bg=labels_background_color)
empt_label_2 = Label(calculator, width=10, bg=labels_background_color)


# Define Entries.
number1_entry = Entry(calculator, width=20, borderwidth=4, bg=entries_backgroung_color, fg=entries_text_color)
number2_entry = Entry(calculator, width=20, borderwidth=4, bg=entries_backgroung_color, fg=entries_text_color)
result_entry = Entry(calculator, width=30, borderwidth=4, bg=entries_backgroung_color, fg=entries_text_color)


# Define Buttons
plus_button = Button(calculator, text="+", width=10, command=add_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)
subtraction_button = Button(calculator, text="-", width=10, command=subtraction_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)
multiply_button = Button(calculator, text="*", width=10, command=multiply_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)
divide_button = Button(calculator, text="/", width=10, command=divide_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)
power_button = Button(calculator, text="**", width=10, command=power_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)
radical_button = Button(calculator, text="rad", width=10, command=radical_1_to_2, bg=buttons_background_color, fg=buttons_text_color, bd=0)


# Grid any thing
number1_label.grid(row=0, column=0, padx=10, pady=10)
number1_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
number2_label.grid(row=0, column=3, padx=10, pady=10)
number2_entry.grid(row=0, column=4, columnspan=2, padx=10, pady=10)
plus_button.grid(row=1, column=0, padx=10, pady=10)
subtraction_button.grid(row=1, column=1, padx=10, pady=10)
empt_label_1.grid(row=1, column=2, padx=10, pady=10)
empt_label_2.grid(row=1, column=3, padx=10, pady=10)
multiply_button.grid(row=1, column=4, padx=10, pady=10)
divide_button.grid(row=1, column=5, padx=10, pady=10)
power_button.grid(row=2, column=0, padx=10, pady=10)
creator_label.grid(row=2, column=1, columnspan=4, padx=10, pady=10)
radical_button.grid(row=2, column=5, padx=10, pady=10)
equals_label.grid(row=3, column=1, pady=10)
result_entry.grid(row=3, column=2, columnspan=3, pady=10)

# end loop
calculator.mainloop()
