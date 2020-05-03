from tkinter import *
from math import *


class Application:
    def __init__(self):
        master = Tk()
        self.master = master
        master.title('Right Triangle Solver')
        master.geometry('800x500')
        white = 'white'

        self.inputFrame = Frame(master, width=400, height=500, bg=white)
        self.outputFrame = Frame(master, width=400, height=500, bg=white)
        self.imageFrame = Frame(self.inputFrame, bg=white)
        self.entryFrame = Frame(self.inputFrame, bg=white)

        self.inputFrame.grid(row=0, column=0)
        self.outputFrame.grid(row=0, column=1)
        self.imageFrame.pack(side='top')
        self.entryFrame.pack(side='bottom')

        self.rightTriangle = PhotoImage(file='right_triangle.gif')
        self.rightTriangleLabel = Label(self.imageFrame, image=self.rightTriangle, bg=white)

        self.rightTriangleLabel.image = self.rightTriangle
        self.rightTriangleLabel.pack(side='top')

        self.hypLabel = Label(self.entryFrame, text='Hyp')

        master.mainloop()

    def sinSide(self, opp, hyp, x):
        if opp == 0:


    def cosSide(self, adj, hyp, x):

    def tanSide(self, adj, hyp, x):

    def tanAngle(self, opp, adj, x):
        
    def solveAngle(self, x):
        ang = 180 - 90 - x
        return ang
    
    def decideOrder(self):
        self.


if __name__ == '__main__':
    Application()
