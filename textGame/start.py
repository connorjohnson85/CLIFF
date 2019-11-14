from tkinter import *
root = Tk()

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

Window(root)
mainloop()