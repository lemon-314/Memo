from tkinter import *

from matplotlib.pyplot import fill

app = Tk()
app.title("备忘录")


text = StringVar()
text.set("短视频害死人！！！\n====================\n")
notes = []
s = StringVar()

frame = Frame(app)
frame1 = Frame(app)


def show():
    text.set("短视频害死人！！！\n====================\n")
    for i, n in enumerate(notes):
        text.set(text.get() + n % i)

def Add():
    top = Toplevel(app)
    Entry(top, width = 30, textvariable = s).pack()
    Button(top, text="OK", command=lambda:Add2(top, s)).pack(fill=X)
    s.set("")
    # return s.get()

def Add2(top, s):
    notes.append(f"%03d. {s.get()}\n--------------------\n")
    show()
    top.destroy()

def Minus():
    top = Toplevel(app)
    s = StringVar()
    Entry(top, width = 30, textvariable = s).pack()
    Button(top, text="OK", command=lambda:Minus2(top, int(s.get()))).pack(fill=X)

def Minus2(top, n):
    notes.pop(n-1)
    show()
    top.destroy()


add = Button(frame1, text="+", command=Add)
minus = Button(frame1, text="-", command=Minus)


note = Label(frame, textvariable = text, justify = LEFT)

note.pack(side=LEFT)

add.pack(side=LEFT)
minus.pack(side=RIGHT)

frame.pack()
frame1.pack()

print(app.winfo_height())
app.mainloop()
