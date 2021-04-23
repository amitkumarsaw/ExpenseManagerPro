from tkinter import *
from tkinter import ttk
from expense_database import get_connection
from tkinter import messagebox
import pandas as pd

def graph(self, userid):

    self.frame1 = Frame(self)
    self.frame1.grid(row=0, column=0)

    self.frame2 = Frame(self)
    self.frame2.grid(row=0, column=1)

    self.frame3 = Frame(self)
    self.frame3.grid(row=1, column=0)

    self.frame4 = Frame(self)
    self.frame4.grid(row=0, column=1)

    df = pd.read_sql(('SELECT date, expense FROM expense WHERE userID=%s', (userid,)), con=get_connection)

    print(df)

