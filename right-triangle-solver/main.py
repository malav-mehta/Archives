from tkinter import *
from tkinter import messagebox
from math import *


class Application:
    def __init__(self, master):
        theme = '#333333'
        inverse = '#afafaf'
        button = '#4d4d4d'

        self.master = master
        master.title('Right Triangle Solver')
        master.iconbitmap(r'logo.ico')

        master.geometry('800x500')
        master.configure(bg=theme)

        self.inputFrame = Frame(master, width=400, bg=theme)
        self.outputFrame = Frame(master, width=400, height=500, bg=theme)
        self.outputFrame.grid_propagate(False)

        self.imageFrame = Frame(self.inputFrame, bg=theme)
        self.entryFrame = Frame(self.inputFrame, bg=theme)

        self.inputFrame.grid(row=0, column=0)
        self.outputFrame.grid(row=0, column=1)
        self.imageFrame.pack(side='top')
        self.entryFrame.pack(side='bottom')

        self.rightTriangle = PhotoImage(file='right_triangle.gif')
        self.rightTriangleLabel = Label(self.imageFrame, image=self.rightTriangle, bg=theme, fg=inverse)

        self.rightTriangleLabel.image = self.rightTriangle
        self.rightTriangleLabel.pack(side='top')
        self.space1 = Label(self.imageFrame, bg=theme, fg=inverse, text='\t', font=('Arial', 5)).pack(side=BOTTOM)

        self.entryText1 = StringVar(self.entryFrame, value='unknown')
        self.entryText2 = StringVar(self.entryFrame, value='unknown')
        self.entryText3 = StringVar(self.entryFrame, value='unknown')
        self.entryText4 = StringVar(self.entryFrame, value='unknown')
        self.entryText5 = StringVar(self.entryFrame, value='unknown')

        self.Leg1Label = Label(self.entryFrame, text='Leg1 (a)\t', bg=theme, fg=inverse)
        self.Leg1Entry = Entry(self.entryFrame, bg=theme, textvariable=self.entryText2, fg=inverse)

        self.Leg2Label = Label(self.entryFrame, text='Leg2 (b)\t', bg=theme, fg=inverse)
        self.Leg2Entry = Entry(self.entryFrame, bg=theme, textvariable=self.entryText3, fg=inverse)

        self.hypLabel = Label(self.entryFrame, text='Hyp (c)\t', bg=theme, fg=inverse)
        self.hypEntry = Entry(self.entryFrame, bg=theme, textvariable=self.entryText1, fg=inverse)

        self.angleCLabel = Label(self.entryFrame, text='Ang C\t', bg=theme, fg=inverse)
        self.angleCLabel2 = Label(self.entryFrame, text='90', bg=theme, fg=inverse)

        self.angleALabel = Label(self.entryFrame, text='Ang A\t', bg=theme, fg=inverse)
        self.angleAEntry = Entry(self.entryFrame, bg=theme, textvariable=self.entryText5, fg=inverse)

        self.angleBLabel = Label(self.entryFrame, text='Ang B\t', bg=theme, fg=inverse)
        self.angleBEntry = Entry(self.entryFrame, bg=theme, textvariable=self.entryText4, fg=inverse)

        self.submitButton = Button(self.entryFrame, bg='#003972', text='Submit', command=self.run, fg=inverse)
        self.resetButton = Button(self.entryFrame, bg=button, text='  R̲̲eset  ', command=self.resetValues, fg=inverse)
        self.copyButton = Button(self.entryFrame, bg=button, text='  C̲opy  ', fg=inverse, command=self.copyFinalAnswer)
        self.quitButton = Button(self.entryFrame, bg='#720000', text='   Q̲uit   ', command=master.destroy, fg=inverse)

        # Griding Items
        self.Leg1Label.grid(row=0, column=0)
        self.Leg1Entry.grid(row=0, column=1)

        self.Leg2Label.grid(row=1, column=0)
        self.Leg2Entry.grid(row=1, column=1)

        self.hypLabel.grid(row=2, column=0)
        self.hypEntry.grid(row=2, column=1)

        self.angleALabel.grid(row=3, column=0)
        self.angleAEntry.grid(row=3, column=1)

        self.angleBLabel.grid(row=4, column=0)
        self.angleBEntry.grid(row=4, column=1)

        self.angleCLabel.grid(row=5, column=0)
        self.angleCLabel2.grid(row=5, column=1)

        self.space2 = Label(self.entryFrame, bg=theme, fg=inverse, text='\t\t', font=('Arial', 6)).grid(row=2, column=2)
        self.space3 = Label(self.entryFrame, bg=theme, fg=inverse, text='\t\t', font=('Arial', 6)).grid(row=3, column=2)

        self.submitButton.grid(row=2, column=3)
        self.resetButton.grid(row=3, column=3)
        self.space5 = Label(self.entryFrame, bg=theme, fg=inverse, text='\t', font=('Arial', 6)).grid(row=3, column=4)
        self.copyButton.grid(row=2, column=5)
        self.quitButton.grid(row=3, column=5)

        self.answer2 = StringVar(self.outputFrame)
        self.output = Text(self.outputFrame, bg=theme, width=400, height=500, fg=inverse, font=('Cambria', 11))
        self.output.grid()

        self.resetValues()
        self.master.bind('<r>', self.resetValuesKey)
        self.master.bind('<Return>', self.runKey)
        self.master.bind('<c>', self.copyFinalAnswerKey)
        self.master.bind('<q>', self.killApp)

    def killApp(self, event):
        self.master.destroy()

    def copyFinalAnswer(self):
        finalAnswer = str(self.answer2.get())
        master = self.master

        master.clipboard_clear()
        master.clipboard_append(finalAnswer)
        master.update()

    def copyFinalAnswerKey(self,event):
        finalAnswer = str(self.answer2.get())
        master = self.master

        master.clipboard_clear()
        master.clipboard_append(finalAnswer)
        master.update()

    def runKey(self, event):
        self.output.delete('1.0', END)
        self.output.insert(END, 'Calculating...')
        self.master.after(800, self.logic)

    def run(self):
        self.output.delete('1.0', END)
        self.output.insert(END, 'Calculating...')
        self.master.after(800, self.logic)

    def resetValuesKey(self, event):
        self.angleAEntry.delete(0, END)
        self.angleBEntry.delete(0, END)
        self.Leg1Entry.delete(0, END)
        self.Leg2Entry.delete(0, END)
        self.hypEntry.delete(0, END)
        # .insert(END, 'unknown')
        self.angleAEntry.insert(END, 'unknown')
        self.angleBEntry.insert(END, 'unknown')
        self.Leg1Entry.insert(END, 'unknown')
        self.Leg2Entry.insert(END, 'unknown')
        self.hypEntry.insert(END, 'unknown')

        self.output.delete('1.0', END)
        self.output.insert(END, 'Please enter values...')

    def resetValues(self):
        self.angleAEntry.delete(0, END)
        self.angleBEntry.delete(0, END)
        self.Leg1Entry.delete(0, END)
        self.Leg2Entry.delete(0, END)
        self.hypEntry.delete(0, END)
        # .insert(END, 'unknown')
        self.angleAEntry.insert(END, 'unknown')
        self.angleBEntry.insert(END, 'unknown')
        self.Leg1Entry.insert(END, 'unknown')
        self.Leg2Entry.insert(END, 'unknown')
        self.hypEntry.insert(END, 'unknown')

        self.output.delete('1.0', END)
        self.output.insert(END, 'Please enter values...')

    def deleteValue(self):
        self.angleAEntry.delete(0, END)
        self.angleBEntry.delete(0, END)
        self.Leg1Entry.delete(0, END)
        self.Leg2Entry.delete(0, END)
        self.hypEntry.delete(0, END)

    def answer(self, ans1, ans2, ans3, a, b, c, A, B):
        self.output.delete('1.0', END)

        finalAnswer = '%s\n%s\n%s\n' % (ans1, ans2, ans3)
        self.output.insert(END, finalAnswer)
        self.answer2.set(finalAnswer)

        self.angleAEntry.delete(0, END)
        self.angleBEntry.delete(0, END)
        self.Leg1Entry.delete(0, END)
        self.Leg2Entry.delete(0, END)
        self.hypEntry.delete(0, END)
        # .insert(END, 'unknown')
        self.angleAEntry.insert(END, str(A))
        self.angleBEntry.insert(END, str(B))
        self.Leg1Entry.insert(END, str(a))
        self.Leg2Entry.insert(END, str(b))
        self.hypEntry.insert(END, str(c))

    def logic(self):
        A = self.angleAEntry.get()
        B = self.angleBEntry.get()
        C = 90

        a = self.Leg1Entry.get()
        b = self.Leg2Entry.get()
        c = self.hypEntry.get()

        if A == 'unknown':
            A = 0

        if B == 'unknown':
            B = 0

        if a == 'unknown':
            a = 0

        if b == 'unknown':
            b = 0

        if c == 'unknown':
            c = 0

        a, b, c, A, B = float(a), float(b), float(c), float(A), float(B)

        if a + b + c + A + B == 0 or a + b + c == 0 or A >= 90 or B >= 90:
            messagebox.showinfo('Error', 'Invalid Input')
            self.deleteValue()
            self.resetValues()
            self.output.delete('1.0', END)
            self.output.insert(END, 'Invalid input...\n\nWaiting for new values...')

        elif a < 0 or b < 0 or c < 0 or A < 0 or B < 0:
            messagebox.showinfo('Error', 'Invalid Input')
            self.deleteValue()
            self.resetValues()
            self.output.delete('1.0', END)
            self.output.insert(END, 'Invalid input...\n\nWaiting for new values...')

        elif c != 0:
            if b >= c:
                messagebox.showinfo('Error', 'Invalid Input')
                self.deleteValue()
                self.resetValues()
                self.output.delete('1.0', END)
                self.output.insert(END, 'Invalid input...\n\nWaiting for new values...')

            elif a >= c:
                messagebox.showinfo('Error', 'Invalid Input')
                self.deleteValue()
                self.resetValues()
                self.output.delete('1.0', END)
                self.output.insert(END, 'Invalid input...\n\nWaiting for new values...')


        else:
            if c + A + B == 0:
                a, b = float(a), float(b)
                c, ans1 = self.solveLastSide(0, a, b)
                A, ans2 = self.angleTan(a, b, 'A')
                B, ans3 = self.solveAngle(A, 'B')

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif b + A + B == 0:
                a, c = float(a), float(c)
                b, ans1 = self.solveLastSide(1, a, c)
                A, ans2 = self.angleSin(a, c, 'A')
                B, ans3 = self.solveAngle(A, 'B')

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif a + A + B == 0:
                c, b = float(c), float(b)
                a, ans1 = self.solveLastSide(1, b, c)
                A, ans2 = self.angleCos(b, c, 'A')
                B, ans3 = self.solveAngle(A, 'B')

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif b + c + B == 0:
                a, A = float(a), float(A)
                B, ans1 = self.solveAngle(A, 'B')
                b, ans2 = self.sideTan(a, B, 'b')
                c, ans3 = self.solveLastSide(0, a, b)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif b + A + c == 0:
                a, B = float(a), float(B)
                A, ans1 = self.solveAngle(B, 'A')
                b, ans2 = self.sideTan(a, B, 'b')
                c, ans3 = self.solveLastSide(0, a, b)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif a + c + B == 0:
                A, b = float(A), float(b)
                B, ans1 = self.solveAngle(A, 'B')
                a, ans2 = self.sideTan(b, A, 'a')
                c, ans3 = self.solveLastSide(0, a, b)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif a + A + c == 0:
                B, b = float(B), float(b)
                A, ans1 = self.solveAngle(B, 'A')
                a, ans2 = self.sideTan(b, A, 'a')
                c, ans3 = self.solveLastSide(0, a, b)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif a + b + B == 0:
                c, A = float(c), float(A)
                B, ans1 = self.solveAngle(A, 'B')
                b, ans2 = self.sideSin(c, A, 'a', 'A')
                print(a, b, c, A, B)
                a, ans3 = self.solveLastSide(1, b, c)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

            elif a + A + b == 0:
                c, B = float(c), float(B)
                A, ans1 = self.solveAngle(B, 'A')
                b, ans2 = self.sideSin(c, B, 'a', 'B')
                a, ans3 = self.solveLastSide(1, b, c)

                self.answer(ans1, ans2, ans3, a, b, c, A, B)

    def solveAngle(self, ang1, label):
        newAngle = round(90 - ang1, 2)
        finalAnswer = '%s = 180 - 90 - %s\n%s = %s\n' % (label, ang1, label, newAngle)
        return newAngle, finalAnswer

    def solveLastSide(self, type, s1, s2):
        if type == 0:
            leg = s1
            leg2 = s2

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
            total = round(total, 2)
            total = str(total)
            step5 = 'c = %s' % total

            finalAnswer = '%s\n%s\n%s\n%s\n%s\n' % (step1, step2, step3, step4, step5)
            return total, finalAnswer

        if type == 1:
            leg = s1
            hyp = s2

            step1 = "c² - a² = b² (Pythagoras Theorem)"
            step2 = '%s² - %s² = b²' % (str(hyp), str(leg))

            hyp = hyp ** 2
            leg = leg ** 2
            step3 = '%s - %s = b²' % (str(hyp), str(leg))

            total = hyp - leg
            total1 = str(total)
            step4 = '%s = b²' % total1

            total = sqrt(total)
            total = round(total, 2)
            total = str(total)
            step5 = 'b = %s' % total

            finalAnswer = '%s\n%s\n%s\n%s\n%s\n' % (step1, step2, step3, step4, step5)
            return total, finalAnswer

    def sideTan(self, adj, ang, side):
        angle = str(ang)
        step1 = 'tan%s = opp ÷ adj' % angle
        step2 = '%s = %stan%s' % (side, adj, ang)
        total = round(adj*(tan(radians(ang))), 3)

        step3 = '%s = %s' % (side, total)
        finalAnswer = '%s\n%s\n%s\n' % (step1, step2, step3)
        return total, finalAnswer

    def sideSin(self, hyp, ang, side, angle):
        step1 = 'sin%s = opp ÷ hyp' % angle
        step2 = '%s = %ssin%s' % (side, hyp, ang)
        total = round(hyp*(sin(radians(ang))), 3)

        step3 = '%s = %s' % (side, total)
        finalAnswer = '%s\n%s\n%s\n' % (step1, step2, step3)
        return total, finalAnswer

    def angleTan(self, opp, adj, angle):
        step1 = 'tan%s = opp ÷ adj' % angle
        step2 = '%s = tan(-1) x opp ÷ adj' % angle
        total = round(degrees(atan(opp / adj)), 2)

        step3 = "%s = %s" % (angle, total)
        finalAnswer = '%s\n%s\n%s\n' % (step1, step2, step3)
        return total, finalAnswer

    def angleSin(self, opp, hyp, angle):
        step1 = 'tan%s = opp ÷ hyp' % angle
        step2 = '%s = tan(-1) x opp ÷ hyp' % angle
        total = round(degrees(asin(opp / hyp)), 3)

        step3 = "%s = %s" % (angle, total)
        finalAnswer = '%s\n%s\n%s\n' % (step1, step2, step3)
        return total, finalAnswer

    def angleCos(self, adj, hyp, angle):
        step1 = 'tan%s = adj ÷ hyp' % angle
        step2 = '%s = tan(-1) x adj ÷ hyp' % angle
        total = round(degrees(acos(adj / hyp)), 3)

        step3 = "%s = %s" % (angle, total)
        finalAnswer = '%s\n%s\n%s\n' % (step1, step2, step3)
        return total, finalAnswer


if __name__ == '__main__':
    RightTriangleSolver = Tk()
    Application(RightTriangleSolver)
    RightTriangleSolver.mainloop()
