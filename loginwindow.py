from tkinter import *
from database import create_account, admin_delete_account, show_accounts, login
import tkinter.messagebox
from account_class import Account


class LoginWindow:

    global login_status

    def __init__(self, login_window_frame, window):
        self.login_window_frame = login_window_frame
        self.window = window
        self.label_name = Label(login_window_frame, text="Name:")
        self.label_pw = Label(login_window_frame, text="Password:")
        self.login_name = Entry(login_window_frame, width=20)
        self.login_pw = Entry(login_window_frame, width=20)

        self.label_name.grid(row=0, column=0, pady=(5, 0))
        self.label_pw.grid(row=1, column=0)
        self.login_name.grid(row=0, column=1)
        self.login_pw.grid(row=1, column=1, padx=5)

        self.login_name.insert(0, "osku")
        self.login_pw.insert(0, "s")

        self.login_button = Button(login_window_frame, text="Login", command=self.loginb)
        self.exit_button = Button(login_window_frame, text="Exit", command=self.exitb)
        self.create_account_button = Button(login_window_frame, text="Create Account",
                                            command=self.new_account)
        self.delete_account_button = Button(login_window_frame, text="Delete Account",
                                            command=self.del_account)

        # testing button
        self.show_db_btn = Button(login_window_frame, text="show db", command=show_accounts)

        self.login_button.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        self.exit_button.grid(row=2, column=1, sticky=E, padx=10, pady=10)
        self.create_account_button.grid(row=3, column=1, ipadx=10)
        self.delete_account_button.grid(row=4, column=1, ipadx=10)

        # testing button
        self.show_db_btn.grid(row=5, column=1, ipadx=10)

    def loginb(self):
        # login_status = login.login(login_name.get(), login_pw.get())

        login_success = login(self.login_name.get(), self.login_pw.get())

        # print("no pw")
        if login_success:
            print("loggging")
            self.window.destroy()

    def exitb(self):
        print("exit by exit button")
        sys.exit()

    def new_account(self):
        print(self.login_name.get())
        if (self.login_name.get() and self.login_pw.get()) != "":
            availability = create_account(self.login_name.get(), self.login_pw.get(), "pleb")
            if availability:
                creation_successful = tkinter.messagebox.askyesno("Account creation successful!",
                                                           "Log in to your new account?")
                if creation_successful:
                    self.loginb()
                else:
                    self.login_name.delete(0, END)
                    self.login_pw.delete(0, END)
                    return
            else:
                tkinter.messagebox.showerror("Username already exists", "Choose new username")
                self.login_name.delete(0, END)
                self.login_pw.delete(0, END)
        else:
            tkinter.messagebox.showerror("Error", "Enter username and password to create an account")
            return

        return

    def show_db(self):
        try:
            show_table(self.login_name.get())
        except NameError:
            print("enter correct table name")

    def del_account(self):
        admin_delete_account(self.login_name.get())
