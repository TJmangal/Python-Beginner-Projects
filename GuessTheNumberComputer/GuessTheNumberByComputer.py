import random
import tkinter
import time

guess = 0
high = 10
low = 1


def generate_random(l, h):
    global guess
    guess = random.randint(l, h)
    label3.config(text=f"Is you number = {guess}?")


def read_feedback():
    global guess
    global low
    global high

    feedback = entry.get()

    if feedback.lower() == "l":
        low = guess + 1
    elif feedback.lower() == "h":
        high = guess - 1
    elif feedback.lower() == "c":
        label3.config(text="Congratulations!!", fg="green")
    else:
        label3.config(text="Invalid Input!!", fg="red")
    generate_random(low, high)


root = tkinter.Tk()
root.geometry("585x500")
root.title("Guess the number computer!")

frame1 = tkinter.Frame(root)
frame1.pack(pady=10)

label1 = tkinter.Label(frame1, text="Think of a number between 1-10 and computer will guess the number",
                       font=('Areal', 10))
label1.pack(pady=10)

label2 = tkinter.Label(frame1, text="Click start when ready", font=('Areal', 10))
label2.pack(pady=10)

button1 = tkinter.Button(frame1, text="Start", font=('Areal', 10), background="green",
                         command=lambda: generate_random(low, high))
button1.pack(pady=10)

label3 = tkinter.Label(frame1, text="", font=('Areal', 10), fg="red")
label3.pack(pady=10)

label4 = tkinter.Label(frame1, text="Provide feedback in below box and click submit. (l) if value is low, "
                                    "(h) if value is high & (c) if correct", font=('Areal', 10))
label4.pack(pady=10)

entry = tkinter.Entry(frame1)
entry.pack(pady=10)

button2 = tkinter.Button(frame1, text="Submit Feedback", font=('Areal', 10), background="green",
                         command=read_feedback)
button2.pack()

root.mainloop()
