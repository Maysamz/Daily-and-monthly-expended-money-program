import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re
import datetime
from datetime import date
from datetime import date as ddt
from random import randint
import sqlite3
from matplotlib import pyplot as plt
from PIL import Image, ImageTk

class GUI():
    def __init__(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        def admin_window(self):
            self.lroot4 = Tk()
            self.lroot4.geometry('800x550')
            self.lroot4.title('Admin')
            self.lroot4.configure(background="#bff794")
            self.label_7 = Label(self.lroot4, text="Admin",background="#bff794", width=16, font=('bold', 20))
            self.label_7.grid(row=0, column=2)

            # conn = sqlite3.connect('database.db')
            # cursor = conn.cursor()

            cursor.execute("select FName from UserData order by FName")
            name = cursor.fetchall()

            cursor.execute("select LName from UserData order by FName")
            lname = cursor.fetchall()

            cursor.execute("select CustomerID from UserData order by FName")
            id = cursor.fetchall()

            cursor.execute("select initialbalance from UserData order by FName")
            balance = cursor.fetchall()


            l = Label(self.lroot4, text="First Name",background="#bff794", font="Calibri 14", fg="black", padx=20, pady=20)
            l.grid(row=1, column=0)
            l = Label(self.lroot4, text="Last Name",background="#bff794", font="Calibri 14", fg="black", padx=20, pady=20)
            l.grid(row=1, column=1)
            l = Label(self.lroot4, text="ID",background="#bff794", font="Calibri 14", fg="black", padx=20, pady=20)
            l.grid(row=1, column=2)
            l = Label(self.lroot4, text="BALANCE",background="#bff794", font="Calibri 14", fg="black", padx=20, pady=20)
            l.grid(row=1, column=3)


            count = 2
            for n in name:
                l = Label(self.lroot4, text=n, font="Calibri 15",background="#bff794", fg="black", padx=20, pady=20)
                l.grid(row=count, column=0)
                count += 1

            count = 2
            for n in lname:
                l = Label(self.lroot4, text=n, font="Calibri 15",background="#bff794", fg="black", padx=20, pady=20)
                l.grid(row=count, column=1)
                count += 1

            count = 2
            for n in id:
                l = Label(self.lroot4, text=n, font="Calibri 15",background="#bff794", fg="black", padx=20, pady=20)
                l.grid(row=count, column=2)
                count += 1

            count = 2
            for n in balance:
                l = Label(self.lroot4, text=n, font="Calibri 15",background="#bff794", fg="black", padx=20, pady=20)
                l.grid(row=count, column=3)
                count += 1


            def back():
                self.lroot4.destroy()
                signup(self)

            def exit():
                self.lroot4.destroy()


            self.button15 = Button(self.lroot4, text='Back',background="#f4f7b7", width=12, command=back)
            self.button15.place(x=50, y=500)

            self.button16 = Button(self.lroot4, text='Exit', width=12,background="#f4f7b7", command=exit)
            self.button16.place(x=580, y=500)

            self.lroot4.mainloop()
        # admin_window(self)

        def login(self):
            def validateLogin():
                self.id = username.get()
                self.id2 = username.get()
                self.passwrd = password.get()

                if username.get() == 'admin' and password.get() == 'admin':
                    self.lroot.destroy()
                    admin_window(self)
                else:
                    conn = sqlite3.connect('database.db')
                    cursor = conn.cursor()
                    statement = f"SELECT CustomerID,Password from UserData WHERE CustomerID={int(self.id)} AND Password = '{str(self.passwrd)}';"
                    cursor.execute(statement)
                    result = cursor.fetchone()

                    if re.fullmatch(r'[0-9]{6}?', self.id2):
                        pass
                    else:
                        messagebox.showerror("Error", "Invalid ID")
                    if len(self.id2)!=6:
                        messagebox.showerror("Error", "Invalid ID length")
                    else:
                        if result==None:  # An empty result evaluates to False.
                            messagebox.showerror("Error", "Invalid Credentials")
                        else:
                            messagebox.showerror("Login", "Successfully Logged in!")
                            self.lroot.destroy()
                            ebudget(self)

            self.lroot = Tk()
            self.lroot.geometry('400x150')
            self.lroot.title('Login Form')
            self.lroot.configure(background="#bff794")
            usernameLabel = Label(self.lroot, text="ID",font=("Helvetica", "13"),background="#bff794").place(x=10,y=5)
            username = StringVar()

            usernameEntry = Entry(self.lroot, textvariable=username,width=40).place(x=100,y=5)
            passwordLabel = Label(self.lroot, text="Password",font=("Helvetica", "13") ,background="#bff794").place(x=10,y=50)

            password = StringVar()
            passwordEntry = Entry(self.lroot, textvariable=password,width=40, show='*').place(x=100,y=50)

            loginButton = Button(self.lroot, text="Login",font="Helvetica",width=8,background="#f4f7b7",command=validateLogin).place(x=150,y=105)
            self.lroot.mainloop()
        # login(self)

        def ebudget(self):
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Transactions (CustomerID ,Type ,Category,Amount,Date DATE )')
            self.root2 = Tk()
            self.root2.geometry("800x600")

            self.root2.title('e-buget')
            self.root2.configure(background="#bff794")

            def bycategory():
                self.win2 = Tk()
                self.win2.geometry("1000x600")
                self.win2.title('Transactions By Category')
                self.win2.configure(background="#bff794")
                self.label1 = Label(self.win2, text=f"Select Category: ", width=18, font=("bold", 13),
                                    background="#bff794")
                self.label1.grid(row=0, column=0)

                def show():
                    # print(self.menu3.get())
                    cursor.execute(
                        f"select CustomerID from Transactions WHERE Category='{str(self.menu3.get())}' AND CustomerID='{str(self.id)}' ORDER BY Category")
                    name = cursor.fetchall()


                    cursor.execute(
                        f"select Type from Transactions WHERE Category='{str(self.menu3.get())}' AND CustomerID='{str(self.id)}' ORDER BY Category")
                    lname = cursor.fetchall()

                    cursor.execute(
                        f"select Category from Transactions WHERE Category='{str(self.menu3.get())}' AND CustomerID='{str(self.id)}' ORDER BY Category")
                    id = cursor.fetchall()

                    cursor.execute(
                        f"select Amount from Transactions WHERE Category='{str(self.menu3.get())}' AND CustomerID='{str(self.id)}' ORDER BY Category")
                    balance = cursor.fetchall()

                    cursor.execute(
                        f"select Date from Transactions WHERE Category='{str(self.menu3.get())}' AND CustomerID='{str(self.id)}' ORDER BY Category")
                    date = cursor.fetchall()

                    l = Label(self.win2, text="Customer ID", background="#bff794", font=("Helvetica", "15"),
                              fg="black", padx=20, pady=20)
                    l.grid(row=2, column=0)
                    l = Label(self.win2, text="Type", background="#bff794", font=("Helvetica", "15"), fg="black",
                              padx=20, pady=20)
                    l.grid(row=2, column=1)
                    l = Label(self.win2, text="Category", background="#bff794", font=("Helvetica", "15"), fg="black",
                              padx=20, pady=20)
                    l.grid(row=2, column=2)
                    l = Label(self.win2, text="Amount", background="#bff794", font=("Helvetica", "15"), fg="black",
                              padx=20, pady=20)
                    l.grid(row=2, column=3)
                    l = Label(self.win2, text="Date", background="#bff794", font=("Helvetica", "15"), fg="black",
                              padx=20, pady=20)
                    l.grid(row=2, column=4)

                    count = 3
                    for n in name:
                        self.l1 = Label(self.win2, text=n, font="Calibri 15", background="#bff794", fg="black",
                                        padx=20, pady=20)
                        self.l1.grid(row=count, column=0)
                        count += 1

                    count = 3
                    for n in lname:
                        self.l1 = Label(self.win2, text=n, font="Calibri 15", background="#bff794", fg="black",
                                        padx=20, pady=20)
                        self.l1.grid(row=count, column=1)
                        count += 1

                    count = 3
                    for n in id:
                        self.l1 = Label(self.win2, text=n, font="Calibri 15", background="#bff794", fg="black",
                                        padx=20, pady=20)
                        self.l1.grid(row=count, column=2)
                        count += 1

                    count = 3
                    for n in balance:
                        self.l1 = Label(self.win2, text=n, font="Calibri 15", background="#bff794", fg="black",
                                        padx=20, pady=20)
                        self.l1.grid(row=count, column=3)
                        count += 1
                    count = 3
                    for n in date:
                        self.l1 = Label(self.win2, text=n, font="Calibri 15", background="#bff794", fg="black",
                                        padx=20, pady=20)
                        self.l1.grid(row=count, column=4)
                        count += 1


                self.menu3 = StringVar()
                self.menu3.set("Select Category")
                self.drop2 = OptionMenu(self.win2, self.menu3, "Salary","Transfer","Food and Beverages", "Utilities", "Health and Sport", "Monthly Redemption Payment",
                                           "Restaurants and Hotels", "Education and Culture", "Insurance and Taxes")
                self.drop2.grid(row=0, column=2)

                self.button14 = Button(self.win2, text='Show',background="#f1f59f", width=12, command=show)
                self.button14.grid(row=0, column=4)

                self.win2.mainloop()

            def byperiod():
                self.win3= Tk()
                self.win3.geometry("1000x600")
                self.win3.title('Transactions By Period')
                self.win3.configure(background="#bff794")

                self.label1 = Label(self.win3, text=f"Select Period: ", width=18, font=("bold", 13),
                                    background="#bff794")
                self.label1.grid(row=0, column=0)

                cursor.execute(
                    f"select Date from Transactions WHERE  CustomerID='{str(self.id)}' ORDER BY Category")
                date = cursor.fetchall()
                # print(date)#AND Date ='{str(self.entry1.get())}'
                def show():
                    if self.menu4.get() == 'First Quarter':
                        cursor.execute(
                            f"select CustomerID from Transactions WHERE CustomerID='{str(self.id)}' AND Date='{ddt.today()}' ORDER BY Category")
                        date2 = cursor.fetchall()

                        cursor.execute(
                            f"select Type from Transactions WHERE CustomerID='{str(self.id)}' AND Date='{ddt.today()}' ORDER BY Category")
                        lname = cursor.fetchall()

                        cursor.execute(
                            f"select Category from Transactions WHERE CustomerID='{str(self.id)}' AND Date='{ddt.today()}' ORDER BY Category")
                        id = cursor.fetchall()

                        cursor.execute(
                            f"select Amount from Transactions WHERE CustomerID='{str(self.id)}' AND Date='{ddt.today()}' ORDER BY Category")
                        balance = cursor.fetchall()

                        cursor.execute(
                            f"select Date from Transactions WHERE CustomerID='{str(self.id)}' AND Date='{ddt.today()}' ORDER BY Category")
                        date = cursor.fetchall()

                        l = Label(self.win3, text="Customer ID", background="#bff794", font=("Helvetica", "15"),
                                  fg="black", padx=20, pady=20)
                        l.grid(row=2, column=0)
                        l = Label(self.win3, text="Type", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=1)
                        l = Label(self.win3, text="Category", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=2)
                        l = Label(self.win3, text="Amount", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=3)
                        l = Label(self.win3, text="Date", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=4)

                        count = 3
                        for n in date2:
                            self.l1 = Label(self.win3, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=0)
                            count += 1

                        count = 3
                        for n in lname:
                            self.l1 = Label(self.win3, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=1)
                            count += 1

                        count = 3
                        for n in id:
                            self.l1 = Label(self.win3, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=2)
                            count += 1

                        count = 3
                        for n in balance:
                            self.l1 = Label(self.win3, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=3)
                            count += 1

                        count = 3
                        for n in date:
                            self.l1 = Label(self.win3, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=4)
                            count += 1

                    else:
                        messagebox.showerror("Error","No Records Found")


                self.menu4 = StringVar()
                self.menu4.set("Select Category")
                self.drop3 = OptionMenu(self.win3, self.menu4, "First Quarter","Second Quarter","Third Quarter","Fourth Quarter")

                self.drop3.grid(row=0, column=2)
                self.button14 = Button(self.win3, text='Show',background="#f1f59f", width=12,command = show)
                self.button14.place(x=650,y=0)

            def piechart():
                self.win5 = Tk()
                self.win5.geometry("800x200")
                self.win5.title('Charts')
                self.win5.configure(background="#bff794")

                def showchart():

                    cursor.execute(
                        f"select Category  from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' AND (Date BETWEEN strftime('%Y-%m-01','now') and strftime('%Y-%m-%d','now')) ORDER BY Category")
                    category = cursor.fetchall()
                    categorylist = []
                    for tup in category:
                        t = str(tup).replace("('", "").replace("',)", "")
                        categorylist.append(t)
                    # print(categorylist)

                    cursor.execute(
                        f"select Amount  from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' AND (Date BETWEEN strftime('%Y-%m-01','now') and strftime('%Y-%m-%d','now')) ORDER BY Category")
                    amount = cursor.fetchall()
                    amountlist = []
                    for tup in amount:
                        t = str(tup).replace("('", "").replace("',)", "")
                        amountlist.append(int(t))
                    outputlist = list(zip(categorylist, amountlist))
                    count = -1
                    list2 = []
                    dict = {}
                    for i in outputlist:
                        count += 1
                        if i[0] in list2:
                            list2.append(i[0])
                            dict[i[0]] += amountlist[count]
                        else:
                            list2.append(i[0])
                            dict[i[0]] = amountlist[count]
                    keyslist = []
                    valueslist = []
                    for key, val in dict.items():
                        keyslist.append(key)
                        valueslist.append(val)
                    fig = plt.figure(figsize=(6, 4))
                    plt.pie(valueslist, labels=keyslist)
                    plt.show()

                def showchartyear():
                    cursor.execute(
                        f"select Category  from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' AND (strftime('%Y',date) = strftime('%Y','now')) ORDER BY Category")
                    category = cursor.fetchall()
                    categorylist = []
                    for tup in category:
                        t = str(tup).replace("('", "").replace("',)", "")
                        categorylist.append(t)
                    # print(categorylist)

                    cursor.execute(
                        f"select Amount  from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' AND (strftime('%Y',date) = strftime('%Y','now')) ORDER BY Category")
                    amount = cursor.fetchall()
                    amountlist = []
                    for tup in amount:
                        t = str(tup).replace("('", "").replace("',)", "")
                        amountlist.append(int(t))
                    outputlist = list(zip(categorylist, amountlist))
                    count = -1
                    list2 = []
                    dict = {}
                    for i in outputlist:
                        count += 1
                        if i[0] in list2:
                            list2.append(i[0])
                            dict[i[0]] += amountlist[count]
                        else:
                            list2.append(i[0])
                            dict[i[0]] = amountlist[count]
                    keyslist = []
                    valueslist = []
                    for key, val in dict.items():
                        keyslist.append(key)
                        valueslist.append(val)
                    fig = plt.figure(figsize=(6, 4))
                    plt.pie(valueslist, labels=keyslist)
                    plt.show()


                self.button114 = Button(self.win5, text='This Week', width=12,background="#f1f59f", command=showchart)
                self.button114.place(x=150,y=30)

                self.button115 = Button(self.win5, text='This Month', width=12,background="#f1f59f", command=showchart)
                self.button115.place(x=300, y=30)

                self.button115 = Button(self.win5, text='This Year', width=12,background="#f1f59f", command=showchartyear)
                self.button115.place(x=450, y=30)


            def transactions():
                self.win = Tk()
                self.win.geometry("1000x600")
                self.win.title('Transactions by Type')
                self.win.configure(background="#bff794")

                def show():
                    if self.menu2.get()=='Income':
                        cursor.execute(f"select CustomerID from Transactions WHERE Type='Income' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        name = cursor.fetchall()

                        cursor.execute(f"select Type from Transactions WHERE Type='Income' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        lname = cursor.fetchall()

                        cursor.execute(f"select Category from Transactions WHERE Type='Income' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        id = cursor.fetchall()

                        cursor.execute(f"select Amount from Transactions WHERE Type='Income' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        balance = cursor.fetchall()

                        cursor.execute(
                            f"select Date from Transactions WHERE Type='Income' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        date = cursor.fetchall()

                        l = Label(self.win, text="Customer ID", background="#bff794", font=("Helvetica", "15"),
                                  fg="black", padx=20, pady=20)
                        l.grid(row=2, column=0)
                        l = Label(self.win, text="Type", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=1)
                        l = Label(self.win, text="Category", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=2)
                        l = Label(self.win, text="Amount", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=3)
                        l = Label(self.win, text="Date", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=4)

                        count = 3
                        for n in name:
                            self.l1 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l1.grid(row=count, column=0)
                            count += 1

                        count = 3
                        for n in lname:
                            self.l1 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l1.grid(row=count, column=1)
                            count += 1

                        count = 3
                        for n in id:
                            self.l1 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l1.grid(row=count, column=2)
                            count += 1

                        count = 3
                        for n in balance:
                            self.l1 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l1.grid(row=count, column=3)
                            count += 1

                        count = 3
                        for n in date:
                            self.l1 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l1.grid(row=count, column=4)
                            count += 1


                    elif self.menu2.get()=='Outcome':
                        cursor.execute(f"select CustomerID from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        name = cursor.fetchall()

                        cursor.execute(f"select Type from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        lname = cursor.fetchall()

                        cursor.execute(f"select Category from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        id = cursor.fetchall()

                        cursor.execute(f"select Amount from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        balance = cursor.fetchall()

                        cursor.execute(
                            f"select Date from Transactions WHERE Type='Outcome' AND CustomerID='{str(self.id)}' ORDER BY Category")
                        date = cursor.fetchall()

                        l = Label(self.win, text="Customer ID", background="#bff794", font=("Helvetica", "15"),
                                  fg="black", padx=20, pady=20)
                        l.grid(row=2, column=0)
                        l = Label(self.win, text="Type", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=1)
                        l = Label(self.win, text="Category", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=2)
                        l = Label(self.win, text="Amount", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=3)
                        l = Label(self.win, text="Date", background="#bff794", font=("Helvetica", "15"), fg="black",
                                  padx=20, pady=20)
                        l.grid(row=2, column=4)

                        count = 3
                        for n in name:
                            self.l2 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l2.grid(row=count, column=0)
                            count += 1

                        count = 3
                        for n in lname:
                            self.l2 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l2.grid(row=count, column=1)
                            count += 1

                        count = 3
                        for n in id:
                            self.l2 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l2.grid(row=count, column=2)
                            count += 1

                        count = 3
                        for n in balance:
                            self.l2 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                      padx=20, pady=20)
                            self.l2.grid(row=count, column=3)
                            count += 1
                        count = 3
                        for n in date:
                            self.l2 = Label(self.win, text=n, font="Calibri 15", background="#bff794", fg="black",
                                            padx=20, pady=20)
                            self.l2.grid(row=count, column=4)
                            count += 1


                self.label1 = Label(self.win, text=f"Choose Category: ", width=18, font=("bold", 13),
                                      background="#bff794")
                self.label1.grid(row=0,column=0)

                self.menu2 = StringVar()
                self.menu2.set("Select Type")


                self.drop = OptionMenu(self.win, self.menu2, "Income", "Outcome")
                self.drop.grid(row=0,column=2)

                self.button14 = Button(self.win, text='Show',background="#f1f59f", width=12, command=show)
                self.button14.grid(row=0,column=4)

                self.win.mainloop()


            # conn = sqlite3.connect('database.db')
            # cursor = conn.cursor()
            statement = f"SELECT FName ,LName ,CustomerID ,Password ,Email text,Phone ,enumber ,Date ,initialbalance from UserData WHERE CustomerID={int(self.id)} AND Password = '{str(self.passwrd)}';"
            cursor.execute(statement)
            result = cursor.fetchone()

            self.label1 = Label(self.root2, text="Track Your Expenses With The Best Service!", font=("Helvetica", "20"), width=50, background="#bff794")
            self.label1.place(x=0, y=0)

            self.button18 = Button(self.root2, text='Transactions By Type',background="#f1f59f", width=22,command = transactions)
            self.button18.place(x=20, y=470)

            self.button19 = Button(self.root2, text='Transactions By Category',background="#f1f59f", width=24, command=bycategory)
            self.button19.place(x=210, y=470)

            self.button20 = Button(self.root2, text='Transactions By Period',background="#f1f59f", width=22, command=byperiod)
            self.button20.place(x=420, y=470)

            self.button21 = Button(self.root2, text='View Charts',background="#f1f59f", width=20, command=piechart)
            self.button21.place(x=610, y=470)



            self.label_10 = Label(self.root2, text=f"e-Budget : {result[6]}", font=("Helvetica", "13"), width=16,
                               background="#bff794")
            self.label_10.place(x=0, y=80)


            self.label_10 = Label(self.root2, text=f"Balance: {result[8]}", font=("Helvetica", "13"), width=14,
                                 background="#bff794")
            self.label_10.place(x=0, y=130)


            self.label_101 = Label(self.root2, text=f"Date: {date.today()}", font=("Helvetica", "13"), width=15,
                                 background="#bff794")
            self.label_101.place(x=0, y=180)


            self.label_11 = Label(self.root2, text=f"Operation Source: ", width=16, font=("Helvetica", "13"), background="#bff794")
            self.label_11.place(x=0, y=230)


            self.entry_11 = Entry(self.root2, width=40)
            self.entry_11.place(x=160, y=230)


            self.label_12 = Label(self.root2, text=f"Operation Type: ", width=14, font=("Helvetica", "13"),
                                  background="#bff794")
            self.label_12.place(x=0, y=280)


            var = IntVar()
            def ShowChoice():
                output = var.get()
                if output==1:
                    def callback(selection):
                        print(selection)
                    self.label_13.config(text = 'Category of Income:')
                    self.drop = OptionMenu(self.root2, self.menu, "Salary", "Transfer")
                    self.drop.place(x=250, y=330)
                    # print(self.menu.get())

                elif output==2:
                    self.label_13.config(text = 'Category of Outcome:')
                    self.drop = OptionMenu(self.root2, self.menu, "Food and Beverages", "Utilities", "Health and Sport", "Monthly Redemption Payment",
                                           "Restaurants and Hotels", "Education and Culture", "Insurance and Taxes")
                    self.drop.place(x=250, y=330)


            Radiobutton(self.root2, text="Income",font=("Helvetica", "13"), padx=5, variable=var, value=1, background="#bff794",command = ShowChoice).place(x=150,y=280)
            Radiobutton(self.root2, text="Outcome",font=("Helvetica", "13"), padx=30, variable=var, value=2, background="#bff794",command = ShowChoice).place(x=280,y=280)

            self.label_13 = Label(self.root2, text=f"Category of Income: ", width=18, font=("Helvetica", "13"),background="#bff794")
            self.label_13.place(x=0, y=330)

            self.menu = StringVar()
            self.menu.set("Choose Category")

            self.label_14 = Label(self.root2, text=f"Enter Amount: ", width=15, font=("Helvetica", "13"),
                                  background="#bff794")
            self.label_14.place(x=0, y=380)

            self.label_1114 = Label(self.root2, text=f"Choose Options to View Transaction Sheet: ", width=36, font=("Helvetica", "13"),
                                  background="#bff794")
            self.label_1114.place(x=0, y=420)

            self.entry_14 = Entry(self.root2, width=40)
            self.entry_14.place(x=160, y=380)

            def submit2():
                # conn = sqlite3.connect('database.db')
                # cursor = conn.cursor()
                statement = f"SELECT FName ,LName ,CustomerID ,Password ,Email text,Phone ,enumber ,Date ,initialbalance from UserData WHERE CustomerID={int(self.id)} AND Password = '{str(self.passwrd)}';"
                cursor.execute(statement)
                result = cursor.fetchone()
                amount = self.entry_14.get()
                inpt = var.get()
                if inpt == 1:
                    statement = f'UPDATE UserData SET initialbalance = {int(result[8])+int(amount)} WHERE CustomerID={int(self.id)};'
                    cursor.execute(statement)
                    conn.commit()

                    if self.menu.get()!='Select Category':
                        cursor.execute(
                            "INSERT INTO Transactions VALUES (:CustomerID ,:Type ,:Category,:Amount,:Date)",
                            {'CustomerID': self.id,'Type':'Income','Category': self.menu.get(),'Amount':self.entry_14.get(),'Date':date.today()})
                        conn.commit()
                        # self.label_10 = Label(self.root2, text=f"Current Balance: {result[8]}", font=("bold", 13),
                        #                       width=25,
                        #                       background="light blue")

                    messagebox.showerror("Successful", "Successfully Done!")

                elif inpt == 2:
                    if int(amount)>int(result[8]):
                        messagebox.showerror("Error","There is not enough money")
                    else:
                        statement = f'UPDATE UserData SET initialbalance = {int(result[8]) - int(amount)} WHERE CustomerID={int(self.id)};'
                        cursor.execute(statement)
                        conn.commit()
                        if self.menu.get() != 'Select Category':
                            cursor.execute(
                                "INSERT INTO Transactions VALUES (:CustomerID ,:Type ,:Category,:Amount,:Date)",
                                {'CustomerID': self.id, 'Type': 'Outcome', 'Category': self.menu.get(),
                                 'Amount': self.entry_14.get(),'Date':date.today()})
                            conn.commit()
                        messagebox.showerror("Successful", "Successfully Done!")
                statement = f"SELECT FName ,LName ,CustomerID ,Password ,Email text,Phone ,enumber ,Date ,initialbalance from UserData WHERE CustomerID={int(self.id)} AND Password = '{str(self.passwrd)}';"
                cursor.execute(statement)
                result = cursor.fetchone()
                self.label_10["text"] = f"Current Balance: {result[8]}"

            self.button13 = Button(self.root2, text='Pay/Deposit',background="#f1f59f", width=14, command=submit2)
            self.button13.place(x=650, y=530)

            def back():
                self.root2.destroy()
                signup(self)
            self.button14 = Button(self.root2, text='Back',background="#f1f59f", width=14, command=back)
            self.button14.place(x=50, y=530)
            self.root2.mainloop()

        # ebudget(self)
        def signup(self):
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS UserData (FName ,LName ,CustomerID Integer,Password ,Email text,Phone ,enumber ,Date ,initialbalance)')
            self.root = Tk()
            self.root.geometry("580x520")

            self.root.title('Signup')
            self.root.configure(background="#bff794")

            self.label =Label(self.root,text="Your Expense-Tracker!",font=("Helvetica", "20"), width=20,background="#bff794")
            self.label.place(x=150,y=40)

            self.label_0 =Label(self.root,text="First Name: ", width=20,font=("Helvetica", "13"),background="#bff794")
            self.label_0.place(x=80,y=130)

            self.entry_0=Entry(self.root,width = 40)
            self.entry_0.place(x=240,y=130)

            self.label_1 = Label(self.root, text="Last Name: ", width=20, font=("Helvetica", "13"), background="#bff794")
            self.label_1.place(x=80, y=180)

            self.entry_1 = Entry(self.root, width=40)
            self.entry_1.place(x=240, y=180)

            self.label_2 =Label(self.root,text="Customer ID:", width=20,font=("Helvetica", "13"),background="#bff794")
            self.label_2.place(x=68,y=230)

            self.entry_2=Entry(self.root,width = 40)
            self.entry_2.place(x=240,y=230)

            self.label_3 =Label(self.root,text="Password:", width=20,font=("Helvetica", "13"),background="#bff794")
            self.label_3.place(x=70,y=280)

            self.entry_3=Entry(self.root,width = 40)
            self.entry_3.place(x=240,y=280)

            self.label_4=Label(self.root,text="Email Address:",width=20,font=("Helvetica", "13"),background="#bff794")
            self.label_4.place(x=70,y=330)

            self.entry_4=Entry(self.root,width = 40)
            self.entry_4.place(x=240,y=330)

            self.label_5=Label(self.root,text="Phone Number:",width=20,font=("Helvetica", "13"),background="#bff794")
            self.label_5.place(x=75,y=380)

            self.entry_5 = Entry(self.root, width=40)
            self.entry_5.place(x=240, y=380)


            self.check = 0
            self.check1 = 0
            self.check2 = 0
            self.check3 = 0
            self.check4 = 0
            self.check5 = 0
            self.check6 = 0
            self.check7 = 0

            def submit():
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()

                self.entry_0_text = self.entry_0.get()
                pattern = r'[a-z]+'
                if re.fullmatch('[A-Za-z]{2,25}?', self.entry_0_text):
                    self.check = 0
                else:
                    messagebox.showerror("Error", "First Name: Invalid")
                    self.check +=1

                self.entry_1_text = self.entry_1.get()
                pattern = r'[a-z]+'

                if re.fullmatch('[A-Za-z]{2,25}?', self.entry_1_text):
                    self.check1 = 0
                else:
                    messagebox.showerror("Error", "Last Name: Invalid")
                    self.check1 +=1


                self.entry_2_text = self.entry_2.get()
                if len(self.entry_2_text)!=6:
                    self.check2 += 1
                    messagebox.showerror("Error", "ID: should be of 6 digits")
                else:
                    cursor.execute(
                        f"select CustomerID from UserData WHERE CustomerID='{str(self.entry_2.get())}' ORDER BY FName")
                    idcheck = cursor.fetchall()

                    if re.fullmatch('[0-9]{6}?', self.entry_2_text):
                        self.check2 = 0
                        for i in idcheck:
                            if str(i) == f'({str(self.entry_2.get())},)':
                                self.check2 += 1
                                messagebox.showerror("Error", "ID Already Registered!")
                            else:
                                self.check2 = 0
                    else:
                        messagebox.showerror("Error", "ID: Invalid")
                        self.check2 +=1

                self.entry_3_text = self.entry_3.get()
                if len(self.entry_3_text)<=7: #or self.entry_3_text[:2]!= '05':
                    messagebox.showerror("Error", "Password: Should be at least 8 digits or letters ")
                if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', self.entry_3_text):
                    self.check3 = 0
                else:
                    messagebox.showerror("Error", "Password: Invalid Password")
                    self.check3 +=1

                regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                self.entry_4_text = str(self.entry_4.get())
                if re.fullmatch(regex, self.entry_4_text):
                    self.check4 = 0
                else:
                    messagebox.showerror("Error", "Email: Invalid Email")
                    self.check4 +=1

                self.entry_5_text = self.entry_5.get()
                if len(self.entry_5_text) != 10 or self.entry_5_text[:2] != '05':
                    messagebox.showerror("Error", "Phone: Invalid Number")
                else:
                    if re.fullmatch('[0-9]{10}?', self.entry_5_text):
                        self.check5 = 0
                    else:
                        messagebox.showerror("Error", "Phone: Invalid Number")
                        self.check5 +=1


                range_start = 10 ** (6 - 1)
                range_end = (10 ** 6) - 1
                self.enumber = randint(range_start, range_end)
                self.date = date.today()
                # self.income = self.entry_6.get()
                # self.amountsaved = self.entry_7.get()
                if self.check == 0 and self.check1 == 0 and self.check2 == 0 and self.check3 == 0 and self.check4 == 0 and self.check5 == 0 and self.check6 == 0:
                    # print("CHECL",self.check)

                    conn = sqlite3.connect('database.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO UserData VALUES (:FName ,:LName ,:CustomerID ,:Password ,:Email ,:Phone ,:enumber ,:Date ,:initialbalance)",
                        {'FName': self.entry_0_text, 'LName': self.entry_1_text,
                         'CustomerID': self.entry_2_text, 'Password': self.entry_3_text, 'Email': self.entry_4_text,
                         'Phone': self.entry_5_text, 'enumber': self.enumber, 'Date': self.date,
                         'initialbalance': 0})
                    conn.commit()
                    self.root.destroy()
                    login(self)

                ###################
                # print(self.check)

            self.button3= Button(self.root, text='Signup',font=("Helvetica", "11"),background="#f1f59f" , width=10,command = submit)
            self.button3.place(x=250,y=430)
            self.root.mainloop()

        # signup(self)
        def intro_window(self):
            self.lroot3 = Tk()
            self.lroot3.geometry('500x500')
            self.lroot3.title('Login/Signup')
            self.lroot3.config(background="#f0f0f0")
            self.lroot3.resizable(False,False)

            image1 = Image.open("logo.PNG")
            image1 = image1.resize((500, 400), Image.Resampling.LANCZOS)
            test = ImageTk.PhotoImage(image1)

            label1 = tk.Label(image=test)
            label1.image = test

            # Position image
            label1.place(x=0,y = 0)

            # self.label_7 = Label(self.lroot3, text="Welcome to EXPENSE TRACKER!", width=30, font=('bold', 15))
            # self.label_7.place(x=50, y=5)

            def intro_login():
                self.lroot3.destroy()
                login(self)

            def intro_signup():
                self.lroot3.destroy()
                signup(self)

            SigninButton = Button(self.lroot3, text="Signup",font="Helvetica",background="#bff794",command = intro_signup ).place(x=220,y=350)
            self.label_7 = Label(self.lroot3, text="Already a member? Login!", width=30, font=('bold', 12))
            self.label_7.place(x=120,y=390)
            loginButton = Button(self.lroot3, text="Login",width=6, font="Helvetica", background="#bff794",
                                 command=intro_login).place(x=220, y=430)

            self.lroot3.mainloop()
        intro_window(self)


if __name__=="__main__":
    GUI()