from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
from tkcalendar import *
from expense_database import get_connection
import datetime

def add_subWindow(self, userid):
    '''
    sub window using toplevel and set focus on child and disable access to parent window
    '''
    self.sub = Toplevel(self)
    self.sub.title("Add Window")
    self.sub.geometry("850x570+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    # ------- frames --------
    self.frame1 = Frame(self.sub)
    self.frame1.grid(row = 0)
    self.frame2 = Frame(self.sub)
    self.frame2.grid(row = 1)

    # command to add data into the database and displaying it into the treeview
    def insert():
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.date = self.date_entry.get()
        self.date_obj = datetime.datetime.strptime(self.date, '%d/%m/%y').strftime('%Y-%m-%d')      # edited
        self.title = self.title_entry.get()
        self.quantity = self.quantity_entry.get()
        self.expense = self.expense_entry.get()
        self.cursor.execute("INSERT INTO expense (userID, date, product_name, quantity, expense) VALUES(%s, %s, %s, %s, %s)", (userid, self.date_obj, self.title, self.quantity, self.expense))                         
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        self.tree_view.insert('', 'end', values=(self.date, self.title, self.quantity, self.expense))

        self.title_entry.delete(0, END)   # to clear the title entry box
        self.expense_entry.delete(0, END)   # to clear the expense entry box
        self.quantity_entry.delete(0, END)   # to clear the quantity entry box

    # styling
    self.style = ttk.Style()
    self.style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='10', relief=RAISED)

    # ------------- date --------------
    self.date_label = Label(self.frame1, text='DATE : ', font=(None, 10), anchor=W)
    self.date_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')

    self.date = StringVar()
    self.date_entry = DateEntry(self.frame1, width=10, font=(None, 10), textvariable=self.date)
    self.date_entry.grid(row=0, column=1, padx=10, pady=20, sticky='w')

    # ------------- title -------------
    self.title_label = Label(self.frame1, text='TITLE : ', font=(None, 10), anchor=W)
    self.title_label.grid(row=1, column=0, padx=20, pady=5, sticky='w')

    self.title = StringVar()
    self.title_entry = Entry(self.frame1, width=30, font=(None, 10), textvariable=self.title)
    self.title_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    # ------------- quantity ------------
    self.quantity_label = Label(self.frame1, text="QUANTITY :", font=(None, 10), anchor=W)
    self.quantity_label.grid(row=2, column=0, padx=20, pady=5, sticky='w')

    self.quantity = StringVar() 
    self.quantity_entry = Entry(self.frame1, width=30, font=(None, 10), textvariable=self.quantity)
    self.quantity_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    # ------------- expense -------------
    self.expense_label = Label(self.frame1, text='EXPENSE : ', font=(None, 10), anchor=W)
    self.expense_label.grid(row=3, column=0, padx=20, pady=15, sticky='w')

    self.expense = StringVar() 
    self.expense_entry = Entry(self.frame1, width=30, font=(None, 10), textvariable=self.expense)
    self.expense_entry.grid(row=3, column=1, padx=10, pady=15, sticky='w')

    # tkinter button to add data into the database
    self.add_button = Button(self.frame1, text='       ADD      ', command=insert)
    self.add_button.grid(row=1, column=2, padx=40, pady=15)

    # treeview for the add form
    self.tree_view = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4), show="headings", height="15")
    self.tree_view.grid(row=4, column=0, padx=15, pady=10, sticky='w', columnspan=3)

    self.tree_view.heading('#1', text="D A T E")
    self.tree_view.heading('#2', text="T I T L E")
    self.tree_view.heading('#3', text="Q U A N T I T Y")
    self.tree_view.heading('#4', text="E X P E N S E")

    self.scrollbar = Scrollbar(self.frame1, orient=VERTICAL, command=self.tree_view.yview)
    self.tree_view.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.grid(row=4, column=0, sticky=S + E + N, columnspan=3)

    # sub.grab_release()
    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    add_subWindow(root, "amit")
