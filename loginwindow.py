from tkinter import *
from database import create_account, admin_delete_account, show_accounts, login
import tkinter.messagebox
from account_window import Account


class LoginWindow:

    global login_status

    def __init__(self, login_window_frame, window):
        self.login_window_frame = login_window_frame
        self.window = window

        # login name and password labels
        self.label_name = Label(login_window_frame, text="Name:")
        self.label_pw = Label(login_window_frame, text="Password:")
        self.label_name.grid(row=0, column=0, pady=(5, 0))
        self.label_pw.grid(row=1, column=0)

        # login name and password entries
        self.login_name = Entry(login_window_frame, width=20)
        self.login_pw = Entry(login_window_frame, width=20)
        self.login_name.grid(row=0, column=1)
        self.login_pw.grid(row=1, column=1, padx=5)

        # insert login to save typing
        # self.login_name.insert(0, "osku")
        # self.login_pw.insert(0, "s")

        # login button initiates login
        self.login_button = Button(login_window_frame, text="Login", command=self.loginb)
        self.login_button.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        # login using enter
        self.window.bind("<Return>", self.callback)

        # exit button exits program
        self.exit_button = Button(login_window_frame, text="Exit", command=self.exitb)
        self.exit_button.grid(row=2, column=1, sticky=E, padx=10, pady=10)

        # creates new account using name and password from entries
        self.create_account_button = Button(login_window_frame, text="Create Account",
                                            command=self.new_account)
        self.create_account_button.grid(row=3, column=1, ipadx=10)

        # to be deleted
        self.delete_account_button = Button(login_window_frame, text="Delete Account",
                                            command=self.del_account)
        self.delete_account_button.grid(row=4, column=1, ipadx=10)

    def callback(self, event):
        self.loginb()

    def loginb(self):
        # database login using name and pw returns true if login details match
        login_success = login(self.login_name.get(), self.login_pw.get())
        if login_success:
            print("loggging")
            # breaks login_window.mainloop and resumes main
            self.window.destroy()

    def exitb(self):
        print("exit by exit button")
        # system exit ends program
        sys.exit()

    def new_account(self):
        # check that some data is in entries
        if (self.login_name.get() and self.login_pw.get()) != "":
            # database.createaccount(name, password, status) returns true if name available
            # # and account is created
            availability = create_account(self.login_name.get(), self.login_pw.get(), "pleb")
            if availability:
                # create message box to ask for login
                creation_successful = tkinter.messagebox.askyesno("Account creation successful!",
                                                           "Log in to your new account?")
                # if yes login if not clear name and pw entries
                if creation_successful:
                    self.loginb()
                else:
                    self.login_name.delete(0, END)
                    self.login_pw.delete(0, END)
                    return
            else:
                # availability false popup error box and clear entries
                tkinter.messagebox.showerror("Username already exists", "Choose new username")
                self.login_name.delete(0, END)
                self.login_pw.delete(0, END)
        else:
            # error to show entry or entries are empty
            tkinter.messagebox.showerror("Error", "Enter username and password to create an account")
            return

        return

    # to be deleted
    def del_account(self):
        admin_delete_account(self.login_name.get())
