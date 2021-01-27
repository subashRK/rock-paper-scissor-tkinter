import tkinter

class Tkinter:
    def __init__(self):
        self.win = tkinter.Tk()

    def button(self, name, fg, bg, command):
        button = tkinter.Button(self.win, text=name, fg=fg, bg=bg, command=command)
        button.pack()

    def label(self, name, fg, bg):
        label = tkinter.Label(self.win, text=name, fg=fg, bg=bg)
        label.pack()

    def canvas(self, bg):
        canvas = tkinter.Canvas(self.win, bg=bg)
        canvas.pack()
    
    def adjust(self):
        self.win.mainloop()
        print(self.win)

