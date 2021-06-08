from tkinter import *
from tkinter import ttk
from expense_database import get_connection
from tkinter import messagebox

def changePwdOfUser(self, userid):

    # search function
    def search():
        # checking for empty space
        if self.entry_search.get() == "":
            messagebox.showinfo("WARNING !! ", "WARNING: Search Entry is empty. Check again !!")
        else:
            self.conn = get_connection()
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM users WHERE userID = %s", (self.entry_search.get(),))                 
            self.records = self.cursor.fetchone()
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

            # for record in self.records:
            if self.records == None:
                messagebox.showinfo("INFO", "There is no user with that UserID!!")
            else:
                self.tree_view.insert('', 'end', values=(self.records[0], self.records[1], self.records[4], self.records[5]))
                
            self.entry_search.delete(0, END)    # to clear the search entry

    # to change password of a user
    def changePwd():

        # update button logic
        def update():

            # to get the selected items from the tree_view
            self.selected_items = self.tree_view.selection()

            if self.entry_newPwd.get() != "":                # to check if the text fields are empty or not
                self.conn = get_connection()
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT password FROM users WHERE userID=%s", (self.tree_view.set(self.selected_items, '#1'),))            
                self.p = self.cursor.fetchone()
                self.conn.commit()
                if self.p == None:
                    messagebox.showinfo("WARNING!!","No data selected form the table", icon='warning')
                else:
                    self.cursor.execute("UPDATE users SET password = %s WHERE userID=%s", (self.entry_newPwd.get(), self.tree_view.set(self.selected_items, '#1')))
                    self.conn.commit()
                self.cursor.close()
                self.conn.close()
                self.sub.destroy()
            else:
                messagebox.showinfo("WARNING!!","Empty text field(s)...", icon='warning')

        # edit popup window to edit the pwd of the selected user
        self.upadte_Window = Toplevel(self.sub)
        self.upadte_Window.title("UPDATE PASSWORD WINDOW")
        self.upadte_Window.geometry("520x100")
        self.upadte_Window.focus_force()
        self.upadte_Window.grab_set()
        self.upadte_Window.transient(self)

        self.frame = Frame(self.upadte_Window)
        self.frame.grid(row=0, padx=25, pady=15, sticky=W)

        self.label_newPwd = Label(self.frame, text="Enter a new password : ", font=(None, 10))
        self.label_newPwd.grid(row=0, column=0, sticky='w', pady=20)

        self.newPwd = StringVar()
        self.entry_newPwd = Entry(self.frame, width=30, font=(None, 10), textvariable=self.newPwd)
        self.entry_newPwd.grid(row=0, column=1, padx=10, sticky='w')

        self.button_update = Button(self.frame, text="UPDATE", command=update)
        self.button_update.grid(row=0, column=2, padx=30)


    # show all button logic
    def show_all():
        self.conn = get_connection()
        self.cursor = self.conn.cursor() 
        self.cursor.execute("SELECT userID, username, user_status, is_admin, password FROM users")                                              
        self.rows = self.cursor.fetchall()     # fetching all the contents of the tabe to insert in the new window tree view
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        # clearing tree view before displaying all the datas
        self.tree_view_records = self.tree_view.get_children()
        for item in self.tree_view_records:
            self.tree_view.delete(item)

        # inserts all the contents of the table into the tree_view_new
        for row in self.rows:
            self.tree_view.insert('', 'end', values=row)
        self.tree_view.insert('', 'end', values="")                    # to put a blank row in the tree view

    # clear screen button logic
    def clear_screen():
        self.tree_view_records = self.tree_view.get_children()
        for item in self.tree_view_records:
            self.tree_view.delete(item)

    # -------------- GUI -----------------
    # toplevel window to chnage username
    self.sub = Toplevel(self)
    self.sub.title("CHANGE PASSWORD OF A USER")
    self.sub.geometry("850x500+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    # --------------- frames -----------------
    self.frame = Frame(self.sub)
    self.frame.grid(row=0, padx=25, pady=15, sticky=W)

    self.frame1 = Frame(self.sub)
    self.frame1.grid(row=1, padx=25, sticky=W, columnspan=4)

    self.frame2 = Frame(self.sub)
    self.frame2.grid(row=2, padx=25, sticky=W)

    # --------------- search row (frame) ---------------
    self.label_searchby = Label(self.frame, text = "Enter the user's ID : ", font=(None, 10))
    self.label_searchby.grid(row=0, column=0, sticky=W, pady=10)

    # search entry
    self.entry_search = Entry(self.frame, width=30, font=(None, 10))
    self.entry_search.grid(row=0, column=2, padx=60, pady=10, sticky='w')

    # search button
    self.button_search = Button(self.frame, text='SEARCH', command=search)
    self.button_search.grid(row=0, column=3, padx=25, pady=10)

    # -------------------- tree view (frame1) ---------------------
    # treeview for the add form
    self.tree_view = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4), show="headings", height="15")
    self.tree_view.grid(row=0, column=0, pady=6, sticky='w')

    self.tree_view.heading('#1', text="USER_ID")
    self.tree_view.heading('#2', text="USER_NAME")
    self.tree_view.heading('#3', text="USER_STATUS")
    self.tree_view.heading('#4', text="IS_ADMIN")

    self.scrollbar = Scrollbar(self.frame1, orient=VERTICAL, command=self.tree_view.yview)
    self.tree_view.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.grid(row=0, column=0, sticky=S + E + N)

    #----------------------some buttons (frame2) ----------------------
    # button to show all the records - user list
    self.button_showall = Button(self.frame2, text='SHOW ALL', command=show_all)
    self.button_showall.grid(row=0, column=0, pady=30)

    # change pwd of a user button
    self.button_chngPwd = Button(self.frame2, text='CHANGE PASSWORD', command=changePwd)
    self.button_chngPwd.grid(row=0, column=2, pady=30, padx=200)

    # clear screen button
    self.button_clearScreen = Button(self.frame2, text='CLEAR SCREEN', command=clear_screen)
    self.button_clearScreen.grid(row=0, column=3, pady=30, sticky=E)

    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    changePwdOfUser(root, "amit")