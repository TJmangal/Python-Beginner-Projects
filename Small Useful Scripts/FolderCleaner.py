"""
    This program will rearrange files in a folder by creating a folder for each file type
"""

import os
import shutil
import tkinter


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def folder_cleaner(folder_path):
    os.chdir(folder_path)
    mapping_dict = {"jpg": "Image", "png": "Image", "JPG": "Image", "PNG": "Image", "pdf": "PDF",
                    "doc": "Word Document", "docx": "Word Document"}
    lst = os.listdir(folder_path)
    for item in lst:
        if os.path.isdir(item):
            continue
        item_extension = item.split(".")[1]
        if item_extension in mapping_dict.keys():
            create_folder(mapping_dict[item_extension])
            shutil.move(item, mapping_dict[item_extension])
        else:
            print("Unsupported file extension")
    exit()


if __name__ == '__main__':

    root = tkinter.Tk()

    label = tkinter.Label(root, text="Enter the folder you want to clean", font=('Areal', 16))
    label.pack()

    folder = tkinter.Entry(root)
    folder.pack(pady=20)

    button = tkinter.Button(root, text="SUBMIT", font=('Areal', 16), background="green",
                            command=lambda: folder_cleaner(folder.get()))
    button.pack(pady=20)

    root.mainloop()


