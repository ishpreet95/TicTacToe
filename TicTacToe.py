from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("The Tic Tac Toe Game")

clicked = True
count = 0


def disable_buttons():
    b00['state'] = 'disable'
    b01['state'] = 'disable'
    b02['state'] = 'disable'

    b10['state'] = 'disable'
    b11['state'] = 'disable'
    b12['state'] = 'disable'

    b20['state'] = 'disable'
    b21['state'] = 'disable'
    b22['state'] = 'disable'


# **********************************FINISHING************************************
def finishing(b1, b2, b3):
    b1.config(bg='#86C232', fg='#222629')
    b2.config(bg='#86C232', fg='#222629')
    b3.config(bg='#86C232', fg='#222629')
    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!!\n" + b1['text'] + " WINS")


# *********************************ALGORITHM**********************************
def checkifwon():
    global winner
    winner = False
    if b00['text'] == b01['text'] and b00['text'] == b02['text'] and b00['text'] != ' ':
        winner = True
        finishing(b00, b01, b02)
        disable_buttons()
        return 1

    if b00['text'] == b11['text'] and b11['text'] == b22['text'] and b00['text'] != ' ':
        winner = True
        finishing(b00, b11, b22)
        disable_buttons()
        return 1

    if b00['text'] == b10['text'] and b10['text'] == b20['text'] and b00['text'] != ' ':
        winner = True
        finishing(b00, b10, b20)
        disable_buttons()
        return 1

    if b01['text'] == b11['text'] and b11['text'] == b21['text'] and b01['text'] != ' ':
        winner = True
        finishing(b01, b11, b21)
        disable_buttons()
        return 1

    if b02['text'] == b11['text'] and b11['text'] == b20['text'] and b02['text'] != ' ':
        winner = True
        finishing(b02, b11, b20)
        disable_buttons()
        return 1

    if b02['text'] == b12['text'] and b12['text'] == b22['text'] and b02['text'] != ' ':
        winner = True
        finishing(b02, b12, b22)
        disable_buttons()
        return 1

    if b10['text'] == b11['text'] and b11['text'] == b12['text'] and b10['text'] != ' ':
        winner = True
        finishing(b10, b11, b12)
        disable_buttons()
        return 1

    if b20['text'] == b21['text'] and b21['text'] == b22['text'] and b20['text'] != ' ':
        winner = True
        finishing(b20, b21, b22)
        disable_buttons()
        return 1

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a TIE\nTRY AGAIN !!")
        disable_buttons()
        return 1


# ************************************************************************************

# Button Clicked Function
def b_click(b):
    global clicked, count
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count = count + 1
        # IMPORTANT
        checkifwon()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count = count + 1
        # IMPORTANT
        checkifwon()
    else:
        messagebox.showerror('Tic Tac Toe', 'Error 404')


# Reset
def reset():
    global b00, b01, b02, b10, b11, b12, b20, b21, b22
    global clicked, count
    clicked = True
    count = 0
    # Buttons
    b00 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b00))
    b01 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b01))
    b02 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b02))

    b10 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b10))
    b11 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b11))
    b12 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b12))

    b20 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b20))
    b21 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b21))
    b22 = Button(root, text=' ', font=("Roboto", 20, 'bold'), fg="#86C232", bg="#222629", height=2, width=5,
                 command=lambda: b_click(b22))

    # Putting buttons in the grid
    b00.grid(row=0, column=0)
    b01.grid(row=0, column=1)
    b02.grid(row=0, column=2)

    b10.grid(row=1, column=0)
    b11.grid(row=1, column=1)
    b12.grid(row=1, column=2)

    b20.grid(row=2, column=0)
    b21.grid(row=2, column=1)
    b22.grid(row=2, column=2)


# Menu
the_menu = Menu(root)
root.config(menu=the_menu)

# Options menu
options_menu = Menu(the_menu, tearoff=False)
the_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()
