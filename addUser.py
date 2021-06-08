# add user form (in admin menubar): to add users by the admin

from tkinter import *
from tkinter import ttk
from expense_database import get_connection
from tkinter import messagebox
from tkcalendar import *
import datetime
from datetime import date

# defining a method to add users
def add_user(self, userid, username):
    # -------------- LOGIC ------------------
    def submit():
        self.user_id = self.entry_userid.get()
        self.user_name = self.entry_username.get()
        self.user_pwd = self.entry_pwd.get()
        # self.rr1 = self.rr1.get()
        # self.rr2 = self.rr2.get()
        self.date = self.entry_date.get()

        if self.user_id != "" and self.user_name != "" and self.user_pwd != "" and self.date != "" and self.rr1.get() !="" and self.rr2.get() != "":       # checking for empty text fields
            self.conn = get_connection()
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT userID FROM users WHERE userID=%s", (self.user_id,))
            self.id = self.cursor.fetchone()
            self.conn.commit()
            if self.id == None:          # checking for duplicate userID
                self.cursor.execute("INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s, %s)", (self.user_id, self.user_name, self.user_pwd, username, self.rr1.get(), self.rr2.get(), self.date_obj))
                self.conn.commit()

                # inserting the data into the tree view
                self.tree_view.insert('', 'end', values=(self.user_id, self.user_name, self.user_pwd, username, self.rr1.get(), self.rr2.get(), self.date_obj))
            else:
                messagebox.showinfo("WARNING!!","This userID is already taken....", icon='warning')
            self.cursor.close()
            self.conn.close()
        else:
            messagebox.showinfo("WARNING!!","Empty text field(s)...", icon='warning')

        # deleting the contents of text fields when "submit" button is clicked
        self.entry_userid.delete(0, END)
        self.entry_username.delete(0, END)
        self.entry_pwd.delete(0, END)

    # -------------- GUI -----------------
    # toplevel window to chnage username
    self.sub = Toplevel(self)
    self.sub.title("ADD USER WINDOW")
    self.sub.geometry("1450x700+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    # frame
    self.frame = Frame(self.sub)
    self.frame.grid(row=0, padx=25, pady=15, sticky=W)

    self.frame1 = Frame(self.sub)
    self.frame1.grid(row=1, padx=25, sticky=W)

    # ----------------- userid -------------------
    self.label_userid = Label(self.frame, text = "UserID : ", font=(None, 10))
    self.label_userid.grid(row=0, column=0, sticky=W)

    self.user_id = StringVar()
    self.entry_userid = Entry(self.frame, width=30, font=(None, 10), textvariable=self.user_id)
    self.entry_userid.grid(row=0, column=1, padx=20, pady=10, sticky='w')

    # ----------------- username -------------------
    self.label_username = Label(self.frame, text = "User name : ", font=(None, 10))
    self.label_username.grid(row=1, column=0, sticky=W)

    self.user_name = StringVar()
    self.entry_username = Entry(self.frame, width=30, font=(None, 10), textvariable=self.user_name)
    self.entry_username.grid(row=1, column=1, padx=20, pady=10, sticky='w')

    # ----------------- user password ------------------
    self.label_pwd = Label(self.frame, text = "Password : ", font=(None, 10))
    self.label_pwd.grid(row=3, column=0, sticky=W)

    self.user_pwd = StringVar()
    self.entry_pwd = Entry(self.frame, width=30, font=(None, 10), textvariable=self.user_pwd)
    self.entry_pwd.grid(row=3, column=1, padx=20, pady=10, sticky='w')

    # ----------------- user status --------------------
    self.label_userStatus = Label(self.frame, text = "User Status : ", font=(None, 10))
    self.label_userStatus.grid(row=4, column=0, pady=10, sticky=W)

    self.rr1 = StringVar()                                                               # radio button variable

    self.R1 = Radiobutton(self.frame, text="ENABLE", variable=self.rr1, value="enabled", font=(None, 10))
    self.R1.grid(row=4, column=1, padx=20, sticky=W)
    self.rr1.set("enabled")                                                              # setting radio button to a default value

    self.R2 = Radiobutton(self.frame, text="DISABLE", variable=self.rr1, value="disabled", font=(None, 10))
    self.R2.grid(row=4, column=1, padx=20, sticky=E)

    # -------------------- is admin -------------------------
    self.label_isAdmin = Label(self.frame, text = "The user is an admin : ", font=(None, 10))
    self.label_isAdmin.grid(row=5, column=0, pady=10, sticky=W)

    self.rr2 = StringVar()                                                               # radio button variable

    self.R3 = Radiobutton(self.frame, text="YES", variable=self.rr2, value="yes", font=(None, 10))
    self.R3.grid(row=5, column=1, padx=20, sticky=W)

    self.R4 = Radiobutton(self.frame, text="NO", variable=self.rr2, value="no", font=(None, 10))
    self.R4.grid(row=5, column=1, padx=20, sticky=E)
    self.rr2.set("no")                                                                   # setting radio button to a default value

    # ---------------------- date of when a user is added ----------------------------------
    self.label_date = Label(self.frame, text = "Date : ", font=(None, 10))
    self.label_date.grid(row=6, column=0, pady=10, sticky=W)

    self.date = StringVar()
    self.entry_date = DateEntry(self.frame, width=15, font=(None, 10),  textvariable=self.date)
    self.entry_date.grid(row=6, column=1, pady=10, padx=20, sticky='w')
    self.date = self.entry_date.get()
    self.date_obj = datetime.datetime.strptime(self.date, '%m/%d/%y').strftime('%Y-%m-%d')

    # ----------------------- button to submit all the entries ------------------------------
    self.submit_button = Button(self.frame, text='       SUBMIT      ', command=submit)
    self.submit_button.grid(row=7, column=0, padx=40, pady=15)

    # ----------------------- tree view -----------------------------
    self.tree_view = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="15")
    self.tree_view.grid(row=0, column=0, pady=10, sticky='w')

    self.tree_view.heading('#1', text="USER_ID")
    self.tree_view.heading('#2', text="USER_NAME")
    self.tree_view.heading('#3', text="PASSWORD")
    self.tree_view.heading('#4', text="ADMIN_NAME")
    self.tree_view.heading('#5', text="USER_STATUS")
    self.tree_view.heading('#6', text="IS_ADMIN")
    self.tree_view.heading('#7', text="DATE")

    self.scrollbar = Scrollbar(self.frame1, orient=VERTICAL, command=self.tree_view.yview)
    self.tree_view.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.grid(row=0, column=0, sticky=S + E + N)


    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    add_user(root, "amit")
