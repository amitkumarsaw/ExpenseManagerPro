# from tkcalendar import Calendar, DateEntry
# try:
#     import tkinter as tk
#     from tkinter import ttk
# except ImportError:
#     import Tkinter as tk
#     import ttk


# def example1():
#     def print_sel():
#         print(cal.selection_get())
#         cal.see(datetime.date(year=2016, month=2, day=5))

#     top = tk.Toplevel(root)

#     import datetime
#     today = datetime.date.today()

#     mindate = datetime.date(year=2018, month=1, day=21)
#     maxdate = today + datetime.timedelta(days=5)
#     print(mindate, maxdate)

#     cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
#                    mindate=mindate, maxdate=maxdate, disabledforeground='red',
#                    cursor="hand1", year=2018, month=2, day=5)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()


# def example2():

#     top = tk.Toplevel(root)

#     cal = Calendar(top, selectmode='none')
#     date = cal.datetime.today() + cal.timedelta(days=2)
#     cal.calevent_create(date, 'Hello World', 'message')
#     cal.calevent_create(date, 'Reminder 2', 'reminder')
#     cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
#     cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

#     cal.tag_config('reminder', background='red', foreground='yellow')

#     cal.pack(fill="both", expand=True)
#     ttk.Label(top, text="Hover over the events.").pack()


# def example3():
#     top = tk.Toplevel(root)

#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2, year=2010)
#     cal.pack(padx=10, pady=10)


# root = tk.Tk()
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

# root.mainloop()

from pandas import DataFrame
 
# data1 = {'Country': ['US','CA','GER','UK','FR'],
#          'GDP_Per_Capita': [45000,42000,52000,49000,47000]
#         }
# df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])
# print (df1)


# data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#          'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#         }  
# df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])
# print (df2)


# data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
#          'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
#         }
# df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
# print (df3)

# import tkinter as tk
# from pandas import DataFrame
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# data1 = {'Country': ['US','CA','GER','UK','FR'],
#          'GDP_Per_Capita': [45000,42000,52000,49000,47000]
#         }
# df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


# data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#          'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#         }
# df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


# data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
#          'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
#         }  
# df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
 

# root= tk.Tk() 
  
# figure1 = plt.Figure(figsize=(6,5), dpi=100)
# ax1 = figure1.add_subplot(111)
# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Country Vs. GDP Per Capita')

# figure2 = plt.Figure(figsize=(5,4), dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2, root)
# line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
# ax2.set_title('Year Vs. Unemployment Rate')

# figure3 = plt.Figure(figsize=(5,4), dpi=100)
# ax3 = figure3.add_subplot(111)
# ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
# scatter3 = FigureCanvasTkAgg(figure3, root) 
# scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# ax3.legend(['Stock_Index_Price']) 
# ax3.set_xlabel('Interest Rate')
# ax3.set_title('Interest Rate Vs. Stock Index Price')

# root.mainloop()

# from easygui import msgbox, passwordbox
  
# title = "Password"
# pass_word = (passwordbox("Please enter your password", title))
  
# msgbox("Your password: %s"%pass_word, title="Password revealed")


from tkinter import *
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="click me!",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="print value",command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.b2.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()