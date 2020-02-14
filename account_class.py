from tkinter import *
from database import change_username
from account import Account


class AccountOptions:
    def __init__(self, root):
        self.root = root

        # Info labels
        # Username
        username = Account.username
        username_txt_lbl = Label(root, text="Username:")
        self.username_ent = Entry(root, width=20)
        self.username_ent.insert(0, username)
        self.username_ent.configure(state=DISABLED)
        change_username_btn = Button(root, text="Change username", command=self.change_username)

        username_txt_lbl.grid(row=0, column=0, pady=(30, 2), padx=2)
        self.username_ent.grid(row=0, column=1, pady=(30, 2))
        change_username_btn.grid(row=1, column=1)

        # Confirm button
        self.confirm_username_btn = Button(root, text="Confirm username", command=self.username_confirm)

        # Password
        password_txt_lbl = Label(root, text="Password:")
        self.password_ent = Entry(root, width=20)
        self.password_ent.insert(0, "******")
        self.password_ent.configure(state=DISABLED)
        show_password_btn = Button(root, text="Show password", command=self.show_password)
        change_password_btn = Button(root, text="Change password", command=self.change_password)

        password_txt_lbl.grid(row=2, column=0, padx=2, pady=5)
        self.password_ent.grid(row=2, column=1, padx=2, pady=5)
        show_password_btn.grid(row=3, column=0)
        change_password_btn.grid(row=3, column=1)

    def change_username(self):
        self.username_ent.configure(state=NORMAL)
        self.confirm_username_btn.grid(row=1, column=0)

    def username_confirm(self):
        print(Account.username)
        print(self.username_ent.get())
        print(Account.oid)
        change_username(self.username_ent.get(), Account.oid)

    def show_password(self):
        print("pw")

    def change_password(self):
        print("pww")
