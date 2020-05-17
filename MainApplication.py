from tkinter import *
from ScrRec import *
import docx

def startrec():
    wordfile = filename.get()
    f = ScrRec(wordfile)
    f.recodSrc()
def stoprec():
    wordfile = filename.get()
    doc = docx.Document()
    doc.save(wordfile)

gui = Tk()
gui.configure(background="light green")
gui.title("Screen recorder Application")
gui.geometry("350x200")
enterTask = Label(gui, text="Give word document name ", font=("Arial Bold", 10), bg="light green").grid(row=1, column=1)
filename = Entry(gui, width=30)
filename.grid(row=2, column=1)
start = Button(gui, text="Start", fg="red", bg="light blue", command=startrec)
start.grid(row=3, column=1)
#Stop = Button(gui, text="Stop", fg="red", bg="light blue", command=stoprec)
#Stop.grid(row=4, column=1)
#TextArea = Text(gui, height=5, width=20, font="lucida 13")

#TextArea.grid(row=5, column=1, padx=10, sticky=W)
# create a text entry box
# for typing the task
# enterTaskField = Entry(gui)
a = filename.get()
gui.mainloop()
print(a)
