from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox

from main_window import MainWindow
from expense_database import get_connection

class Login(Frame):
    '''
    Login form
    '''
    def __init__(self, master=None):
        '''
        Initialize frame
        '''
        Frame.__init__(self, master)
        self.grid()

        self.master.title('Login')

        self.winLabel = Label(master, text="LOGIN", font=(None, 10))
        self.winLabel.grid(row=0, column=0, padx=40, pady=5)
        
        self.winLabel = Label(master)
        self.winLabel.grid(row=1, column=0)        

        self.nunameLabel = Label(master, text="UserID", font=(None, 10))
        self.nunameLabel.grid(row=2, column=0, padx=40)

        self.nuname = StringVar()
        self.nunameEntry = Entry(master, textvariable=self.nuname, font=(None, 10))
        self.nunameEntry.grid(row=3, column=0, padx=40, pady=5)
                        
        self.npwdLabel = Label(master, text="Password", font=(None, 10))
        self.npwdLabel.grid(row=4, column=0, padx=40)

        self.npwd = StringVar()
        self.npwdEntry = Entry(master, show='*', textvariable=self.npwd, font=(None, 10))
        self.npwdEntry.grid(row=5, column=0, padx=40, pady=5)               

        self.button_submit = Button(master, text = "     LOGIN     ", command=self.openMainWindow)
        self.button_submit.grid(row = 6, column = 0, padx=40, pady=25)

    def signin(self):
        self.nuname = self.nunameEntry.get()
        self.npwd = self.npwdEntry.get()
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM users WHERE userID = %s AND password = %s ", (self.nuname, self.npwd))
        self.user_info = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        if self.nuname != "" and self.npwd != "":
            if self.user_info[0] == self.nuname and self.user_info[2] == self.npwd:
                if self.user_info[4] == "enabled":
                    self.master.destroy()
                    mainroot = Tk()
                    # set size of main window in maximize state
                    # mainroot.state('zoomed')
                    mainroot.attributes('-zoomed', True)
                    MainWindow(mainroot, self.user_info[5], self.nuname, self.user_info[1])
                    print(self.user_info[5])
                    mainroot.mainloop()
                else:
                    messagebox.showinfo("WARNING!!","SORRY!! Yor account has been deleted by the ADMIN", icon='warning')
            else:
                messagebox.showinfo("WARNING!!","SORRY!! Incorrect UserID or Password, check again....", icon='warning')
        else:
            messagebox.showinfo("WARNING!!","Enter your username and password", icon='warning')


    def openMainWindow(self):
        '''
        openMainWindow function closes login window and opens main window
        '''
        self.signin()
  

# main methods start the program
if __name__ == '__main__':
    loginRoot = Tk()
    # set default size
    loginRoot.geometry("230x240+300+300")
    # disable maximize option
    loginRoot.resizable(0,0)
    # set position in middle of screen
    loginRoot.eval('tk::PlaceWindow . center')
    lg = Login(loginRoot)
    # loginRoot.mainloop()
    lg.mainloop()

