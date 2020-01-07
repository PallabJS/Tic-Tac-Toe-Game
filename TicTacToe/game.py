import tkinter as tk
from tkinter.ttk import *
import numpy as np

#-------------------------------    WINDOW SIZE --------------------------------------------
w = 340    #340
h = 400    #310
na = np.array([(1,2,3),(4,5,6),(7,8,9)])
p1_score = 0
p2_score = 0
p1_name = ""
p2_name = ""
k = ""
start = True
def clearText():
    global p1_name
    global p2_name
    p1_name = e1.get()
    p2_name = e2.get()
    e1.destroy()
    l1.destroy()
    e2.destroy()
    l2.destroy()
    button.destroy()
    firstwindow.destroy()

def winnerLogic(na):
    for i in range(0,3):
        for j in range(0,1):
            if na[i][j] == na[i][j+1] == na[i][j+2] == -1:
                return "p1"
            elif na[i][j] == na[i][j+1] == na[i][j+2] == 0:
                return "p2"
    for i in range(0,3):
        for j in range(0,1):
            if na[j][i] == na[j+1][i] == na[j+2][i] == -1:
                return "p1"
            elif na[j][i] == na[j+1][i] == na[j+2][i] == 0:
                return "p2"
    if na[0][0] == na[1][1] == na[2][2] == -1:
        return "p1"
    elif na[0][0] == na[1][1] == na[2][2] == 0:
        return "p2"
    if na[0][2] == na[1][1] == na[2][0] == -1:
        return "p1"
    elif na[0][2] == na[1][1] == na[2][0] == 0:
        return "p2"
#-------------------------------    WINNER VALIDATION  ---------------------------------------
count = 0
def checkWinner(pos):
    global playername
    global p1_name
    global p2_name
    global na
    global count
    global start
    global k

    print("Current player:", playername)

    if pos == 1:
        if playername == p1_name:
            na[0][0] = -1
        else:
            na[0][0] = 0
        print(na[0][0])

    elif pos == 2:
        if playername == p1_name:
            na[0][1] = -1
        else:
            na[0][1] = 0
        print(na[0][1])

    elif pos == 3:
        if playername == p1_name:
            na[0][2] = -1
        else:
            na[0][2] = 0
        print(na[0][2])

    elif pos == 4:
        if playername == p1_name:
            na[1][0] = -1
        else:
            na[1][0] = 0
        print(na[1][0])

    elif pos == 5:
        if playername == p1_name:
            na[1][1] = -1
        else:
            na[1][1] = 0
        print(na[1][1])

    elif pos == 6:
        if playername == p1_name:
            na[1][2] = -1
        else:
            na[1][2] = 0
        print(na[1][2])

    elif pos == 7:
        if playername == p1_name:
            na[2][0] = -1
        else:
            na[2][0] = 0
        print(na[2][0])

    elif pos == 8:
        if playername == p1_name:
            na[2][1] = -1
        else:
            na[2][1] = 0
        print(na[2][1])

    elif pos == 9:
        if playername == p1_name:
            na[2][2] = -1
        else:
            na[2][2] = 0
        print(na[2][2])
    count = count+1

    k = winnerLogic(na)
    if k == "p1":
        main.destroy()
        k = p1_name
    elif k == "p2":
        main.destroy()
        k = p2_name

    print("COUNT: ", count)
    if count == 9:
        print("DATA----------")
        print(na)

#-------------------    PLAYER DETAILS  ---------------------------------------
firstwindow = tk.Tk()
firstwindow.title("Player 1 Name")

l1 = tk.Label(text = "Enter 1st Player's name: ", font = 15, pady = 20)
e1 = tk.Entry(firstwindow, font = 15)
l1.pack()
e1.pack()

l2 = tk.Label(text = "Enter 2st Player's name: ", font = 15, pady = 20)
e2 = tk.Entry(firstwindow, font = 15)
l2.pack()
e2.pack()

button = tk.Button(firstwindow,text = "OK", width = 10, height = 2, command = clearText)
button.pack()

firstwindow.minsize(w+200,h)
firstwindow.mainloop()

main = tk.Tk()
main.title("TIC TAC TOE by Pallab JS")
#-------------------------------    PLAYER MARKERS  -----------------------------------
empty = tk.PhotoImage(file = "R:\Projects\Python\TicTacToe\Images\empty.png")
cross = tk.PhotoImage(file = "R:\Projects\Python\TicTacToe\Images\cross.png")
circle = tk.PhotoImage(file = "R:\Projects\Python\TicTacToe\Images\circle.png")
player = cross
playername = p1_name

#-------------------------------    GAME CLICKS MANAGER ---------------------------------------
def changePlayer(pos):
    global playername
    global player
    global p1_name
    global p2_name
    global info
    if playername == p1_name:
        info.config(text = str(p1_name+"'s"+" TURN"))
        # print(p1_name,"'s turn")
        checkWinner(pos)
        playername = p2_name
        player = circle
    else:
        info.config(text = str(p2_name+"'s"+" TURN"))
        # print(p2_name,"'s turn")
        checkWinner(pos)
        playername = p1_name
        player = cross      

#-------------------------------    PlAYER MARKER SWITCH    -----------------------------------
def update(pos,playername):
    global start

    # if start == True:
    #     print(p1_name,"'s turn")
    #     start = False
    #     playername = p2_name

    if pos == 1:
        p11['command'] = p11.destroy
        q11 = tk.Label(main, image = player).grid(row = 1, column = 1)
        changePlayer(pos)
        
    elif pos == 2:
        p12['command'] = p12.destroy
        q12 = tk.Label(main, image = player).grid(row = 1, column = 2)
        changePlayer(pos)
    elif pos == 3:
        p13['command'] = p13.destroy
        q13 = tk.Label(main, image = player).grid(row = 1, column = 3)
        changePlayer(pos)
    elif pos == 4:
        p21['command'] = p21.destroy
        q21 = tk.Label(main, image = player).grid(row = 2, column = 1)
        changePlayer(pos)
    elif pos == 5:
        p22['command'] = p22.destroy
        q22 = tk.Label(main, image = player).grid(row = 2, column = 2)
        changePlayer(pos)
    elif pos == 6:
        p23['command'] = p23.destroy
        q23 = tk.Label(main, image = player).grid(row = 2, column = 3)
        changePlayer(pos)
    elif pos == 7:
        p31['command'] = p31.destroy
        q31 = tk.Label(main, image = player).grid(row = 3, column = 1)
        changePlayer(pos)
    elif pos == 8:
        p32['command'] = p32.destroy
        q32 = tk.Label(main, image = player).grid(row = 3, column = 2)
        changePlayer(pos)
    elif pos == 9:
        p33['command'] = p33.destroy
        q33 = tk.Label(main, image = player).grid(row = 3, column = 3)
        changePlayer(pos)

#-------------------------------    INITIALIZATION  ---------------------------------------

p11 = tk.Button(main, image = empty)
p11.grid(row=1,column=1)
p11['command'] = lambda : update(1,player)

# lambda idx=l: self.click(idx)

p12 = tk.Button(main, image = empty)
p12.grid(row=1,column=2)
p12['command'] = lambda : update(2,playername)

p13 = tk.Button(main, image = empty)
p13.grid(row=1,column=3)
p13['command'] = lambda : update(3,playername)

p21 = tk.Button(main, image = empty)
p21.grid(row=2,column=1)
p21['command'] = lambda : update(4,playername)

p22 = tk.Button(main, image = empty)
p22.grid(row=2,column=2)
p22['command'] = lambda : update(5,playername)

p23 = tk.Button(main, image = empty)
p23.grid(row=2,column=3)
p23['command'] = lambda : update(6,playername)

p31 = tk.Button(main, image = empty)
p31.grid(row=3,column=1)
p31['command'] = lambda : update(7,playername)

p32 = tk.Button(main, image = empty)
p32.grid(row=3,column=2)
p32['command'] = lambda : update(8,playername)

p33 = tk.Button(main, image = empty)
p33.grid(row=3,column=3)
p33['command'] = lambda : update(9,playername)
# p11.config()

#----------------------------------  Grid Setup  -----------------------------------
info = tk.Label(main, text = str(p1_name+"'s"+" turn"), font = 5)
info.grid(row = 4, column = 1, columnspan = 2)
gamename = tk.Label(main, text = "TIC TAC TOE", font = 5, foreground = "blue", background = "grey", height = 2, width = 28)
gamename.grid(row = 0, column = 1, columnspan = 3)

main.minsize(w,h)
main.maxsize(w,h)
main.mainloop()

#---------------------------------- FINAL WINDOW    -----------------------------------
winner = tk.Tk()

dialog = tk.Label(winner, text = str("WINNER IS "+k), font = 10, width = 50, height = 30)
dialog.pack()
winner.after(2000, winner.destroy)
winner.mainloop()