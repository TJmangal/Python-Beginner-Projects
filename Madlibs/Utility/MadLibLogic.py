import tkinter


def logic(prompts: [str], mad_lib: str):
    """
    :param prompts: list of prompts that user will get while playing madlib game
    :param mad_lib: the madlib story in string format
    :return: None

    This method is the main logic of madlib game. if asks the user to input different words for a madlib and then
    prints the final madlib by appending the user inputs.
    """
    entries = []

    def clicked_submit(story):
        for ent in entries:
            index = story.find("{}")
            story = story[:index] + ent.get() + story[index + 2:]
        result.config(text=story, fg="black")

    root = tkinter.Tk()
    root.title("Mad Libs")
    root.configure(background="gray")
    for prompt in range(0, len(prompts)):
        frame = tkinter.Frame(root)
        frame.pack()
        label = tkinter.Label(frame, text=prompts[prompt].capitalize(), font=('calibri', 12, 'bold'), width=15,
                              anchor="w")
        label.grid(row=prompt, column=0)
        entry = tkinter.Entry(frame, width=25)
        entry.grid(row=prompt, column=1)
        entries.append(entry)

    button = tkinter.Button(root, text="Submit", font=('Areal', 16), width=16, bg="gray",
                            command=lambda: clicked_submit(mad_lib))
    button.pack(pady=20)
    result = tkinter.Label(root, text="", background="grey")
    result.pack(pady=10)
    root.mainloop()
