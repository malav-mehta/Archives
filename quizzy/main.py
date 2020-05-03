from tkinter import *
from tkinter import messagebox
from oauth2client.service_account import ServiceAccountCredentials
import gspread


class App:
    def __init__(self, master):
        self.master = master

        # designing the window
        w = 1200  # width for the Tk root
        h = 657  # height for the Tk root

        self.ws = master.winfo_screenwidth()  # width of the screen
        self.hs = master.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (self.ws/2) - (w/2)
        y = (self.hs/2) - (h/2)

        # set the dimensions of the window and where it will be placed
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.config(bg='white')
        master.title('QuiZZy')
        master.iconbitmap('./resources/logo.ico')

        # defining the inner organizations
        self.statusBar = Frame(master, width=1200, bg='white')
        self.statusBar.place(x=5, y=637)

        self.mainFrame = Frame(master, width=1200, height=625, bg='white')
        self.mainFrame.pack(side=TOP)

        # defining the scope creds and client variables (to access sheets)
        self.scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)

        # connecting to all sheets
        self.quizzList = self.client.open("available_quizzes").sheet1  # list of available quizzes
        self.authentication = self.client.open("quizzy_c1").sheet1  # spreadsheet with authentication information
        self.currentQuiz = ''  # current quiz that is open for either editing or actual quiz taking

        # to load the widgets
        self.clientLevel = 4
        self.loadWidgets()

        # a status bar
        self.actionLabel = Label(self.statusBar, text='connected to server', font=("Tahoma", 8), bg='white')
        self.actionLabel.pack(side=LEFT)

    def loadWidgets(self):
        self.mainFrame.destroy()  # removing current contents of the window
        self.mainFrame = Frame(self.master, width=1200, height=625, bg='white')
        self.mainFrame.pack(side=TOP)

        if self.clientLevel == 1:  # admin level
            self.adminWidgets()

        elif self.clientLevel == 2:  # teacher
            self.teacherWidgets()

        elif self.clientLevel == 3:  # student
            self.titleFrame = Frame(self.mainFrame, bg='white')
            self.titleFrame.place(x=10, y=10)

            self.Title = Label(self.titleFrame, text='QuiZZy', font=("Tahoma", 50, "bold"), fg='#002366', bg='white')
            self.Title.grid(row=0, column=0)

        elif self.clientLevel == 4:  # unauthenticated
            self.titleFrame = Frame(self.mainFrame, bg='white')
            self.titleFrame.place(x=10, y=10)

            self.Title = Label(self.titleFrame, text='QuiZZy', font=("Tahoma", 50, "bold"), fg='#002366', bg='white')
            self.Title.grid(row=0, column=0)

            self.authenticationFrame = Frame(self.mainFrame, bg='white')
            self.authenticationFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

            self.promptAuthentication = Label(self.authenticationFrame, text='Please sign in or create an account.', font=("Tahoma", 10), bg="white")
            self.promptAuthentication.grid(row=0, column=0)

            self.promptAuth = Button(self.authenticationFrame, text='Sign in/Create account', command=self.authenticationWindow, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0)
            self.promptAuth.grid(row=1, column=0)

    def adminWidgets(self):
        self.titleFrame = Frame(self.mainFrame, bg='white')
        self.titleFrame.place(x=10, y=10)

        self.Title = Label(self.titleFrame, text='QuiZZy', font=("Tahoma", 50, "bold"), fg='#002366', bg='white')
        self.Title.grid(row=0, column=0)

        self.loginOptions = Frame(self.mainFrame, bg='white')
        self.loginOptions.place(relx=0, rely=0, anchor=CENTER)

        self.client
        self.authenticateTeacher = Button(self.loginOptions, text='Authenticate as teacher', command=self.loadWidgets, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0)

    def teacherWidgets(self):
        self.titleFrame = Frame(self.mainFrame, bg='white')
        self.titleFrame.place(x=10, y=10)

        self.Title = Label(self.titleFrame, text='QuiZZy', font=("Tahoma", 50, "bold"), fg='#002366', bg='white')
        self.Title.grid(row=0, column=0)

        self.actionFrame = Frame(self.mainFrame, bg='white')
        self.actionFrame.place(x=18, y=115)

        self.actionIdentity1 = Label(self.actionFrame, text='Actions Panel', font=("Tahoma", 30, "bold"), bg='white')
        self.actionIdentity1.grid(row=0, column=0)

        self.createFrame = Frame(self.actionFrame, bg='white')
        self.createFrame.grid(row=1, column=0)

        self.createButton = Button(self.createFrame, bg='white', activebackground='white', relief=FLAT, bd=0)
        self.createButton.grid()

        self.createImage = PhotoImage(file="./resources/new_quiz.gif")
        self.createButton.config(image=self.createImage)

    def studentWidgets(self):


    def connectToSheet(self):
        self.sheet = self.client.open("quizzy_c1").sheet1
        self.statusLabel['text'] = 'connected'

        self.connectButton['text'] = 'disconnect'
        self.connectButton['command'] = self.disconnectFromSheet
        self.connectButton['fg'] = 'red'

    def disconnectFromSheet(self):
        self.sheet = ''
        self.statusLabel['text'] = 'disconnected'

        self.connectButton['text'] = 'connect'
        self.connectButton['command'] = self.connectToSheet
        self.connectButton['fg'] = 'green'

    def authenticate(self):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()

        try:
            self.id = self.authentication.find("%s" % self.email)

        except gspread.exceptions.CellNotFound:
            messagebox.showerror("Error", "email/username not found")

        self.passRow = self.id.row
        self.passCol = self.id.col + 1

        self.confirm = self.authentication.cell(self.passRow, self.passCol).value
        self.adminRow = self.passRow
        self.adminCol =  self.passCol + 1

        if self.confirm == self.password:
            self.clientLevel = self.authentication.cell(self.adminRow, self.adminCol).value
            self.clientLevel = int(self.clientLevel)

            self.actionLabel['text'] = ("latest action: sign-in has been completed")
            self.account.destroy()
            self.loadWidgets()

        elif self.confirm != self.password:
            messagebox.showerror("Error", "incorrect password")

    def loadAuthentication(self):
        self.options.place_forget()
        self.options2 = Frame(self.account, bg='white', relief=FLAT, bd=0)
        self.options2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.emailEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", relief=FLAT, bd=0)
        self.emailEntry.grid(row=0, column=0)
        self.emailEntry.insert(0, "email/username")

        self.passwordEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", show='●', relief=FLAT, bd=0)
        self.passwordEntry.grid(row=1, column=0)
        self.passwordEntry.insert(0, "password")

        self.submitLogin = Button(self.options2, text="Sign In", command=self.authenticate, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=1)
        self.submitLogin.grid(row=2, column=0)

    def addUser(self):
        try:
            x = self.emailEntry.get()
            y = self.authentication.find(x)
            messagebox.showerror("Error", "username already used")

        except gspread.exceptions.CellNotFound:
            if self.Level.get() == "Teacher":
                level = 2
                newUser = [self.emailEntry.get(), self.passwordEntry.get(), level, self.Class.get(), self.fNameEntry.get(), self.lNameEntry.get()]
                self.authentication.insert_row(newUser, 2)
                self.options.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.options2.place_forget()

            elif self.Level.get() == "Student":
                level = 3

                newUser = [self.emailEntry.get(), self.passwordEntry.get(), level, self.Class.get(), self.fNameEntry.get(), self.lNameEntry.get()]
                self.authentication.insert_row(newUser, 2)
                self.options.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.options2.place_forget()

            else:
                messagebox.showerror("Error", "account creation failed")

    def createAccountWindow(self):
        self.options.place_forget()
        self.options2 = Frame(self.account, bg='white')
        self.options2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.fNameEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", relief=FLAT, bd=0)
        self.fNameEntry.grid(row=0, column=0)
        self.fNameEntry.insert(0, "first name")

        self.lNameEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", relief=FLAT, bd=0)
        self.lNameEntry.grid(row=1, column=0)
        self.lNameEntry.insert(0, "last name")

        self.emailEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", relief=FLAT, bd=0)
        self.emailEntry.grid(row=2, column=0)
        self.emailEntry.insert(0, "email/username")

        self.passwordEntry = Entry(self.options2, font=("Tahoma", 10), bg="white", relief=FLAT, bd=0)
        self.passwordEntry.grid(row=3, column=0)
        self.passwordEntry.insert(0, "password")

        self.Level = StringVar(self.options2)
        choices = {'Teacher', 'Student'}
        self.Level.set("you are a:")

        self.Class = StringVar(self.options2)
        classes = ('1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D')
        self.Class.set("period: ")

        self.clientLevelRequest = OptionMenu(self.options2, self.Level, *choices)
        self.clientLevelRequest.config(font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0, highlightbackground='white')
        self.clientLevelRequest.grid(row=4, column=0)

        self.classRequest = OptionMenu(self.options2, self.Class, *classes)
        self.classRequest.config(font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0, highlightbackground='white')
        self.classRequest.grid(row=5, column=0)

        self.submitLogin = Button(self.options2, text="Create Account", command=self.addUser, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0)
        self.submitLogin.grid(row=6, column=0)

    def authenticationWindow(self):
        self.account = Tk()

        w = 400 # width for the Tk root
        h = 200 # height for the Tk root
        x = (self.ws/2) - (w/2)
        y = (self.hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        self.account.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.account.config(bg='white')
        self.account.title('Sign in')
        self.account.iconbitmap('./resources/logo.ico')

        self.options = Frame(self.account, bg='white')
        self.options.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.signIn = Button(self.options, text='Sign In', command=self.loadAuthentication, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0)
        self.signIn.pack()
        self.createAccount = Button(self.options, text='Create Account', command=self.createAccountWindow, font=("Tahoma", 10), bg="white", activebackground='white', relief=FLAT, bd=0)
        self.createAccount.pack()


def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
