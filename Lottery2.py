from tkinter import *

#Author Athenkosi Gongotha

from random import randint
import random
import datetime
from tkinter import messagebox

Lottonumbers = []

now = datetime.datetime.now()
mynewtime=now.strftime('%Y-%m-%d. %H:%M:%S')
x = mynewtime

# Declaring a function for my Play Button
def go():
    """
    en1 = int(n1.get())
    en2 = int(n2.get())
    en3 = int(n3.get())
    en4 = int(n4.get())
    en5 = int(n5.get())
    en6 = int(n6.get())
    """
    # Adding the user input into a list
    InputNumbers = [int(en1.get()), int(en2.get()), int(en3.get()), int(en4.get()), int(en5.get()), int(en6.get())]
    enDisp2.insert(0,str(str(InputNumbers)[1:-1]))# Displaying my Input number
    # Generating my Random number and appending them on a list
    for i in range(6):
        value = random.randint(1, 49)
        if value not in Lottonumbers: # Cancelling the duplicates from my random numbers list
            Lottonumbers.append(value)
    enDisp.insert(0, str(str(Lottonumbers)[1:-1])) # Displaying the  random numbers generated in the list
    # Creating a counter to compare my 2 lists
    counter = 0
    for i in InputNumbers:
        if i in Lottonumbers:
            counter += 1
            # if counter == 2:
            #     messagebox.showinfo('', 'Congrats you have won')
            # elif counter == 3:
            #     messagebox.showinfo('', 'Congrats you have won')


    print(counter)
    prizemoney={6:"R10, 000 000.00", 5:"R8,584.00", 4:"R2,384.00", 3:"R100.50", 2:"R20.00", 1:"R0.00", 0:"R0.00"}
    prizemoney.get(counter)
    print(prizemoney[counter])
    print(Lottonumbers)
    print(InputNumbers)
    winning = prizemoney.get(counter)
    En_winning.insert(0, str(winning))

    winners = open('winnings.txt', 'r+')
    winners.truncate(0)
    for item in winning:
        winners.write(item)
    winners.write("\n" + x)
    winners.close()



win2 = Tk()
n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()
n5 = StringVar()
n6 = StringVar()

t = StringVar()

win2.geometry('1115x320')
win2.title('A G Lottery machine')
win2.config(bg='#086972')
l0 = Label(win2, text='The\n National\n Lottery', width=20, bg='gold', font=('Times')).grid(columnspan=8, row=0, column=2, pady=20)

l1 = Label(win2, text='One', width=5, bg='#0A043C', fg='white', font=('forte',15))
l2 = Label(win2, text='Two', width=5, bg='#0A043C', fg='white', font=('forte',15))
l3 = Label(win2, text='Three', width=5, bg='#0A043C', fg='white', font=('forte',15))
l4 = Label(win2, text='Four', width=5, bg='#0A043C', fg='white', font=('forte',15))
l5 = Label(win2, text='Five', width=5, bg='#0A043C', fg='white', font=('forte',15))
l6 = Label(win2, text='Six', width=5, bg='#0A043C', fg='white', font=('forte',15))
l1.grid(column=0, row=1,padx=0), l2.grid(column=1, row=1), l3.grid(column=2, row=1),
l4.grid(column=3, row=1), l5.grid(column=4, row=1), l6.grid(column=5, row=1),

en1 = Entry(win2, width=5,  bg='#87DFD6', fg='yellow', font=('forte',15))
en2 = Entry(win2, width=5,  bg='#87DFD6', fg='cyan', font=('forte',15))
en3 = Entry(win2, width=5,  bg='#87DFD6', fg='blue', font=('forte',15))
en4 = Entry(win2, width=5,  bg='#87DFD6', fg='cyan', font=('forte',15))
en5 = Entry(win2, width=5,  bg='#87DFD6', fg='white', font=('forte',15))
en6 = Entry(win2, width=5,  bg='#87DFD6', fg='black', font=('forte',15))
en1.grid(column=0, row=2), en2.grid(column=1, row=2), en3.grid(column=2, row=2),
en4.grid(column=3, row=2), en5.grid(column=4, row=2), en6.grid(column=5, row=2)

l11 = Label(win2, text='Played Numbers', width=15, bg='#8F384D', fg='white', font=('forte',15))
l12 = Label(win2, text='Winning Numbers', width=15, bg='#8F384D', fg='white', font=('forte',15))
l11.grid(column=7, row=1, padx=10), l12.grid(column=8, row=1, padx=10)

lbl_time = Label(win2, text=mynewtime, bg='#086972', fg='white', font=('forte',10)).grid(column=0, row=10, pady=20)
En_winning = Entry(win2, text='', width=10, bg='white', fg='black', font=('forte',15))
En_winning.grid(column=7, row=10, pady=20)


enDisp2 = Entry(win2, width=17,  bg='white', fg='yellow', font=('forte',10))
enDisp2.grid(column=7, row=2, pady=20)

enDisp = Entry(win2, width=17, bg='white', fg='cyan', font=('forte',10) )
enDisp.grid(column=8, row=2, pady=20)

btnE = Button(win2, text='Play', width=20, bg='gold', command=go)
btnE.grid(column=6, row=11, pady=20)




win2.mainloop()
