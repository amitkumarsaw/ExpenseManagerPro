from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkcalendar import *
from expense_database import get_connection
import datetime
from tkinter import messagebox

def edit_subWindow(self, userid):
    '''
    sub window using toplevel and set focus on child and disable access to parent window
    '''
    self.sub = Toplevel(self)
    self.sub.title("Edit Window")
    self.sub.geometry("850x570+100+100")
    self.sub.focus_force()
    self.sub.grab_set()
    self.sub.transient(self)

    # search function
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

    # define an edit function
    def edit_record():
        # to check if there is a record selected or not
        if self.tree_view.selection():
            # local variables
            self.edited_date = StringVar()
            self.edited_title = StringVar()
            self.edited_quantity = StringVar()
            self.edited_expense = StringVar()

            # to get the editable item from the tree_view1
            self.editable_item = self.tree_view.selection()
            # print(self.tree_view.set(self.editable_item, '#1'))

            # defining update function
            def update():
                self.edited_date = edit_e_date.get()
                self.edited_date_obj = datetime.datetime.strptime(self.edited_date, '%m/%d/%y').strftime('%y-%m-%d')
                self.edited_title = edit_e_title.get()
                self.edited_quantity = edit_e_quantity.get()
                self.edited_expense = edit_e_expense.get()
                # conning to sqlite database
                self.conn = get_connection()
                self.cursor = self.conn.cursor()

                for x in self.editable_item:
                    # database stuff
                    self.cursor.execute("UPDATE expense SET date=%s, product_name=%s,  quantity=%s, expense=%s WHERE date=%s AND product_name=%s AND quantity=%s AND expense=%s AND userID = %s", (self.edited_date_obj, self.edited_title, self.edited_quantity, self.edited_expense, self.tree_view.set(self.editable_item, '#1'), self.tree_view.set(self.editable_item, '#2'), self.tree_view.set(self.editable_item, '#3'), self.tree_view.set(self.editable_item, '#4'), userid))
                    self.conn.commit()
                    # replacing the selected row with new inputs
                    self.tree_view.item(x, values=(self.edited_date, self.edited_title, self.edited_quantity, self.edited_expense))   # to edit the selected item in the tree_view1
                
                # to exit the edit window
                self.upadte_Window.destroy()

            # edit popup window to edit the items
            self.upadte_Window = Toplevel(self.sub)
            self.upadte_Window.title("EDIT TOOL WINDOW :")
            self.upadte_Window.geometry("650x140")
            self.upadte_Window.focus_force()
            self.upadte_Window.grab_set()
            self.upadte_Window.transient(self)

            # styling
            self.style = ttk.Style()
            self.style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='10', relief=RAISED)

            # frame for the new opened window
            edit_frame = Frame(self.upadte_Window)
            edit_frame.pack(fill="both", expand=1, padx=10, pady=10)

            edit_l_date = Label(edit_frame, text='DATE : ')
            edit_l_date.grid(row=0, column=0, padx=15, pady=5, sticky='w')

            edit_e_date = DateEntry(edit_frame, width=10, font=(None, 10),  textvariable=self.edited_date)
            edit_e_date.grid(row=1, column=0, padx=15, pady=5, sticky='w')
            self.editable_date_obj = datetime.datetime.strptime(self.tree_view.set(self.editable_item, '#1'), '%Y-%m-%d').strftime('%m/%d/%y')
            self.edited_date.set(self.editable_date_obj)

            edit_l_title = Label(edit_frame, text='TITLE : ')
            edit_l_title.grid(row=0, column=1, padx=15, pady=5, sticky='w')

            edit_e_title = Entry(edit_frame, width=20, font=(None, 10), textvariable=self.edited_title)
            edit_e_title.grid(row=1, column=1, padx=15, pady=5, sticky='w')
            self.edited_title.set((self.tree_view.set(self.editable_item, '#2')),)      # to set a default value to the text field ( i.e. the value selected from the tree view)

            edit_l_quantity = Label(edit_frame, text='QUANTITY : ')
            edit_l_quantity.grid(row=0, column=2, padx=15, pady=5, sticky='w') 

            edit_e_quantity = Entry(edit_frame, width=20, font=(None, 10), textvariable=self.edited_quantity)
            edit_e_quantity.grid(row=1, column=2, padx=15, pady=5, sticky='w')
            self.edited_quantity.set((self.tree_view.set(self.editable_item, '#3')),)      # to set a default value to the text field ( i.e. the value selected from the tree view)

            edit_l_expense = Label(edit_frame, text='EXPENSE : ')
            edit_l_expense.grid(row=0, column=3, padx=15, pady=5, sticky='w') 

            edit_e_expense = Entry(edit_frame, width=20, font=(None, 10), textvariable=self.edited_expense)
            edit_e_expense.grid(row=1, column=3, padx=15, pady=5, sticky='w')
            self.edited_expense.set((self.tree_view.set(self.editable_item, '#4')),)      # to set a default value to the text field ( i.e. the value selected from the tree view)

            # button to add the entered data into the database
            update_button = Button(edit_frame, text='  UPDATE  ', command=update)
            update_button.grid(row=2, column=2, padx=40, pady=15)
        else:
            messagebox.showinfo('WARNING','There is no record selected !!')

    # clear screen button logic
    def clear_screen():
        self.tree_view_records = self.tree_view.get_children()
        for item in self.tree_view_records:
            self.tree_view.delete(item)

    # styling
    self.style = ttk.Style()
    self.style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='10', relief=RAISED)

    # ------- frames --------
    self.frame1 = Frame(self.sub)
    self.frame1.grid(row = 0, columnspan = 4)
    self.frame2 = Frame(self.sub)
    self.frame2.grid(row = 1, columnspan = 4)
    self.frame3 = Frame(self.sub)
    self.frame3.grid(row = 2, column = 0)
    self.frame4 = Frame(self.sub)
    self.frame4.grid(row = 2, column = 1)

    self.label_search = Label(self.frame1, text="Search by ", font=(None, 13))
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
    self.entry_search = Entry(self.frame1, width=20, font=(None, 13))
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

    # button to clear the screen
    self.button_clearScreen = Button(self.frame3, text='CLEAR SCREEN', command=clear_screen)
    self.button_clearScreen.grid(row=2, column=0, padx=15, pady=30)

    # button to edit
    self.button_edit = Button(self.frame3, text='   E D I T   ', command=edit_record)
    self.button_edit.grid(row=2, column=3, padx=300, pady=30)

    self.sub.mainloop()

if __name__ == '__main__':
    root = Tk()
    edit_subWindow(root, "amit")