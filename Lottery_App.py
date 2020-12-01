from tkinter import *
from tkinter import messagebox
root = Tk()


def validate():
    age = int(txtAge.get())
    if age >= 18:
        import Lottery2
        Lottery2.Play()
        root.withdraw

    else:
        messagebox.showinfo('Underage', 'Come back when you are 18 or older')
        txtAge.delete(0, END)
        txtAge.focus


root.title('Lottery Machine')

root.geometry('220x90')

lblAge = Label(root, text='Enter your age', width=15)
lblAge.grid(column=0, row=0)

txtAge = Entry(root, width=10)
txtAge.grid(column=1, row=0)

btnEnter = Button(root, bg='green', text='Enter', command=validate)
btnEnter.grid(column=0, row=2)

root.mainloop()
