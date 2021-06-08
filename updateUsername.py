from tkinter import *
from tkinter import ttk
from expense_database import get_connection
from tkinter import messagebox

def update_username(self, userid):

    # function to change the username
    def new_username():
        if self.entry_newUsername.get() != "" or self.entry_pwd.get() != "":                # to check if the text fields are empty or not
            self.conn = get_connection()
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT password FROM users WHERE userID=%s", (userid,))            
            self.p = self.cursor.fetchone()
            self.conn.commit()
            if self.p[0] == self.entry_pwd.get():                 # to match the password
                self.cursor.execute("UPDATE users SET username = %s WHERE userID=%s AND password=%s", (self.entry_newUsername.get(), userid, self.entry_pwd.get()))
                self.conn.commit()
            else:
                messagebox.showinfo("WARNING!!","Wrong password, Try again....", icon='warning')
            self.cursor.close()
            self.conn.close()
            self.sub.destroy()
        else:
            messagebox.showinfo("WARNING!!","Empty text fields...", icon='warning')

    # toplevel window to chnage username
    self.sub = Toplevel(self)
    self.sub.title("Update User name")
    self.sub.geometry("330x250+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    self.frame = Frame(self.sub)
    self.frame.grid(padx=60)

    self.label_heading = Label(self.frame, text="CHANGE USER NAME")
    self.label_heading.grid(row=0, column=0)

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=1, column=0)

    self.label_pwd = Label(self.frame, text="Enter your Password", font=(None, 10))
    self.label_pwd.grid(row=2, column=0, sticky='w', pady=5)

    self.pwd = StringVar()
    self.entry_pwd = Entry(self.frame, width=30, show='*', font=(None, 10), textvariable=self.pwd)
    self.entry_pwd.grid(row=3, column=0, sticky='w')

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=4, column=0)

    self.label_newUsername = Label(self.frame, text="Enter your new UserName", font=(None, 10))
    self.label_newUsername.grid(row=5, column=0, sticky='w', pady=5)

    self.newUsername = StringVar()
    self.entry_newUsername = Entry(self.frame, width=30, font=(None, 10), textvariable=self.newUsername)
    self.entry_newUsername.grid(row=6, column=0, sticky='w')

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=7, column=0)

    self.button_update = Button(self.frame, text="UPDATE", command=new_username)
    self.button_update.grid(row=8, column=0)

    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    update_username(root, "amit")