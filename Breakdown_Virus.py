# message box

from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
import os


def message():
    GB = 1000
    download = 0
    speed = 5

    messagebox.showwarning(title="System warning", message="Installing Malware in 5 sec", icon="warning")

    while download < GB:
        time.sleep(0.05)
        bar["value"] += (speed / GB) * 100
        download += speed
        percentage.set(str(int((download / GB) * 100)) + "%")
        windows.update_idletasks()
        bar.pack()
        percentage_label.config(bg="white")
        percentage_label.pack()

    time.sleep(5)

    messagebox.showwarning(title="Windows defender", message="Virus detected")

    if messagebox.askyesnocancel(title="Windows defender",
                                 message="Suspicious Malware activity detected. Wanna delete?"):
        time.sleep(3)
        if messagebox.askretrycancel(title="ERROR", message="Failed to delete virus"):

            while messagebox.askretrycancel(title="ERROR", message="Failed to delete virus") is True:
                messagebox.askretrycancel(title="ERROR", message="Failed to delete virus")

            if not messagebox.askretrycancel(title="ERROR", message="Failed to delete virus"):
                messagebox.showwarning(title="WARNING", message="System breakdown in few sec")
                # os.system("shutdown /s /t 10")
        else:
            messagebox.showwarning(title="WARNING", message="System breakdown in few sec")
            # os.system("shutdown /s /t 10")

    else:
        messagebox.showwarning(title="WARNING", message="System breakdown in few sec")
        # os.system("shutdown /s /t 10")


windows = Tk()
windows.geometry("300x150")
windows.config(bg="white")
percentage = StringVar()

icon = PhotoImage(file="windows.png")
windows.iconphoto(True, icon)

windows.title("Warning")

danger_image = PhotoImage(file="poison.png")

warning_sign = Label(windows,
                     text="WARNING!! DO NOT PRESS THIS BUTTON",
                     font=('Arial', 10, BOLD),
                     fg="red")

warning_sign.pack()

button = Button(windows,
                image=danger_image,
                bg="red",
                command=message)

button.pack()

bar = Progressbar(windows, orient=HORIZONTAL, length=300, )

percentage_label = Label(windows, textvariable=percentage, bg="white")

windows.mainloop()
