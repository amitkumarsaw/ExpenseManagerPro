from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkcalendar import *
from expense_database import get_connection
import datetime
from tkinter import messagebox

def delete_subWindow(self, userid):
    '''
    sub window using toplevel and set focus on child and disable access to parent window
    '''
    self.sub = Toplevel(self)
    self.sub.title("Delete Window")
    self.sub.geometry("850x570+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    # search function (in tab 2)
    def search():
        # checking for empty space
        if self.entry_search.get() == "":
            messagebox.showinfo("WARNING !! ", "WARNING: Search Entry is empty. Check again !!")
        else:
            self.conn = get_connection()
            self.cursor = self.conn.cursor()

            self.variable_input = self.variable.get()   # taking selected option from the option menu

            if self.variable_input == "Date :":
                self.cursor.execute("SELECT * FROM expense WHERE date = %s AND userID = %s", (self.entry_search.get(), userid))                 
                self.records = self.cursor.fetchall()
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
            elif self.variable_input == "Title :":
                self.cursor.execute("SELECT * FROM expense WHERE product_name = %s AND userID = %s", (self.entry_search.get(), userid))                  
                self.records = self.cursor.fetchall()
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
            elif self.variable_input == "Expense :":
                self.cursor.execute("SELECT * FROM expense WHERE expense = %s AND userID = %s", (self.entry_search.get(), userid))                   
                self.records = self.cursor.fetchall()
                self.conn.commit()
                self.cursor.close()
                self.conn.close()

            print(self.records)

            # for record in self.records:
            if self.records == []:
                messagebox.showinfo("INFO", "There is no such item...!!")
            else:
                self.tree_view.insert('', 'end', values=(self.records[0][1], self.records[0][2], self.records[0][3], self.records[0][4]))
                
            self.entry_search.delete(0, END)    # to clear the search entry

    # to delete the selected contents from the database and tree_view1
    def delete_record():
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        # if else stmt to check if there is record selected or not
        if self.tree_view.selection():
            # warning window for delete all button 
            self.MsgBox = messagebox.askquestion ('DELETE SELECTED RECORD','Are you sure you want to delete the selected records !!',icon = 'warning')
            if self.MsgBox == 'yes':
                    for selected_item in self.tree_view.selection():
                        print(selected_item)      # it prints the selected row id
                        self.cursor.execute("DELETE FROM expense WHERE date=%s AND product_name=%s AND quantity=%s AND expense=%s AND userID = %s", (self.tree_view.set(selected_item, '#1'), self.tree_view.set(selected_item, '#2'), self.tree_view.set(selected_item, '#3'), self.tree_view.set(selected_item, '#4'), userid))
                        self.conn.commit()
                        self.cursor.close()
                        self.conn.close()
                        self.tree_view.delete(selected_item)
            else:
                messagebox.showinfo('Return','You will now return to the application screen')
        else:
            messagebox.showinfo('WARNING','There is no record selected !!')

    # show all button logic
    def show_all():
        self.conn = get_connection()
        self.cursor = self.conn.cursor() 
        self.cursor.execute("SELECT date, product_name, quantity, expense FROM expense WHERE userID=%s", (userid,))
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
            print(row) # it print all records in the database
            self.tree_view.insert('', 'end', values=row)
        # to put a blank row in the tree view
        self.tree_view.insert('', 'end', values="")

    # function to delete every record
    def delete_all():
        conn = get_connection()
        cursor = conn.cursor()

        # warning window for delete all button 
        MsgBox = messagebox.askquestion ('DELETE EVERYTHING','Are you sure you want to delete all the contents of the table !!',icon = 'warning')
        if MsgBox == 'yes':
            cursor.execute("DELETE FROM expense WHERE userID=%s", (userid,))     # delete the contents of the table
            conn.commit()
            cursor.close()
            conn.close()
            # self.sub.destroy()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')

        # delete the contents of tree_view
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)

    # styling
    self.style = ttk.Style()
    self.style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='10', relief=RAISED)

    # ------- frames --------
    self.frame1 = Frame(self.sub)
    self.frame1.grid(row = 0, columnspan = 3)
    self.frame2 = Frame(self.sub)
    self.frame2.grid(row = 1, columnspan = 3)
    self.frame3 = Frame(self.sub)
    self.frame3.grid(row = 2, column = 0)
    self.frame4 = Frame(self.sub)
    self.frame4.grid(row = 2, column = 1)
    self.frame5 = Frame(self.sub)
    self.frame5.grid(row = 2, column = 2)

    self.label_search = Label(self.frame1, text="Search by ")
    self.label_search.grid(row=0, column=0, padx=10, pady=20, sticky='w')

    # create menulist
    self.variable = StringVar()
    self.choices = {"Title :", "Date :", "Expense :"}
    self.drop_down = OptionMenu(self.frame1, self.variable, *self.choices)
    self.variable.set("Title :") # default value
    self.drop_down.grid(row=0, column=1, pady=20, sticky='w')
    # configure text of the menulist
    # self.drop_down.config(font=(None, 13, 'bold'))

    # text field for search
    self.entry_search = Entry(self.frame1, width=20, font=(None, 13, 'bold'))
    self.entry_search.grid(row=0, column=2, padx=30, pady=50, sticky='w')

    # button for search
    self.button_search = Button(self.frame1, text='SEARCH', command=search)
    self.button_search.grid(row=0, column=3, padx=15, pady=30)

    # treeview for the add form
    self.tree_view = ttk.Treeview(self.frame2, columns=(1, 2, 3, 4), show="headings", height="15")
    self.tree_view.grid(row=0, column=0, padx=15, pady=10, sticky='w')

    self.tree_view.heading('#1', text="D A T E")
    self.tree_view.heading('#2', text="T I T L E")
    self.tree_view.heading('#3', text="Q U A N T I T Y")
    self.tree_view.heading('#4', text="E X P E N S E")

    self.scrollbar = Scrollbar(self.frame2, orient=VERTICAL, command=self.tree_view.yview)
    self.tree_view.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.grid(row=0, column=0, sticky=S + E + N)

    # button to show all the records
    self.button_showall = Button(self.frame3, text='SHOW ALL', command=show_all)
    self.button_showall.grid(row=2, column=0, padx=15, pady=30)

    # button to delete the selected records 
    self.button_delete = Button(self.frame3, text='    DELETE    ', command=delete_record)
    self.button_delete.grid(row=2, column=1, padx=280, pady=30)

    # button to delete all the records
    self.button_deleteall = Button(self.frame3, text='DELETE ALL', command=delete_all)
    self.button_deleteall.grid(row=2, column=2, padx=15, pady=30)







    self.sub.mainloop()