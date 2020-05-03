from math import sqrt
from tkinter import *
import time


class PT_App:
    def __init__(self, master):
        self.master = master
        master.title('Right Triangle Solver')
        master.geometry("200x215")

        self.entryFrame = Frame(master)
        self.entryFrame.grid(row=0)

        self.buttonAndSteps = Frame(master)
        self.buttonAndSteps.grid(row=1)

        self.solutionFrame = Frame(master)
        self.solutionFrame.grid(row=2)

        self.firstLegLabel = Label(self.entryFrame, text='Leg (a): ')
        self.secondLegLabel = Label(self.entryFrame, text='Leg (b): ')
        self.hypotenuseLabel = Label(self.entryFrame, text='Hyp (c): ')

        self.firstLegLabel.grid(row=0, column=0)
        self.secondLegLabel.grid(row=1, column=0)
        self.hypotenuseLabel.grid(row=2, column=0)

        self.entryText = StringVar(self.entryFrame, value='unknown')
        self.entryText1 = StringVar(self.entryFrame, value='unknown')
        self.entryText2 = StringVar(self.entryFrame, value='unknown')

        self.firstLegEntry = Entry(
            self.entryFrame, textvariable=self.entryText)
        self.secondLegEntry = Entry(
            self.entryFrame, textvariable=self.entryText1)
        self.hypotenuseEntry = Entry(
            self.entryFrame, textvariable=self.entryText2)

        self.firstLegEntry.grid(row=0, column=1)
        self.secondLegEntry.grid(row=1, column=1)
        self.hypotenuseEntry.grid(row=2, column=1)

        self.submitEntries = Button(
            self.buttonAndSteps, command=self.run, text='Solve')
        self.resetEntries = Button(
            self.buttonAndSteps, command=self.resetValues, text='Reset')
        self.statusLabel = Label(self.buttonAndSteps, text='Enter values...')

        self.submitEntries.grid(row=0, column=0)
        self.resetEntries.grid(row=0, column=1)
        self.statusLabel.grid(row=1)

        self.stepLabel1 = Label(self.solutionFrame, text='#1')
        self.stepLabel2 = Label(self.solutionFrame, text='#2')
        self.stepLabel3 = Label(self.solutionFrame, text='#3')
        self.stepLabel4 = Label(self.solutionFrame, text='#4')
        self.stepLabel5 = Label(self.solutionFrame, text='#5')

        self.stepLabel1.grid(row=0, column=0)
        self.stepLabel2.grid(row=1, column=0)
        self.stepLabel3.grid(row=2, column=0)
        self.stepLabel4.grid(row=3, column=0)
        self.stepLabel5.grid(row=4, column=0)

        self.stepsLabel1 = Label(self.solutionFrame)
        self.stepsLabel2 = Label(self.solutionFrame)
        self.stepsLabel3 = Label(self.solutionFrame)
        self.stepsLabel4 = Label(self.solutionFrame)
        self.stepsLabel5 = Label(self.solutionFrame)

        self.stepsLabel1.grid(row=0, column=1)
        self.stepsLabel2.grid(row=1, column=1)
        self.stepsLabel3.grid(row=2, column=1)
        self.stepsLabel4.grid(row=3, column=1)
        self.stepsLabel5.grid(row=4, column=1)

    def run(self):
        self.statusLabel['text'] = 'Calculating...'
        self.master.after(1500, self.run2)

    def run2(self):
        a, b, c = self.getValues()
        value_1, value_2, functionType = self.decideFunction(a, b, c)

        if functionType == 0:
            self.solveHypotenuse(value_1, value_2)

        elif functionType == 1 or functionType == 2:
            self.solveLeg(value_1, value_2, functionType)

        self.statusLabel['text'] = 'Complete. Enter values...'

    def resetValues(self):
        self.firstLegEntry.delete(0, END)
        self.secondLegEntry.delete(0, END)
        self.hypotenuseEntry.delete(0, END)

        self.firstLegEntry.insert(END, 'unknown')
        self.secondLegEntry.insert(END, 'unknown')
        self.hypotenuseEntry.insert(END, 'unknown')

    def getValues(self):
        a = self.firstLegEntry.get()
        b = self.secondLegEntry.get()
        c = self.hypotenuseEntry.get()

        return a, b, c

    def decideFunction(self, a, b, c):
        if a == 'unknown':
            return float(b), float(c), 1

        elif c == 'unknown':
            return float(a), float(b), 0

        elif b == 'unknown':
            return float(a), float(c), 2

    def solveHypotenuse(self, leg, leg2):
        step1 = 'a² + b² = c² (PT)'
        step2 = '%s² + %s² = c²' % (str(leg), str(leg2))

        leg = leg ** 2
        leg2 = leg2 ** 2
        step3 = '%s + %s = c²' % (str(leg), str(leg2))

        total = leg + leg2
        total = str(total)
        step4 = '%s = c²' % total

        total = float(total)
        total = sqrt(total)
        total = round(total, 1)
        total = str(total)
        step5 = 'c = %s' % total

        self.stepsLabel1['text'] = step1
        self.stepsLabel2['text'] = step2
        self.stepsLabel3['text'] = step3
        self.stepsLabel4['text'] = step4
        self.stepsLabel5['text'] = step5

        self.hypotenuseEntry.delete(0, END)
        self.hypotenuseEntry.insert(END, total)

    def solveLeg(self, leg, hyp, leg_type):
        step1 = "c² - a² = b² (Pythagoras Theorem)"
        step2 = '%s² - %s² = b²' % (str(hyp), str(leg))

        hyp = hyp ** 2
        leg = leg ** 2
        step3 = '%s - %s = b²' % (str(hyp), str(leg))

        total = hyp - leg
        total = str(total)
        step4 = '%s = b²' % total

        total = float(total)
        total = sqrt(total)
        total = round(total, 1)
        total = str(total)
        step5 = 'b = %s' % total

        self.stepsLabel1['text'] = step1
        self.stepsLabel2['text'] = step2
        self.stepsLabel3['text'] = step3
        self.stepsLabel4['text'] = step4
        self.stepsLabel5['text'] = step5

        if leg_type == 1:
            self.firstLegEntry.delete(0, END)
            self.firstLegEntry.insert(END, total)

        elif leg_type == 2:
            self.secondLegEntry.delete(0, END)
            self.secondLegEntry.insert(END, total)


root = Tk()
PT_App(root)
root.mainloop()
