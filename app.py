from main import Tkinter as Tk
import random

scores = {
    "user": 0,
    "com": 0
}

com = None

def second_window():
    window2 = Tk()
    window2.label(com, "white", "grey")
    window2.label(f"Your score {scores['user']}", "white", "black")
    window2.label(f"Com score {scores['com']}", "black", "white")
    window2.adjust()


def rock():
    global com

    com_choice = random.choice(["rock", "paper", "scissor"])

    if com_choice == "rock":
        pass

    elif com_choice == "paper":
        scores["com"] += 1

    else:
        scores["user"] += 1

    com = com_choice

    second_window()

    
def paper():
    global com

    com_choice = random.choice(["rock", "paper", "scissor"])

    if com_choice == "paper":
        pass

    elif com_choice == "scissor":
        scores["com"] += 1

    else:
        scores["user"] += 1

    com = com_choice

    second_window()


def scissor():
    global com

    com_choice = random.choice(["rock", "paper", "scissor"])

    if com_choice == "scissor":
        pass

    elif com_choice == "rock":
        scores["com"] += 1

    else:
        scores["user"] += 1

    com = com_choice

    second_window()


window1 = Tk()
window1.button("rock", "black", "red", rock)
window1.button("paper", "black", "green", paper)
window1.button("scissor", "black", "yellow", scissor)
window1.canvas("white")
window1.adjust()
