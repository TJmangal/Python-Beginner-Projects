import tkinter
from tkinter import messagebox
import random

x = 10
num = 0


def display_num():
    global num
    num = random.randint(1, x)
    messagebox.showinfo("Message Box", "Random Number Generated!")


def game_logic():
    user_input = int(guess.get())
    if user_input == num:
        result_label.config(text="Congratulations! Your guess is correct", fg="green")
    elif user_input > num:
        result_label.config(text="Guess again! Too High", fg="red")
    else:
        result_label.config(text="Guess again! Too Low", fg="red")


# Screen, size of screen and title on the screen
tk = tkinter.Tk()
tk.geometry("500x500")
tk.title("Number Guessing Game")

# Title/Text inside the screen
Title = tkinter.Label(tk, text="Number Guessing Game", font=("Arial", 30))
Title.pack()

# Creating a frame which will contain buttons and input box. Frame class helps to create a frame of desired background
# color, width and height. In pack function we can give keyword argument pady which defines how much space should be
# between this component and previous one (adds padding on y axis)
frame1 = tkinter.Frame(tk)
frame1.pack(pady=60)

# Adding label in the frame1
guess_num_label = tkinter.Label(frame1, text=f"Guess a number from 1 to {x}", font=("Arial", 20))
guess_num_label.pack()

# Adding input box in frame1 and storing input
guess = tkinter.Entry(frame1, font=("Areal", 16))
guess.pack(pady=10)

# Generate Random number button
generate_num_button = tkinter.Button(frame1, text="Generate The Number", font=("Areal", 16), width=16,
                                     background="blue", command=display_num)
generate_num_button.pack()

# Guess Button
guess_button = tkinter.Button(frame1, text="Guess", font=("Areal", 16), width=16, background="green", command=game_logic)
guess_button.pack(pady=10)

# Result label
result_label = tkinter.Label(frame1, text="", font=("Areal", 16))
result_label.pack()

tk.mainloop()
