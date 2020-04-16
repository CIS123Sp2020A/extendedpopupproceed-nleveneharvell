#Nava Levene-Harvell
#Extended Pop Up

from tkinter import *
import tkinter.messagebox as box

#creates window
window = Tk()
#shows up at the top
window.title("Message Box Example ")


def dialog():
    var = box.askyesno("Message Box", "Proceed?")
    if var == 1:
        box.showinfo("Yes Box", "Proceeding...")
    else:
        box.showwarning("No Box", "Cancelling...")

btn = Button(window,text="Click", command=dialog)
btn.pack(padx=150, pady=50)
window.mainloop()
