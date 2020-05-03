from tkinter import *
from tkinter import messagebox
from oauth2client.service_account import ServiceAccountCredentials
import gspread


class MasterWindow:
    def __init__(self, master):
        # defining the window
        self.master = master

        # colors
        self.primary = "#003366"; self.secondary = "#e5e5e5"  # blue and white
        self.light = "#f4f4f4"; self.dark = "#838383"  # light and dark
        self.red = "#f53d3d"; self.green = "#009900"  # red and green
        self.regular = ("Tahoma", 10)

        # setting the window size
        w = 1000; h = 562  # height and width
        self.sw = master.winfo_screenwidth(); self.sh = master.winfo_screenheight();  # the screen dimensions
        x = (self.sw/2) - (w/2); y = (self.sh/2) - (h/2) # coordinates of the MasterWindow
        master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # configuring the window
        master.config(bg=self.light)
        master.title("QuiZZy")
        master.iconbitmap("./resources/logo.ico")

        # variables needed for authentication and sheet access
        self.scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)

        # connecting to spreadsheets
        self.authSheet = self.client.open("quizzy_a1").sheet1  # authenticates client
        self.quizzList = self.client.open("quizzy_aq1").sheet1  # available quizzes
        self.currentQuiz = ''  # current QuiZZy

        # grabbing needed photos
        self.assignQuizImage = PhotoImage(file="./resources/assign_quiz.gif")
        self.availableQuizzesImage = PhotoImage(file="./resources/available_quizzes.gif")
        self.controlSettingsImage = PhotoImage(file="./resources/control_settings.gif")
        self.createAccountImage = PhotoImage(file="./resources/create_account.gif")
        self.gradeQuizzesImage = PhotoImage(file="./resources/grade_quizzes.gif")
        self.manageStudentsImage = PhotoImage(file="./resources/manage_students.gif")
        self.newQuizImage = PhotoImage(file="./resources/new_quiz.gif")
        self.signInImage = PhotoImage(file="./resources/sign_in.gif")
        self.signOutImage = PhotoImage(file="./resources/sign_out.gif")

        # loading all widgets
        self.clientLevel = 0
        self.clientClass = None
        self.clientName = StringVar()
        self.latestAction = StringVar()

        self.latestAction.set("not authenticated")
        self.clientName.set("please sign in/create account")

        self.loadWidgets()

    def loadWidgets(self):
        # design elements
        primary = self.primary; secondary = self.secondary  # blue and
        white
        light = self.light; dark = self.dark  # light and dark
        red = self.red; green = self.green  # red and green
        regular = self.regular

        # master frame containing all principal widgets
        self.mainFrame = Frame(self.master, width=593, height=542, bg=light)
        self.mainFrame.place(x=0, y=0)

        # the title bar
        self.titleFrame = Frame(self.mainFrame, bg=light)
        self.titleFrame.grid(row=0, column=0)
        self.Title = Label(self.titleFrame, text="QuiZZy", font=("Tahoma", 45, "bold"), fg=primary, bg=light)
        self.Title.pack()

        # authentication section
        self.loginFrame = Frame(self.master, bg=light, width=400, height=150)
        self.loginFrame.place(x=750, y=20)
        self.loggedInLabel = Label(self.loginFrame, textvariable=self.clientName, font=regular, fg=primary, bg=light)
        self.loggedInLabel.grid(row=0, column=0)

        self.options = Frame(self.loginFrame, bg=light)
        self.options.grid(row=1, column=0)

        self.statusBar = Frame(self.master, width=1000, height=9, bg=light)
        self.statusBar.place(x=4, y=542)
        self.actionLabel = Label(self.statusBar, textvariable=self.latestAction, font=("Tahoma", 8), fg=dark, bg=secondary)
        self.actionLabel.pack(side=LEFT)

        if self.clientLevel ==  0:  # unauthenticated client
            self.signIn = Button(self.options, command=self.loadAuthentication, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.signIn.configure(image=self.signInImage)
            self.signIn.grid(row=0, column=0)

            self.createAccount = Button(self.options, command=self.loadAccountCreation, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.createAccount.configure(image=self.createAccountImage)
            self.createAccount.grid(row=0, column=1)

        if self.clientLevel == 1:  # client level = student
            None

        if self.clientLevel == 2:  # client level = teacher
            self.loginFrame.place_forget()
            self.loginFrame.place(x=840, y=20)

            vFactor = 12
            hFactor = 10

            self.signOut = Button(self.options, command=self.unathenticate, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.signOut.configure(image=self.signOutImage)
            self.signOut.pack()

            self.actionsPanel = Frame(self.master, width=633, height=274)
            self.actionsPanel.place(x=5, y=100)
            self.topActions = Frame(self.actionsPanel, height=127)
            self.topActions.grid(row=0, column=0)
            self.separator = Frame(self.actionsPanel, height=vFactor)
            self.separator.grid(row=1, column=0)
            self.bottomActions = Frame(self.actionsPanel, height=127)
            self.bottomActions.grid(row=2, column=0)

            self.separator13 = Frame(self.topActions, bg=light, width=(hFactor * 1)).grid(row=0, column=0)

            self.newQuiz = Button(self.topActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.newQuiz.config(image=self.newQuizImage)
            self.newQuiz.grid(row=0, column=1)

            self.separator9 = Frame(self.topActions, bg=light, width=(hFactor * 1.1)).grid(row=0, column=2)

            self.manageStudents = Button(self.topActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.manageStudents.config(image=self.manageStudentsImage)
            self.manageStudents.grid(row=0, column=3)

            self.separator10 = Frame(self.topActions, bg=light, width=(hFactor * 0.5)).grid(row=0, column=4)

            self.controlSettings = Button(self.topActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.controlSettings.config(image=self.controlSettingsImage)
            self.controlSettings.grid(row=0, column=5)

            self.assignQuiz = Button(self.bottomActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.assignQuiz.config(image=self.assignQuizImage)
            self.assignQuiz.grid(row=0, column=0)

            self.separator11 = Frame(self.bottomActions, bg=light, width=(hFactor * 0.6)).grid(row=0, column=1)

            self.availableQuizzes = Button(self.bottomActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.availableQuizzes.config(image=self.availableQuizzesImage)
            self.availableQuizzes.grid(row=0, column=2)

            self.separator12 = Frame(self.bottomActions, bg=light, width=hFactor).grid(row=0, column=3)

            self.gradePastQuizzes = Button(self.bottomActions, bg=light, activebackground=light, relief=FLAT, bd=0)
            self.gradePastQuizzes.config(image=self.gradeQuizzesImage)
            self.gradePastQuizzes.grid(row=0, column=4)

        if self.clientLevel == 3: # client level == admin
            None

    def loadAuthentication(self):
        self.signIn.grid_forget()
        self.createAccount.grid_forget()

        self.authenticationFrame = Frame (self.master, bg=self.light)
        self.authenticationFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.emailEntry = Entry(self.authenticationFrame, font=self.regular, fg = self.dark, bg=self.secondary, relief=FLAT, bd=0)
        self.emailEntry.grid(row=0, column=0)
        self.emailEntry.insert(0, "email")

        self.separator7 = Frame(self.authenticationFrame, bg=self.light, height=2).grid(row=1, column=0)

        self.passwordEntry = Entry(self.authenticationFrame, font=self.regular, fg=self.dark, bg=self.secondary, show='●', relief=FLAT, bd=0)
        self.passwordEntry.grid(row=2, column=0)
        self.passwordEntry.insert(0, "password")

        self.separator8 = Frame(self.authenticationFrame, bg=self.light, height=2).grid(row=3, column=0)

        self.submitLogin = Button(self.authenticationFrame, command=self.authenticateClient, bg=self.light, activebackground=self.light, relief=FLAT, bd=0)
        self.submitLogin.configure(image=self.signInImage)
        self.submitLogin.grid(row=4, column=0)

    def authenticateClient(self):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()

        try:
            self.id = self.authSheet.find("%s" % self.email)

        except gspread.exceptions.CellNotFound:
            messagebox.showerror("Error", "email/username not found")

        self.clientRow = self.id.row
        self.passCol = self.id.col + 1
        self.levelCol = self.passCol + 1
        self.classCol = self.levelCol + 1
        self.fNameCol = self.classCol + 1
        self.lNameCol = self.fNameCol + 1

        self.confirm = self.authSheet.cell(self.clientRow, self.passCol).value

        if self.confirm == self.password:
            self.clientLevel = self.authSheet.cell(self.clientRow, self.levelCol).value
            self.clientClass = self.authSheet.cell(self.clientRow, self.classCol).value
            self.firstName = self.authSheet.cell(self.clientRow, self.fNameCol).value
            self.lastName = self.authSheet.cell(self.clientRow, self.lNameCol).value

            self.clientLevel = int(self.clientLevel)
            self.clientName.set((self.firstName, self.lastName))
            self.latestAction.set("latest action: sign-in has been completed")
            self.authenticationFrame.destroy()
            self.loadWidgets()

        elif self.confirm != self.password:
            messagebox.showerror("Error", "incorrect password")

    def loadAccountCreation(self):
        self.signIn.destroy()
        self.createAccount.destroy()

        self.newAccountFrame = Frame (self.master, bg=self.light)
        self.newAccountFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.fNameEntry = Entry(self.newAccountFrame, font=self.regular, fg=self.dark, bg=self.secondary, relief=FLAT, bd=0)
        self.fNameEntry.grid(row=0, column=0)
        self.fNameEntry.insert(0, "first name")

        self.separator1 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=1, column=0)

        self.lNameEntry = Entry(self.newAccountFrame, font=self.regular, fg=self.dark, bg=self.secondary, relief=FLAT, bd=0)
        self.lNameEntry.grid(row=2, column=0)
        self.lNameEntry.insert(0, "last name")

        self.separator2 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=3, column=0)

        self.emailEntry = Entry(self.newAccountFrame, font=self.regular, fg=self.dark, bg=self.secondary, relief=FLAT, bd=0)
        self.emailEntry.grid(row=4, column=0)
        self.emailEntry.insert(0, "email")

        self.separator3 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=5, column=0)

        self.passwordEntry = Entry(self.newAccountFrame, font=self.regular, fg=self.dark, bg=self.secondary, relief=FLAT, bd=0)
        self.passwordEntry.grid(row=6, column=0)
        self.passwordEntry.insert(0, "password")

        self.separator4 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=7, column=0)

        self.Level = StringVar(self.newAccountFrame)
        choices = {'Teacher', 'Student'}
        self.Level.set("you are a:")

        self.Class = StringVar(self.newAccountFrame)
        classes = ('1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D')
        self.Class.set("period: ")

        self.clientLevelRequest = OptionMenu(self.newAccountFrame, self.Level, *choices)
        self.clientLevelRequest.config(font=self.regular, fg=self.dark, bg=self.secondary, activebackground=self.secondary, relief=FLAT, bd=0, highlightbackground=self.secondary)
        self.clientLevelRequest.grid(row=8, column=0)

        self.separator5 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=9, column=0)

        self.classRequest = OptionMenu(self.newAccountFrame, self.Class, *classes)
        self.classRequest.config(font=self.regular, fg=self.dark, bg=self.secondary, activebackground=self.secondary, relief=FLAT, bd=0, highlightbackground=self.secondary)
        self.classRequest.grid(row=10, column=0)

        self.separator6 = Frame(self.newAccountFrame, bg=self.light, height=2).grid(row=11, column=0)

        self.submitLogin = Button(self.newAccountFrame, command=self.addUser, font=self.regular, fg=self.dark, bg=self.light, activebackground=self.light, relief=FLAT, bd=0)
        self.submitLogin.config(image=self.createAccountImage)
        self.submitLogin.grid(row=12, column=0)

    def addUser(self):
        try:
            x = self.emailEntry.get()
            y = self.authSheet.find(x)
            messagebox.showerror("Error", "email already used")

        except gspread.exceptions.CellNotFound:
            if self.Level.get() == "Teacher":
                level = 2
                newUser = [self.emailEntry.get(), self.passwordEntry.get(), level, self.Class.get(), self.fNameEntry.get(), self.lNameEntry.get()]
                self.authSheet.insert_row(newUser, 2)
                self.newAccountFrame.destroy()
                self.loadWidgets()
                self.latestAction.set((self.fNameEntry.get(), self.lNameEntry.get() + "'s account has been created, please login"))

            elif self.Level.get() == "Student":
                level = 3
                newUser = [self.emailEntry.get(), self.passwordEntry.get(), level, self.Class.get(), self.fNameEntry.get(), self.lNameEntry.get()]
                self.authSheet.insert_row(newUser, 2)
                self.newAccountFrame.destroy()
                self.loadWidgets()
                self.latestAction.set((self.fNameEntry.get(), self.lNameEntry.get() + "'s account has been created, please login"))

            else:
                messagebox.showerror("Error", "account creation failed")

    def unathenticate(self):
            self.clientLevel = 0
            self.clientClass = None
            self.clientName = StringVar()
            self.latestAction = StringVar()

            self.latestAction.set("")
            self.latestAction.set("not authenticated")
            self.clientName.set("please sign in/create account")
            self.actionsPanel.place_forget()

            self.loadWidgets()


def main():
    root = Tk()
    MasterWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
