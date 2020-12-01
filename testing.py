from tkinter import *
import datetime
import random
from random import randint
from tkinter import messagebox

lotto_numbers = []

now = datetime.datetime.now()
new_time = now.strftime('%Y-%m-%d. %H:%M:%S')
x = new_time

# Declaring a function for the play button


def play():
# typecasting must be inside the list

    # entry_1 = int(number1.get())
    # entry_2 = int(number2.get())
    # entry_3 = int(number3.get())
    # entry_4 = int(number4.get())
    # entry_5 = int(number5.get())
    # entry_6 = int(number6.get())

    # Adding the user input into a list

    input_numbers = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get())]

    # Input number display

    ent_display2.insert(0, str(str(input_numbers)[1:-1]))

    # Generating random numbers and append on a list

    for i in range(6):
        value = random.randint(1, 49)

    #  Cancel duplicates from random numbers list

        if value not in lotto_numbers:
            lotto_numbers.append(value)

    #  Displaying generated random numbers

    ent_display.insert(0, str(str(lotto_numbers)[1:-1])) ##########################################

    #  Counter comparing 2 lists

    counter = 0
    for i in input_numbers:
        if i in lotto_numbers:
            counter += 1

    print(counter)
    prize_money = {6: "R10, 000 000.00", 5: "R8,584.00", 4: "R2,384.00",
                   3: "R100.50", 2: "R20.00", 1: "R0.00", 0: "R0.00"}
    prize_money.get(counter)
    print(prize_money[counter])
    print(lotto_numbers)
    print(input_numbers)
    winning = prize_money.get(counter)
    entry_winning.insert(0, str(winning))

    winners = open('winnings.txt', 'r+')
    winners.truncate(0)
    for item in winning:
        winners.write(item)
    winners.write("\n" + x)
    winners.close()


window2 = Tk()
number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()
number5 = StringVar()
number6 = StringVar()

t = StringVar()


# Graphical User Interface Using Grid

window2.geometry('1200x600')
window2.title('Lotto Machine')
window2.configure(bg="IndianRed")
label_first = Label(window2, text='Ithuba National Lottery', width=20, bg='IndianRed', font='Roboto').grid(row=0, column=0)

# Labels

num_label1 = Label(window2, text='Enter 6 Numbers Below:', width=25, bg='IndianRed', fg='black', font='Roboto').grid(column=0, row=1)

# Entries

entry1 = Entry(window2, width=4, textvariable=number1, bg='white', fg='black', font='Roboto 20')
entry1.grid(column=0, row=2)
entry2 = Entry(window2, width=4, textvariable=number2, bg='white', fg='black', font='Roboto 20')
entry2.grid(column=1, row=2)
entry3 = Entry(window2, width=4, textvariable=number3, bg='white', fg='black', font='Roboto 20')
entry3.grid(column=2, row=2)
entry4 = Entry(window2, width=4, textvariable=number4, bg='white', fg='black', font='Roboto 20')
entry4.grid(column=3, row=2)
entry5 = Entry(window2, width=4, textvariable=number5, bg='white', fg='black', font='Roboto 20')
entry5.grid(column=4, row=2)
entry6 = Entry(window2, width=4, textvariable=number6, bg='white', fg='black', font='Roboto 20')
entry6.grid(column=5, row=2)

# Labels 2
label1 = Label(window2, text='Played Numbers', width=15, bg='IndianRed', fg='black').grid(column=0, row=3, padx=10)
label2 = Label(window2, text='Winning Numbers', width=15, bg='IndianRed', fg='black').grid(column=2, row=3, padx=10)

# Labels 3 & Entries

lbl_time = Label(window2, text=new_time, bg='IndianRed', fg='black').grid(column=2, row=0, pady=20)
entry_winning = Entry(window2, text='Winnings', width=20, bg='white', fg='black', font='Roboto 14')
entry_winning.grid(column=0, row=10, pady=20)


ent_display2 = Entry(window2, width=20,  bg='white', fg='black', font='Roboto 20')
ent_display2.grid(column=1, row=3, pady=10)
ent_display = Entry(window2, width=20, bg='white', fg='black', font='Roboto 20')
ent_display.grid(column=3, row=3, pady=10)

# Buttons

btn = Button(window2, text='Play', width=30, bg='grey20', fg='white', command=play)
btn.grid(column=0, row=11, pady=20)

window2.mainloop()
