from tkinter import *
from tkinter.ttk import *
import sys
from addForm import add_subWindow
from editForm import edit_subWindow
from searchForm import search_subWindow
from deleteForm import delete_subWindow
from updateUsername import update_username
from changePwd import update_pwd
from addUser import add_user
from desableUserForm import disable_user
from changePwdOfUser import changePwdOfUser
from mainWindowContents import graph

class MainWindow(Frame):
    '''
    main window with menu bar
    '''
    def __init__(self, master=None, isAdmin=None, userid="", username=""):
        Frame.__init__(self, master)
        self.grid()
        self.isAdmin = isAdmin
        self.userid=userid
        self.username = username

        self.master.title('Main Window')

        # menubar
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        # file menu
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        # expense menu
        self.expenseMenu = Menu(self.menubar, tearoff=0)
        self.expenseMenu.add_command(label="Add", command=self.call_addWindow)
        self.expenseMenu.add_command(label="Edit", command=self.call_editWindow)
        self.expenseMenu.add_command(label="Search", command=self.call_searchWindow)
        self.expenseMenu.add_command(label="Delete", command=self.call_deleteWindow)
        self.menubar.add_cascade(label="Expense", menu=self.expenseMenu)

        # report menu
        self.reportMenu = Menu(self.menubar, tearoff=0)
        self.reportMenu.add_command(label="Last week report", command="")
        self.reportMenu.add_command(label="Last month report", command="")
        self.reportMenu.add_command(label="Last six month report", command="")
        self.reportMenu.add_command(label="Last twelve month report", command="")
        self.menubar.add_cascade(label="Report", menu=self.reportMenu)

        # user menu
        self.userMenu = Menu(self.menubar, tearoff=0)
        self.userMenu.add_command(label="Update username", command=self.call_updateUsername)
        self.userMenu.add_command(label="Update profile pic", command="")
        self.userMenu.add_command(label="Change password", command=self.call_updatePwd)
        self.menubar.add_cascade(label="User", menu=self.userMenu)

        if isAdmin == "yes":
            # admin menu
            self.adminMenu = Menu(self.menubar, tearoff=0)
            self.adminMenu.add_command(label="Add user", command=self.call_addUser)
            self.adminMenu.add_command(label="Enable/Desable user", command=self.call_disableUser)
            self.adminMenu.add_command(label="Change password of a user", command=self.call_changepwdofuser)
            self.menubar.add_cascade(label="Admin", menu=self.adminMenu)

        # help menu
        self.helpMenu = Menu(self.menubar, tearoff=0)
        self.helpMenu.add_command(label="About", command="")
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)

        # self.call_mainWindowContents()

    def call_addWindow(self):
        add_subWindow(self, self.userid)

    def call_editWindow(self):
        edit_subWindow(self, self.userid)

    def call_searchWindow(self):
        search_subWindow(self, self.userid)

    def call_deleteWindow(self):
        delete_subWindow(self, self.userid)

    def call_updateUsername(self):
        update_username(self, self.userid)

    def call_updatePwd(self):
        update_pwd(self, self.userid)

    def call_addUser(self):
        add_user(self, self.userid, self.username)

    def call_disableUser(self):
        disable_user(self, self.userid, self.username)

    def call_changepwdofuser(self):
        changePwdOfUser(self, self.userid)

    def call_mainWindowContents(self):
        graph(self, self.userid)


    def onExit(self):
        '''
        on click exit close window and exit
        '''        
        self.master.destroy()


# to check the main window indivisually
if __name__ == '__main__':    
    root = Tk()
    root.state('zoomed')
    guiFrame = MainWindow(root)    
    guiFrame.mainloop()