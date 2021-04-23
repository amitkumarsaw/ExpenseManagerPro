from tkinter import *
from tkinter import ttk
from expense_database import get_connection
from tkinter import messagebox

def update_pwd(self, userid):

    def new_pwd():
        if self.entry_newPwd.get() != "" and self.entry_oldPwd.get() != "":                # to check if the text fields are empty or not
            self.conn = get_connection()
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT password FROM users WHERE userID=%s", (userid,))            
            self.p = self.cursor.fetchone()
            self.conn.commit()
            if self.p[0] == self.entry_oldPwd.get():                 # to match the password
                self.cursor.execute("UPDATE users SET password = %s WHERE userID=%s AND password=%s", (self.entry_newPwd.get(), userid, self.entry_oldPwd.get()))
                self.conn.commit()
            else:
                messagebox.showinfo("WARNING!!","Wrong password, Try again....", icon='warning')
            self.cursor.close()
            self.conn.close()
            self.sub.destroy()
        else:
            messagebox.showinfo("WARNING!!","Empty text field(s)...", icon='warning')

    # toplevel window to chnage username
    self.sub = Toplevel(self)
    self.sub.title("Change password")
    self.sub.geometry("330x250+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    self.frame = Frame(self.sub)
    self.frame.grid(padx=60)

    self.label_heading = Label(self.frame, text="CHANGE PASSWORD")
    self.label_heading.grid(row=0, column=0)

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=1, column=0)

    self.label_oldPwd = Label(self.frame, text="Enter your old Password", font=(None, 10))
    self.label_oldPwd.grid(row=2, column=0, sticky='w', pady=5)

    self.oldPwd = StringVar()
    self.entry_oldPwd = Entry(self.frame, width=30, show='*', font=(None, 10), textvariable=self.oldPwd)
    self.entry_oldPwd.grid(row=3, column=0, sticky='w')

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=4, column=0)

    self.label_newPwd = Label(self.frame, text="Enter your new Password", font=(None, 10))
    self.label_newPwd.grid(row=5, column=0, sticky='w', pady=5)

    self.newPwd = StringVar()
    self.entry_newPwd = Entry(self.frame, width=30, font=(None, 10), textvariable=self.newPwd)
    self.entry_newPwd.grid(row=6, column=0, sticky='w')

    self.label_gap = Label(self.frame, text="")
    self.label_gap.grid(row=7, column=0)

    self.button_update = Button(self.frame, text="UPDATE", command=new_pwd)
    self.button_update.grid(row=8, column=0)

    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    update_pwd(root, "amit")